# Anonymization Audit Report

**Generated**: 2026-02-02 14:03
**Source file**: 69 quotations

---

## Summary Statistics

- **Total replacements made**: 8
- **Unique terms replaced**: 6

### Replacement Counts by Type

- GPE: 5
- PERSON: 2
- FAC: 1

---

## Replacement Mapping

| Original | Replacement | Type |
|----------|-------------|------|
| Danielle | [informant] | GPE |
| brazil | Mexico | GPE |
| Kate | Person A | PERSON |
| 7:56:44 AM Danielle | 7:56:44 AM [informant] | TIME |
| 9:56:55 AM Kate | 9:56:55 AM [informant] | TIME |
| OR 2 | OR X | FAC |

---

## Detailed Change Log

### By Document

#### 2013.07.09 R Partial nephrectomy.rtf

- `Danielle` → `[informant]` (GPE)
- `Kate` → `Person A` (PERSON)
- `Danielle` → `[informant]` (GPE)
- `Danielle` → `[informant]` (GPE)
- `Kate` → `Person A` (PERSON)

#### 2015.06.03 RALP.rtf

- `brazil` → `Mexico` (GPE)
- `brazil` → `Mexico` (GPE)

#### 2015.07.01 R Pyleoplasty.rtf

- `OR 2` → `OR X` (FAC)

---

## Items Kept As-Is

The following detected entities were reviewed and determined to not require anonymization:

- **Dude** (PERSON): 
- **7:55:55 AM** (DATE): time date stamp
- **8:31:31 AM** (DATE): time date stamp
- **9:57:45 AM** (DATE): 
- **that week** (DATE): 
- **7:20:48 AM** (DATE): 
- **today** (DATE): 
- **8:48:04 AM** (DATE): 
- **8:53:27 AM** (DATE): 
- **9:00:21 AM** (DATE): 
- **7:56:44 AM** (DATE): 
- **8:25:32 AM Moved** (TIME): 
- **8:25:32 AM** (DATE): 
- **8:27:50 AM Move** (TIME): 
- **8:27:50 AM** (DATE): 
- **CT** (ORG): 
- **IVC** (ORG): 
- **GV** (ORG): 
- **RV** (GPE): 
- **ddon’t** (GPE): 
- **cursor** (GPE): 
- **9:56:55 AM** (DATE): 
- **30 minutes** (TIME): 
- **20 of those minutes** (TIME): 
- **Anesth** (PERSON): 
- **every year** (DATE): 
- **8 days** (DATE): 
- **the end of the week** (DATE): 
- **matt bean** (PERSON): 
- **the day** (DATE): 
- **9:14:31 AM ***** (TIME): 
- **9:14:31 AM** (DATE): 
- **July 1** (DATE): 
- **this morning** (TIME): 
- **room 17** (FAC): 
- **K’s** (ORG): 
- **9:52:03 AM
M** (TIME): 
- **9:52:03 AM** (DATE): 
- **10 minutes** (TIME): 
- **10:57:27 AM
M: it** (TIME): k
- **10:57:27 AM** (DATE): 
- **hospital** (ORG): 
- **11:41:55 AM
M:** (TIME): 
- **11:41:55 AM** (DATE): 

---

## False Positives

The following NER detections were marked as false positives:

- n’t (GPE)
- putin (PERSON)