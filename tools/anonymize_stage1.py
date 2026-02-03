#!/usr/bin/env python3
"""
Anonymization Engine - Stage 1: Automatic NER Detection

Scans text for entities that need anonymization:
- PERSON: Names of people
- ORG: Organizations, hospitals, companies
- GPE: Geographic locations (cities, states, countries)
- DATE: Dates that could identify
- FAC: Facilities (specific rooms, floors, buildings)

Also detects patterns via regex:
- Email addresses
- Phone numbers
- Medical record numbers
- Specific role+context combinations

Usage:
    python anonymize_stage1.py <input_json> [output_json]

Input: JSON from atlasti_parser.py (has quotations and documents)
Output: JSON with entities detected, flagged for review
"""

import json
import re
import sys
from pathlib import Path
from dataclasses import dataclass, asdict, field
from typing import Dict, List, Set, Optional, Tuple
from collections import defaultdict

# Try to import spaCy for NER
try:
    import spacy
    SPACY_AVAILABLE = True
except ImportError:
    SPACY_AVAILABLE = False
    print("Warning: spaCy not available. Using regex-only detection.")


@dataclass
class DetectedEntity:
    """An entity detected in text."""
    text: str
    entity_type: str  # PERSON, ORG, GPE, DATE, FAC, EMAIL, PHONE, PATTERN
    start: int
    end: int
    confidence: str  # HIGH, MEDIUM, LOW
    source: str  # 'ner', 'regex', 'dictionary'
    context: str  # Surrounding text for review
    suggested_replacement: Optional[str] = None


@dataclass
class DocumentAnalysis:
    """Analysis results for a single document."""
    document_id: str
    document_name: str
    entities: List[DetectedEntity] = field(default_factory=list)
    flags: List[str] = field(default_factory=list)  # Warnings/concerns


# Common name patterns that indicate PERSON entities
TITLE_PATTERNS = [
    r'\b(Dr\.?|Mr\.?|Mrs\.?|Ms\.?|Prof\.?|Professor)\s+([A-Z][a-z]+)',
    r'\b(Doctor|Nurse|Attending|Resident|Chief|Senior|Junior)\s+([A-Z][a-z]+)',
]

# Regex patterns for PII
REGEX_PATTERNS = {
    'EMAIL': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
    'PHONE': r'\b(\+?1[-.]?)?\(?\d{3}\)?[-.]?\d{3}[-.]?\d{4}\b',
    'DATE_MDY': r'\b(0?[1-9]|1[0-2])[-/](0?[1-9]|[12]\d|3[01])[-/](19|20)?\d{2}\b',
    'DATE_YMD': r'\b(19|20)\d{2}[-/](0?[1-9]|1[0-2])[-/](0?[1-9]|[12]\d|3[01])\b',
    'TIME': r'\b([01]?\d|2[0-3]):([0-5]\d)(:[0-5]\d)?\s*(AM|PM|am|pm)?\b',
    'MRN': r'\b(MRN|mrn|Medical Record|medical record)[\s:#]*\d{5,10}\b',
    'SSN': r'\b\d{3}[-]?\d{2}[-]?\d{4}\b',
}

# Medical/hospital specific patterns
MEDICAL_PATTERNS = {
    'OR_NUMBER': r'\bOR\s*\d+\b',
    'ROOM_NUMBER': r'\b(Room|Rm\.?)\s*\d+[A-Z]?\b',
    'FLOOR': r'\b(\d+)(st|nd|rd|th)\s+floor\b',
    'UNIT': r'\b(Unit|Ward)\s+[A-Z0-9]+\b',
}

# Common hospital/org names to detect (case-insensitive patterns)
HOSPITAL_PATTERNS = [
    r'\b(Lahey|Faulkner|MGH|Massachusetts General|B&W|Brigham|Parkland)\b',
    r'\b(Hospital|Medical Center|Clinic|Health System)\b',
]

# Role patterns that might identify individuals
ROLE_PATTERNS = [
    r'\b(chief resident|senior resident|junior resident|attending|fellow)\b',
    r'\b(scrub nurse|circulating nurse|OR nurse|charge nurse)\b',
    r'\b(anesthesiologist|anesthetist|CRNA)\b',
]


