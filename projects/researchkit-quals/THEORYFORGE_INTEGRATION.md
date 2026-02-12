# TheoryForge Integration

> This document preserves the mapping between research competency domains and TheoryForge commands. It is separated from the core competency definitions to allow the domains to be discussed and refined independently of any particular tool.

---

## Command-to-Domain Unlock Map

Each TheoryForge command requires demonstrated competence in specific domains. Some commands have multiple access modes (guided → full) gated by different levels.

| Command | Description | Requirements | Mode/Notes |
|---------|-------------|--------------|------------|
| `/explore-data` | Basic data exploration | None | Always available |
| `/hunt-patterns` | Find robust empirical patterns | D1:L2 (guided), D1:L3 (full) | Guided shows AI reasoning |
| `/find-theory` | Identify violated/extended theory | D1:L3 + D2:L2 (guided), D1:L3 + D2:L3 (full) | |
| `/find-lens` | Select sensitizing literature | D1:L3 + D2:L2 (guided), D1:L3 + D2:L3 (full) | |
| `/eval-zuckerman-lite` | Quick puzzle check | D1:L3 + D2:L3 | Single mode |
| `/mine-qual` | Extract mechanism evidence from qual data | D2:L3 + D3:L2 (scaffolded), D2:L3 + D3:L3 (full) | Scaffolded requires coding 3 interviews manually first |
| `/smith-frames` | Generate theoretical framings | D3:L3 + D4:L2 (comparison), D3:L3 + D4:L3 (full) | Comparison: student writes first |
| `/eval-zuckerman` | Full 10-criteria academic framing check | D3:L3 + D4:L3 | Single mode |
| `/eval-becker` | Generalizability test | D4:L3 | Single mode |
| `/eval-genre` | Inductive vs deductive framing check | D4:L3 + D5:L3 | Single mode |
| `/draft-paper` | Generate full manuscript | D4:L3 + D5:L3 | Single mode |
| `/audit-claims` | Adversarial evidence search | D5:L3 + D6:L3 | Single mode |
| `/verify-claims` | Create verification package | D5:L3 + D6:L3 | Single mode |
| `/package-verification` | Final verification for external review | D6:L3 + D7:L3 | Full access — all domains complete |

---

## Domain → Command Mapping (by domain)

| Domain | Commands Unlocked at L2 | Commands Unlocked at L3 |
|--------|------------------------|------------------------|
| 1. Pattern Recognition | `/hunt-patterns` (guided) | `/hunt-patterns` (full) |
| 2. Theoretical Positioning | `/find-theory`, `/find-lens` (guided) | `/find-theory`, `/find-lens` (full), `/eval-zuckerman-lite` |
| 3. Qual Mechanism Extraction | `/mine-qual` (scaffolded: must code 3 interviews manually first) | `/mine-qual` (full) |
| 4. Theoretical Framing | `/smith-frames` (comparison: student writes first) | `/smith-frames` (full), `/eval-zuckerman`, `/eval-becker` |
| 5. Epistemological Genre | — | `/eval-genre`, `/draft-paper` |
| 6. Adversarial Evidence | — | `/audit-claims`, `/verify-claims` |
| 7. Claim Verification | — | `/package-verification` |

---

## Competency Gate Implementation

When TheoryForge integration is built, the gating function goes in `theory-forge/lib/competency_gate.py`:

```python
import json
from pathlib import Path

UNLOCK_MAP = {
    "hunt-patterns": {"domain-1": 3},
    "find-theory": {"domain-1": 3, "domain-2": 3},
    "mine-qual": {"domain-2": 3, "domain-3": 3},
    "smith-frames": {"domain-3": 3, "domain-4": 3},
    "eval-zuckerman": {"domain-3": 3, "domain-4": 3},
    "eval-genre": {"domain-4": 3, "domain-5": 3},
    "draft-paper": {"domain-4": 3, "domain-5": 3},
    "audit-claims": {"domain-5": 3, "domain-6": 3},
    "verify-claims": {"domain-5": 3, "domain-6": 3},
    "package-verification": {"domain-6": 3, "domain-7": 3},
}

def check_competency(command: str, student_id: str = None) -> tuple[bool, str]:
    """
    Check if student can run this command.
    Returns (allowed, message).
    """
    if command not in UNLOCK_MAP:
        return True, ""  # Ungated command

    # Find student record
    if not student_id:
        id_file = Path.home() / ".researchkit-quals" / "student-id"
        if not id_file.exists():
            return True, ""  # No quals system configured
        student_id = id_file.read_text().strip()

    record_path = Path.home() / ".researchkit-quals" / student_id / "unlock-status.json"
    if not record_path.exists():
        return True, ""  # No record = no restrictions (faculty/expert mode)

    record = json.loads(record_path.read_text())
    requirements = UNLOCK_MAP[command]

    missing = []
    for domain, level in requirements.items():
        student_level = record.get("domains", {}).get(domain, {}).get("level", 0)
        if student_level < level:
            missing.append(f"{domain} Level {level}")

    if missing:
        msg = f"/{command} requires: {', '.join(missing)}\n"
        msg += f"Run /quals-status to see your progress."
        return False, msg

    return True, ""
```

