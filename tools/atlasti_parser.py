#!/usr/bin/env python3
"""
Atlas.ti Project Parser for ResearchKit Quals

Extracts coded quotations from Atlas.ti .atlpac archives.
Outputs JSON format suitable for anonymization and assessment materials.

Usage:
    python atlasti_parser.py <path_to_atlpac_or_extracted_dir> [output_file]
"""

import json
import xml.etree.ElementTree as ET
import zipfile
import tempfile
import shutil
import re
from pathlib import Path
from dataclasses import dataclass, asdict, field
from typing import Dict, List, Optional, Tuple
from html.parser import HTMLParser


@dataclass
class Code:
    """A code (tag) in Atlas.ti terminology."""
    id: str
    name: str
    created: str
    modified: str
    group: Optional[str] = None


@dataclass
class Quotation:
    """A coded segment of text."""
    id: str
    document_id: str
    document_name: str
    start_segment: int
    start_offset: int
    end_segment: int
    end_offset: int
    text: str
    codes: List[str] = field(default_factory=list)  # Code names, not IDs


@dataclass
class Document:
    """A source document (interview, field notes, etc.)."""
    id: str
    name: str
    guid: str  # dataSource GUID (folder name in /documents/)
    path: str  # Original file path
    segments: Dict[int, str] = field(default_factory=dict)  # segment_id -> text content


class AtlasHTMLParser(HTMLParser):
    """
    Parse Atlas.ti HTML documents, extracting text by segment ID.

    Atlas.ti stores documents as HTML where each text segment has an ID
    in the format: <span id="N">text content</span>

    Quotation locations reference these segment IDs and character offsets.
    """

    def __init__(self):
        super().__init__()
        self.segments: Dict[int, str] = {}
        self.current_segment_id: Optional[int] = None
        self.current_text: List[str] = []
        self.in_body = False

    def handle_starttag(self, tag, attrs):
        if tag == 'body':
            self.in_body = True
            return

        if not self.in_body:
            return

        # Check for segment ID
        attrs_dict = dict(attrs)
        if 'id' in attrs_dict:
            try:
                segment_id = int(attrs_dict['id'])
                # Save any pending text from previous segment
                if self.current_segment_id is not None and self.current_text:
                    self.segments[self.current_segment_id] = ''.join(self.current_text)
                self.current_segment_id = segment_id
                self.current_text = []
            except ValueError:
                pass  # Not a numeric ID

    def handle_endtag(self, tag):
        if tag == 'body':
            # Save final segment
            if self.current_segment_id is not None and self.current_text:
                self.segments[self.current_segment_id] = ''.join(self.current_text)
            self.in_body = False

    def handle_data(self, data):
        if self.in_body and self.current_segment_id is not None:
            self.current_text.append(data)

    def get_segments(self) -> Dict[int, str]:
        return self.segments


def parse_html_segments(html_content: str) -> Dict[int, str]:
    """Parse HTML and return segment ID -> text mapping."""
    parser = AtlasHTMLParser()
    parser.feed(html_content)
    return parser.get_segments()


def extract_quotation_text(segments: Dict[int, str],
                           start_seg: int, start_off: int,
                           end_seg: int, end_off: int) -> str:
    """
    Extract text for a quotation given segment IDs and offsets.

    Args:
        segments: Dict mapping segment ID to text content
        start_seg: Starting segment ID
        start_off: Character offset within starting segment
        end_seg: Ending segment ID
        end_off: Character offset within ending segment

    Returns:
        The extracted text
    """
    if start_seg == end_seg:
        # Single segment quotation
        if start_seg in segments:
            text = segments[start_seg]
            return text[start_off:end_off]
        return ""

    # Multi-segment quotation
    parts = []

    # Get all segment IDs between start and end
    seg_ids = sorted([s for s in segments.keys() if start_seg <= s <= end_seg])

    for i, seg_id in enumerate(seg_ids):
        text = segments.get(seg_id, "")
        if seg_id == start_seg:
            parts.append(text[start_off:])
        elif seg_id == end_seg:
            parts.append(text[:end_off])
        else:
            parts.append(text)

    return '\n'.join(parts)


def extract_atlpac(atlpac_path: Path) -> Path:
    """Extract .atlpac (ZIP) to temp directory. Returns extraction path."""
    temp_dir = Path(tempfile.mkdtemp(prefix='atlasti_'))
    with zipfile.ZipFile(atlpac_path, 'r') as zf:
        zf.extractall(temp_dir)
    return temp_dir