class AnonymizationDetector:
    """Detects entities needing anonymization in text."""

    def __init__(self, custom_dictionary: Optional[Dict[str, List[str]]] = None):
        """
        Initialize detector.

        Args:
            custom_dictionary: Optional dict mapping entity types to known terms
                               e.g., {'ORG': ['Lahey', 'MGH'], 'PERSON': ['Dr. Smith']}
        """
        self.nlp = None
        if SPACY_AVAILABLE:
            try:
                self.nlp = spacy.load('en_core_web_sm')
            except OSError:
                print("Warning: spaCy model 'en_core_web_sm' not found.")
                print("Install with: python -m spacy download en_core_web_sm")

        self.custom_dictionary = custom_dictionary or {}

        # Compile regex patterns
        self.compiled_patterns = {}
        for name, pattern in {**REGEX_PATTERNS, **MEDICAL_PATTERNS}.items():
            self.compiled_patterns[name] = re.compile(pattern, re.IGNORECASE)

        self.hospital_patterns = [re.compile(p, re.IGNORECASE) for p in HOSPITAL_PATTERNS]
        self.role_patterns = [re.compile(p, re.IGNORECASE) for p in ROLE_PATTERNS]
        self.title_patterns = [re.compile(p) for p in TITLE_PATTERNS]

    def get_context(self, text: str, start: int, end: int, window: int = 40) -> str:
        """Get surrounding context for an entity."""
        ctx_start = max(0, start - window)
        ctx_end = min(len(text), end + window)
        prefix = '...' if ctx_start > 0 else ''
        suffix = '...' if ctx_end < len(text) else ''
        return f"{prefix}{text[ctx_start:ctx_end]}{suffix}"

    def detect_with_ner(self, text: str) -> List[DetectedEntity]:
        """Detect entities using spaCy NER."""
        if not self.nlp:
            return []

        entities = []
        doc = self.nlp(text)

        for ent in doc.ents:
            # Filter to relevant entity types
            if ent.label_ in ('PERSON', 'ORG', 'GPE', 'FAC', 'DATE', 'TIME'):
                confidence = 'HIGH' if ent.label_ in ('PERSON', 'ORG') else 'MEDIUM'

                entities.append(DetectedEntity(
                    text=ent.text,
                    entity_type=ent.label_,
                    start=ent.start_char,
                    end=ent.end_char,
                    confidence=confidence,
                    source='ner',
                    context=self.get_context(text, ent.start_char, ent.end_char)
                ))

        return entities

    def detect_with_regex(self, text: str) -> List[DetectedEntity]:
        """Detect entities using regex patterns."""
        entities = []

        # Standard PII patterns
        for pattern_name, pattern in self.compiled_patterns.items():
            for match in pattern.finditer(text):
                # Map pattern names to entity types
                if pattern_name.startswith('DATE') or pattern_name == 'TIME':
                    entity_type = 'DATE'
                elif pattern_name in ('EMAIL', 'PHONE', 'MRN', 'SSN'):
                    entity_type = pattern_name
                else:
                    entity_type = 'FAC'  # OR_NUMBER, ROOM_NUMBER, etc.

                entities.append(DetectedEntity(
                    text=match.group(),
                    entity_type=entity_type,
                    start=match.start(),
                    end=match.end(),
                    confidence='HIGH',
                    source='regex',
                    context=self.get_context(text, match.start(), match.end())
                ))

        # Hospital/org patterns
        for pattern in self.hospital_patterns:
            for match in pattern.finditer(text):
                entities.append(DetectedEntity(
                    text=match.group(),
                    entity_type='ORG',
                    start=match.start(),
                    end=match.end(),
                    confidence='HIGH',
                    source='regex',
                    context=self.get_context(text, match.start(), match.end())
                ))

        # Title + Name patterns (e.g., "Dr. Smith")
        for pattern in self.title_patterns:
            for match in pattern.finditer(text):
                entities.append(DetectedEntity(
                    text=match.group(),
                    entity_type='PERSON',
                    start=match.start(),
                    end=match.end(),
                    confidence='HIGH',
                    source='regex',
                    context=self.get_context(text, match.start(), match.end())
                ))

        return entities

    def detect_with_dictionary(self, text: str) -> List[DetectedEntity]:
        """Detect entities using custom dictionary."""
        entities = []

        for entity_type, terms in self.custom_dictionary.items():
            for term in terms:
                pattern = re.compile(re.escape(term), re.IGNORECASE)
                for match in pattern.finditer(text):
                    entities.append(DetectedEntity(
                        text=match.group(),
                        entity_type=entity_type,
                        start=match.start(),
                        end=match.end(),
                        confidence='HIGH',
                        source='dictionary',
                        context=self.get_context(text, match.start(), match.end())
                    ))

        return entities

    def detect_role_combinations(self, text: str) -> List[str]:
        """
        Flag potentially identifying role + context combinations.

        Returns list of warning flags.
        """
        flags = []

        # Check for role mentions
        roles_found = []
        for pattern in self.role_patterns:
            for match in pattern.finditer(text):
                roles_found.append(match.group().lower())

        if roles_found:
            # Check for demographic or temporal context
            has_gender = bool(re.search(r'\b(he|she|his|her|female|male)\b', text, re.I))
            has_year = bool(re.search(r'\b(19|20)\d{2}\b', text))
            has_specialty = bool(re.search(r'\b(urology|surgery|cardio|neuro|ortho)\b', text, re.I))

            if has_gender and has_year:
                flags.append(f"⚠️ COMBO RISK: role ({roles_found[0]}) + gender + year could identify")
            if has_specialty and has_year:
                flags.append(f"⚠️ COMBO RISK: role ({roles_found[0]}) + specialty + year could identify")

        return flags

    def detect_all(self, text: str) -> Tuple[List[DetectedEntity], List[str]]:
        """
        Run all detection methods on text.

        Returns:
            (list of entities, list of warning flags)
        """
        entities = []
        flags = []

        # Run all detection methods
        entities.extend(self.detect_with_ner(text))
        entities.extend(self.detect_with_regex(text))
        entities.extend(self.detect_with_dictionary(text))

        # Check for risky combinations
        flags.extend(self.detect_role_combinations(text))

        # Deduplicate entities by position
        seen = set()
        unique_entities = []
        for ent in entities:
            key = (ent.start, ent.end, ent.entity_type)
            if key not in seen:
                seen.add(key)
                unique_entities.append(ent)

        # Sort by position
        unique_entities.sort(key=lambda e: e.start)

        return unique_entities, flags