### Usage in Command Files

Add to top of each gated command:

```markdown
## Competency Gate

Before running this command, the system checks competency status.

If you see a "Locked" message, you need to complete the required
assessments first. Run `/quals-status` for details.

Faculty and expert users (no student record) are not gated.
```

---

## quals-status TheoryForge Display

When TheoryForge integration is active, the `/quals-status` command should also display command access:

```
THEORYFORGE ACCESS
════════════════════════════════════════════════════════════════

AVAILABLE
├── /explore-data (always available)
├── /hunt-patterns (guided mode)
└── /hunt-patterns (full mode)

PARTIAL ACCESS
├── /find-theory (guided mode) - need Domain 2, Level 3
└── /mine-qual (scaffolded) - need Domain 3, Level 2

LOCKED
├── /smith-frames - need Domain 4, Level 2
├── /eval-zuckerman - need Domain 4, Level 3
├── /audit-claims - need Domain 6, Level 3
└── /package-verification - need Domain 7, Level 3
```

---

## Full unlock-map.json

The complete structured mapping is preserved below for programmatic use:

```json
{
  "description": "Maps TheoryForge commands to required competency levels",
  "version": "1.0.0",

  "commands": {
    "/explore-data": {
      "description": "Basic data exploration",
      "mode": "always_available",
      "requirements": {},
      "notes": "Entry point - no gates"
    },
    "/hunt-patterns": {
      "description": "Find robust empirical patterns",
      "modes": {
        "guided": {
          "requirements": { "domain-1": 2 },
          "features": ["Shows AI reasoning", "Comparison to student predictions"]
        },
        "full": {
          "requirements": { "domain-1": 3 },
          "features": ["Full autonomy", "RASC adaptive stopping"]
        }
      }
    },
    "/find-theory": {
      "description": "Identify violated/extended theory",
      "modes": {
        "guided": {
          "requirements": { "domain-1": 3, "domain-2": 2 },
          "features": ["Shows theory search reasoning", "Explains violations"]
        },
        "full": {
          "requirements": { "domain-1": 3, "domain-2": 3 },
          "features": ["Full autonomy"]
        }
      }
    },
    "/find-lens": {
      "description": "Select sensitizing literature",
      "modes": {
        "guided": {
          "requirements": { "domain-1": 3, "domain-2": 2 },
          "features": ["Shows search reasoning", "Explains bridging"]
        },
        "full": {
          "requirements": { "domain-1": 3, "domain-2": 3 },
          "features": ["Full autonomy"]
        }
      }
    },
    "/eval-zuckerman-lite": {
      "description": "Quick puzzle check (early stage)",
      "mode": "single",
      "requirements": { "domain-1": 3, "domain-2": 3 }
    },
    "/mine-qual": {
      "description": "Extract mechanism evidence from qualitative data",
      "modes": {
        "scaffolded": {
          "requirements": { "domain-2": 3, "domain-3": 2 },
          "features": ["Must code 3 interviews manually first", "Comparison to AI coding"]
        },
        "full": {
          "requirements": { "domain-2": 3, "domain-3": 3 },
          "features": ["Full autonomy", "Consensus mode available"]
        }
      }
    },
    "/smith-frames": {
      "description": "Generate theoretical framings",
      "modes": {
        "comparison": {
          "requirements": { "domain-3": 3, "domain-4": 2 },
          "features": ["Student writes framing first", "AI framings shown for comparison"]
        },
        "full": {
          "requirements": { "domain-3": 3, "domain-4": 3 },
          "features": ["Full autonomy", "Adversarial evaluation"]
        }
      }
    },
    "/eval-zuckerman": {
      "description": "Full 10-criteria academic framing check",
      "mode": "single",
      "requirements": { "domain-3": 3, "domain-4": 3 }
    },
    "/eval-becker": {
      "description": "Generalizability test",
      "mode": "single",
      "requirements": { "domain-4": 3 }
    },
    "/eval-genre": {
      "description": "Inductive vs deductive framing check",
      "mode": "single",
      "requirements": { "domain-4": 3, "domain-5": 3 }
    },
    "/draft-paper": {
      "description": "Generate full manuscript",
      "mode": "single",
      "requirements": { "domain-4": 3, "domain-5": 3 }
    },
    "/audit-claims": {
      "description": "Adversarial evidence search",
      "mode": "single",
      "requirements": { "domain-5": 3, "domain-6": 3 }
    },
    "/verify-claims": {
      "description": "Create verification package",
      "mode": "single",
      "requirements": { "domain-5": 3, "domain-6": 3 }
    },
    "/package-verification": {
      "description": "Final verification package for external review",
      "mode": "single",
      "requirements": { "domain-6": 3, "domain-7": 3 },
      "notes": "Full access - requires all domains complete"
    }
  }
}
```