def parse_project(project_dir: Path) -> dict:
    """
    Parse an extracted Atlas.ti project.

    Args:
        project_dir: Path to extracted project (containing Project.aprx)

    Returns:
        dict with codes, documents, quotations, and metadata
    """
    aprx_path = project_dir / 'Project.aprx'
    if not aprx_path.exists():
        raise FileNotFoundError(f"Project.aprx not found in {project_dir}")

    tree = ET.parse(aprx_path)
    root = tree.getroot()

    # Parse codes (tags)
    codes = {}
    tag_to_group = {}

    # First pass: get tag groups
    for tag_group in root.findall('.//tagGroup'):
        group_name = tag_group.get('name')
        for item in tag_group.findall('item'):
            tag_id = item.get('id')
            tag_to_group[tag_id] = group_name

    # Second pass: get tags
    for tag in root.findall('.//tag'):
        tag_id = tag.get('id')
        codes[tag_id] = Code(
            id=tag_id,
            name=tag.get('name'),
            created=tag.get('cDate', ''),
            modified=tag.get('mDate', ''),
            group=tag_to_group.get(tag_id)
        )

    # Parse data sources (maps ID to GUID for folder lookup)
    data_sources = {}
    for ds in root.findall('.//dataSource'):
        ds_id = ds.get('id')
        data_sources[ds_id] = {
            'guid': ds.get('loc'),  # This is the folder name in /documents/
            'name': ds.get('name', ''),
            'path': ds.get('origin', ''),
        }

    # Parse documents with their quotations
    documents = {}
    all_quotations = []
    docs_dir = project_dir / 'documents'

    for doc in root.findall('.//document'):
        doc_id = doc.get('id')
        doc_name = doc.get('name', f'Unknown-{doc_id}')
        ds_ref = doc.get('loc')  # Reference to dataSource

        # Get the folder GUID from dataSource
        ds_info = data_sources.get(ds_ref, {})
        doc_guid = ds_info.get('guid', '')

        document = Document(
            id=doc_id,
            name=doc_name,
            guid=doc_guid,
            path=ds_info.get('path', '')
        )

        # Load document content and parse segments
        if doc_guid:
            content_path = docs_dir / doc_guid / 'content'
            if content_path.exists():
                try:
                    html_content = content_path.read_text(encoding='utf-8')
                    document.segments = parse_html_segments(html_content)
                except Exception as e:
                    print(f"Warning: Could not read content for {doc_name}: {e}")

        documents[doc_id] = document

        # Parse quotations for this document
        for quot_elem in doc.findall('.//q'):
            quot_id = quot_elem.get('id')

            # Get location
            loc = quot_elem.find('.//segmentedTextLoc')
            if loc is not None:
                start_seg = int(loc.get('sSegment', 0))
                start_off = int(loc.get('sOffset', 0))
                end_seg = int(loc.get('eSegment', 0))
                end_off = int(loc.get('eOffset', 0))

                # Extract text
                text = extract_quotation_text(
                    document.segments,
                    start_seg, start_off,
                    end_seg, end_off
                )

                if text:
                    all_quotations.append(Quotation(
                        id=quot_id,
                        document_id=doc_id,
                        document_name=doc_name,
                        start_segment=start_seg,
                        start_offset=start_off,
                        end_segment=end_seg,
                        end_offset=end_off,
                        text=text.strip(),
                        codes=[]  # Will be filled from links
                    ))

    # Parse tag-quotation links
    quot_id_to_codes = {}
    for link in root.findall('.//tagQuotLink'):
        tag_id = link.get('source')
        quot_id = link.get('target')

        if quot_id not in quot_id_to_codes:
            quot_id_to_codes[quot_id] = []

        if tag_id in codes:
            quot_id_to_codes[quot_id].append(codes[tag_id].name)

    # Apply codes to quotations
    for quot in all_quotations:
        quot.codes = quot_id_to_codes.get(quot.id, [])

    # Filter to only coded quotations
    coded_quotations = [q for q in all_quotations if q.codes]

    return {
        'codes': {k: asdict(v) for k, v in codes.items()},
        'code_groups': list(set(tag_to_group.values())),
        'documents': {
            k: {
                'id': v.id,
                'name': v.name,
                'guid': v.guid,
                'path': v.path,
                'segment_count': len(v.segments)
            }
            for k, v in documents.items()
        },
        'quotations': [asdict(q) for q in coded_quotations],
        'stats': {
            'total_codes': len(codes),
            'total_documents': len(documents),
            'documents_with_content': len([d for d in documents.values() if d.segments]),
            'total_quotations': len(all_quotations),
            'coded_quotations': len(coded_quotations),
        }
    }


def main():
    import sys

    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2]) if len(sys.argv) > 2 else None

    # Handle .atlpac or extracted directory
    if input_path.suffix.lower() == '.atlpac':
        print(f"Extracting {input_path}...")
        project_dir = extract_atlpac(input_path)
        cleanup = True
    else:
        project_dir = input_path
        cleanup = False

    try:
        print(f"Parsing project in {project_dir}...")
        result = parse_project(project_dir)

        print(f"\nExtracted:")
        print(f"  - {result['stats']['total_codes']} codes")
        print(f"  - {result['stats']['total_documents']} documents ({result['stats']['documents_with_content']} with content)")
        print(f"  - {result['stats']['total_quotations']} total quotations")
        print(f"  - {result['stats']['coded_quotations']} coded quotations")

        if result['code_groups']:
            print(f"\nCode groups: {', '.join(result['code_groups'])}")

        if output_path:
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(result, f, indent=2, ensure_ascii=False)
            print(f"\nOutput written to {output_path}")
        else:
            # Print sample
            print("\nSample codes:")
            for code in list(result['codes'].values())[:5]:
                group = f" ({code.get('group')})" if code.get('group') else ""
                print(f"  - {code['name']}{group}")

            print("\nSample coded quotations:")
            for quot in result['quotations'][:5]:
                text_preview = quot['text'][:100] + '...' if len(quot['text']) > 100 else quot['text']
                print(f"\n  [{', '.join(quot['codes'])}]")
                print(f"  From: {quot['document_name']}")
                print(f"  \"{text_preview}\"")

    finally:
        if cleanup:
            shutil.rmtree(project_dir)


if __name__ == '__main__':
    main()