def analyze_atlas_export(input_path: Path, custom_dict: Optional[Dict] = None) -> dict:
    """
    Analyze an Atlas.ti export JSON for entities needing anonymization.

    Args:
        input_path: Path to JSON from atlasti_parser.py
        custom_dict: Optional custom dictionary for detection

    Returns:
        Analysis results with detected entities
    """
    with open(input_path) as f:
        data = json.load(f)

    detector = AnonymizationDetector(custom_dictionary=custom_dict)

    # Track all entities across documents
    all_entities = defaultdict(list)  # entity_text -> list of occurrences
    document_analyses = []

    # Analyze each quotation
    for quot in data.get('quotations', []):
        text = quot.get('text', '')
        doc_id = quot.get('document_id', '')
        doc_name = quot.get('document_name', '')

        entities, flags = detector.detect_all(text)

        if entities or flags:
            analysis = DocumentAnalysis(
                document_id=doc_id,
                document_name=doc_name,
                entities=entities,
                flags=flags
            )
            document_analyses.append(analysis)

            # Track entity occurrences
            for ent in entities:
                all_entities[ent.text.lower()].append({
                    'original': ent.text,
                    'type': ent.entity_type,
                    'document': doc_name,
                    'context': ent.context
                })

    # Generate entity summary
    entity_summary = []
    for text, occurrences in sorted(all_entities.items(), key=lambda x: -len(x[1])):
        # Get most common type for this entity
        types = [o['type'] for o in occurrences]
        most_common_type = max(set(types), key=types.count)

        entity_summary.append({
            'text': occurrences[0]['original'],  # Use original casing
            'normalized': text,
            'type': most_common_type,
            'count': len(occurrences),
            'sample_contexts': [o['context'] for o in occurrences[:3]],
            'suggested_replacement': None,  # To be filled in Stage 2
            'review_status': 'pending'
        })

    return {
        'source_file': str(input_path),
        'stats': {
            'total_quotations': len(data.get('quotations', [])),
            'quotations_with_entities': len(document_analyses),
            'unique_entities': len(entity_summary),
            'total_entity_occurrences': sum(e['count'] for e in entity_summary),
        },
        'entity_summary': sorted(entity_summary, key=lambda x: -x['count']),
        'document_analyses': [asdict(a) for a in document_analyses],
        'review_required': True,
    }


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2]) if len(sys.argv) > 2 else None

    # Optional: Load custom dictionary
    custom_dict = None
    # custom_dict = {'ORG': ['Lahey', 'MGH', 'Parkland'], 'PERSON': ['Dr. Canes']}

    print(f"Analyzing {input_path}...")
    results = analyze_atlas_export(input_path, custom_dict)

    print(f"\nDetection complete:")
    print(f"  - {results['stats']['total_quotations']} quotations analyzed")
    print(f"  - {results['stats']['quotations_with_entities']} contain entities")
    print(f"  - {results['stats']['unique_entities']} unique entities found")
    print(f"  - {results['stats']['total_entity_occurrences']} total occurrences")

    if results['entity_summary']:
        print("\nTop entities detected:")
        for ent in results['entity_summary'][:10]:
            print(f"  [{ent['type']}] \"{ent['text']}\" - {ent['count']} occurrences")

    if output_path:
        with open(output_path, 'w') as f:
            json.dump(results, f, indent=2)
        print(f"\nResults written to {output_path}")
        print("Next step: Review entities in Stage 2 (guided human review)")


if __name__ == '__main__':
    main()
