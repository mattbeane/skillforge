#!/usr/bin/env python3
"""ResearchKit Quals CLI - PhD competency assessment system.

Commands:
    init     Create a new student record
    status   Show competency progress
    take     Take a Level 1 assessment
    certify  Advisor certification bypass
"""

import argparse
import json
import os
import random
import re
import sys
import textwrap
from datetime import datetime
from pathlib import Path

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

QUALS_DIR = Path.home() / ".researchkit-quals"

# Where assessment markdown files live (relative to this script)
SCRIPT_DIR = Path(__file__).resolve().parent
ASSESSMENTS_DIR = SCRIPT_DIR.parent / "assessments"

DOMAIN_NAMES = {
    "foundation": "Argument Construction",
    "domain-1": "Pattern Recognition & Data Sense",
    "domain-2": "Theoretical Positioning",
    "domain-3": "Qualitative Mechanism Extraction",
    "domain-4": "Theoretical Framing",
    "domain-5": "Epistemological Genre Awareness",
    "domain-6": "Adversarial Evidence Handling",
    "domain-7": "Claim Verification & Integrity",
}

DOMAIN_FILE_SLUGS = {
    "foundation": "level-1-foundation-argument-construction.md",
    "domain-1": "level-1-domain-1-pattern-recognition.md",
    "domain-2": "level-1-domain-2-theoretical-positioning.md",
    "domain-3": "level-1-domain-3-qualitative-mechanism.md",
    "domain-4": "level-1-domain-4-theoretical-framing.md",
    "domain-5": "level-1-domain-5-epistemological-genre.md",
    "domain-6": "level-1-domain-6-adversarial-evidence.md",
    "domain-7": "level-1-domain-7-claim-verification.md",
}

ALL_DOMAINS = ["domain-1", "domain-2", "domain-3", "domain-4",
               "domain-5", "domain-6", "domain-7"]

VALID_DOMAINS = ["foundation"] + ALL_DOMAINS

# Domains that cannot be advisor-certified
NO_CERTIFY_DOMAINS = {"domain-6", "domain-7"}

MAX_CERTIFICATIONS = 3

PASS_THRESHOLD = 0.80  # 80% for L1


# ---------------------------------------------------------------------------
# Student record helpers
# ---------------------------------------------------------------------------

def student_dir(student_id: str) -> Path:
    return QUALS_DIR / student_id


def record_path(student_id: str) -> Path:
    return student_dir(student_id) / "unlock-status.json"


def load_record(student_id: str) -> dict:
    path = record_path(student_id)
    if not path.exists():
        print(f"Error: No student record found for '{student_id}'.")
        print(f"  Expected: {path}")
        print()
        print("To create a record:")
        print(f"  python quals_cli.py init {student_id} --name \"Full Name\" --advisor \"Prof. Name\"")
        sys.exit(1)
    with open(path) as f:
        return json.load(f)


def save_record(student_id: str, record: dict) -> None:
    path = record_path(student_id)
    with open(path, "w") as f:
        json.dump(record, f, indent=2)


def resolve_student_id(student_id: str | None) -> str:
    """Resolve student ID from argument or stored default."""
    if student_id:
        return student_id
    default_file = QUALS_DIR / "student-id"
    if default_file.exists():
        sid = default_file.read_text().strip()
        if sid:
            return sid
    print("Error: No student ID provided and no default configured.")
    print()
    print("Provide a student ID:")
    print("  python quals_cli.py status <student-id>")
    print()
    print("Or set a default:")
    print(f"  echo \"jsmith\" > {QUALS_DIR / 'student-id'}")
    sys.exit(1)


def make_initial_record(student_id: str, name: str, advisor: str) -> dict:
    """Create a fresh student record with all domains available at L1."""
    record = {
        "student_id": student_id,
        "name": name,
        "advisor": advisor,
        "started": datetime.now().strftime("%Y-%m-%d"),
        "foundation": {
            "level-1": {"status": "available"},
            "level-2": {"status": "locked"},
            "level-3": {"status": "locked"},
        },
        "domains": {},
        "advisor_actions": [],
    }
    for d in ALL_DOMAINS:
        record["domains"][d] = {
            "level-1": {"status": "available"},
            "level-2": {"status": "locked"},
            "level-3": {"status": "locked"},
        }
    return record


def get_domain_data(record: dict, domain: str) -> dict:
    """Get the level data for a domain from the record."""
    if domain == "foundation":
        return record["foundation"]
    return record["domains"][domain]


def set_domain_data(record: dict, domain: str, data: dict) -> None:
    """Set the level data for a domain in the record."""
    if domain == "foundation":
        record["foundation"] = data
    else:
        record["domains"][domain] = data


# ---------------------------------------------------------------------------
# Assessment parsing
# ---------------------------------------------------------------------------

def parse_assessment(filepath: Path) -> dict:
    """Parse an L1 assessment markdown file into structured data.

    Returns:
        {
            "mc_questions": [
                {
                    "number": 1,
                    "text": "...",
                    "options": [("a", "..."), ("b", "..."), ...],
                },
                ...
            ],
            "short_answer_questions": [
                {
                    "number": 11,
                    "text": "...",
                    "model_answer": "...",
                },
                ...
            ],
            "answer_key": {1: "b", 2: "a", ...},  # MC answers only
            "scoring": {"mc_points": 10, "sa_points": 4, "total": 14, "pass": 11},
        }
    """
    text = filepath.read_text()

    # Parse answer key table
    answer_key = {}
    key_match = re.search(r"## Answer Key\s*\n(.*?)(?:\n\n|\n\*\*Scoring)", text, re.DOTALL)
    if key_match:
        for row in re.finditer(r"\|\s*(\d+)\s*\|\s*([^\|]+)\s*\|", key_match.group(1)):
            q_num = int(row.group(1))
            answer = row.group(2).strip()
            if answer.lower().startswith("see"):
                continue  # short answer
            answer_key[q_num] = answer.lower()

    # Parse scoring line
    scoring = {"mc_points": 10, "sa_points": 4, "total": 14, "pass": 11}
    score_section = re.search(r"\*\*Scoring\*\*:\s*\n(.*?)$", text, re.DOTALL)
    if score_section:
        total_m = re.search(r"Total:\s*(\d+)", score_section.group(1))
        pass_m = re.search(r"Pass:\s*[≥>=]*\s*(\d+)", score_section.group(1))
        # Format: "MC: 1 point each (10 points)" — grab the number in parens
        mc_m = re.search(r"MC:.*?\((\d+)\s*point", score_section.group(1))
        sa_m = re.search(r"Short answer:.*?\((\d+)\s*point", score_section.group(1))
        if total_m:
            scoring["total"] = int(total_m.group(1))
        if pass_m:
            scoring["pass"] = int(pass_m.group(1))
        if mc_m:
            scoring["mc_points"] = int(mc_m.group(1))
        if sa_m:
            scoring["sa_points"] = int(sa_m.group(1))

    # Parse questions
    # Split by ### Question N
    question_blocks = re.split(r"### Question (\d+)", text)
    # question_blocks: ['preamble', '1', 'content1', '2', 'content2', ...]

    mc_questions = []
    sa_questions = []

    i = 1
    while i < len(question_blocks):
        q_num = int(question_blocks[i])
        q_content = question_blocks[i + 1] if i + 1 < len(question_blocks) else ""
        i += 2

        # Stop at Answer Key
        if "## Answer Key" in q_content:
            q_content = q_content.split("## Answer Key")[0]

        # Check if it's short answer (has "short answer" in header or model answer)
        is_short_answer = (
            "short answer" in q_content.lower().split("\n")[0]
            or "model answer" in q_content.lower()
            or q_num not in answer_key
        )

        if is_short_answer:
            # Extract question text (before model answer section)
            parts = re.split(r"\*\*Model answer", q_content, flags=re.IGNORECASE)
            q_text = parts[0].strip()
            # Clean up header remnants
            q_text = re.sub(r"^\s*\(short answer\)\s*", "", q_text, flags=re.IGNORECASE).strip()
            # Remove leading ---
            q_text = re.sub(r"^---\s*", "", q_text).strip()

            model_answer = ""
            if len(parts) > 1:
                model_answer = parts[1].strip()
                # Clean up the model answer
                model_answer = re.sub(r"^[^:]*:\s*\n?", "", model_answer).strip()
                # Remove trailing ---
                model_answer = re.sub(r"\n---\s*$", "", model_answer).strip()

            sa_questions.append({
                "number": q_num,
                "text": q_text,
                "model_answer": model_answer,
            })
        else:
            # MC question - extract text and options
            # Remove **Correct** and **Why** sections
            clean = re.split(r"\n\*\*Correct\*\*:", q_content)[0]
            # Remove trailing ---
            clean = re.sub(r"\n---\s*$", "", clean).strip()

            # Extract options
            options = []
            for opt_match in re.finditer(r"- ([a-d])\)\s+(.*?)(?=\n- [a-d]\)|$)", clean, re.DOTALL):
                letter = opt_match.group(1)
                opt_text = opt_match.group(2).strip()
                options.append((letter, opt_text))

            # Question text is everything before the first option
            first_opt = re.search(r"\n- [a-d]\)", clean)
            q_text = clean[:first_opt.start()].strip() if first_opt else clean.strip()
            # Remove leading ---
            q_text = re.sub(r"^---\s*", "", q_text).strip()

            mc_questions.append({
                "number": q_num,
                "text": q_text,
                "options": options,
            })

    return {
        "mc_questions": mc_questions,
        "short_answer_questions": sa_questions,
        "answer_key": answer_key,
        "scoring": scoring,
    }


# ---------------------------------------------------------------------------
# Display helpers
# ---------------------------------------------------------------------------

def status_label(status: str, score: int | None = None, attempts: int | None = None) -> str:
    """Return a formatted status string with progress bar."""
    width = 20
    if status == "passed":
        bar = "\u2588" * width
        score_str = f" ({score}%)" if score is not None else ""
        return f"{bar} PASSED{score_str}"
    elif status == "in_progress":
        bar = "\u2588" * (width // 2) + "\u2591" * (width // 2)
        att_str = f" (attempt {attempts})" if attempts else ""
        return f"{bar} IN PROGRESS{att_str}"
    elif status == "available":
        bar = "\u2591" * width
        return f"{bar} AVAILABLE"
    else:  # locked
        bar = "\u2591" * width
        return f"{bar} LOCKED"


def print_box(text: str) -> None:
    """Print text inside a Unicode box."""
    lines = text.split("\n")
    max_len = max(len(line) for line in lines)
    width = max_len + 4
    print(f"\u250c{'\u2500' * width}\u2510")
    for line in lines:
        print(f"\u2502  {line:<{max_len}}  \u2502")
    print(f"\u2514{'\u2500' * width}\u2518")


# ---------------------------------------------------------------------------
# Commands
# ---------------------------------------------------------------------------

def cmd_init(args: argparse.Namespace) -> None:
    """Create a new student record."""
    sid = args.student_id
    name = args.name
    advisor = args.advisor

    sdir = student_dir(sid)
    if sdir.exists() and record_path(sid).exists():
        print(f"Error: Student record already exists for '{sid}'.")
        print(f"  Location: {record_path(sid)}")
        print()
        print("To view progress:")
        print(f"  python quals_cli.py status {sid}")
        sys.exit(1)

    sdir.mkdir(parents=True, exist_ok=True)

    record = make_initial_record(sid, name, advisor)
    save_record(sid, record)

    # Set as default student
    default_file = QUALS_DIR / "student-id"
    default_file.write_text(sid)

    print()
    print_box(f"ResearchKit Quals - Student Initialized")
    print()
    print(f"  Student ID:  {sid}")
    print(f"  Name:        {name}")
    print(f"  Advisor:     {advisor}")
    print(f"  Started:     {record['started']}")
    print(f"  Record:      {record_path(sid)}")
    print()
    print("  All domains unlocked at Level 1.")
    print("  Foundation (Argument Construction) also available.")
    print()
    print("  Next steps:")
    print(f"    python quals_cli.py status {sid}")
    print(f"    python quals_cli.py take foundation 1")
    print(f"    python quals_cli.py take domain-1 1")
    print()


def cmd_status(args: argparse.Namespace) -> None:
    """Display student competency progress."""
    sid = resolve_student_id(args.student_id)
    record = load_record(sid)

    print()
    print_box(f"ResearchKit Quals - Student: {record['name']}")
    print()
    print(f"  Student ID: {record['student_id']}    Advisor: {record['advisor']}    Started: {record['started']}")
    print()
    print("  COMPETENCY PROGRESS")
    print("  " + "\u2550" * 62)
    print()

    # Foundation
    _print_domain_progress("Foundation", "Argument Construction",
                           record.get("foundation", {}))
    print()

    # Domains
    for d in ALL_DOMAINS:
        num = d.split("-")[1]
        dname = DOMAIN_NAMES[d]
        ddata = record["domains"].get(d, {})
        _print_domain_progress(f"Domain {num}", dname, ddata)
        print()

    # Next steps
    print("  NEXT STEPS")
    print("  " + "\u2550" * 62)
    print()
    next_steps = _compute_next_steps(record)
    if next_steps:
        for step in next_steps:
            print(f"  \u2192 {step}")
    else:
        print("  All assessments completed!")
    print()

    # Advisor certifications
    actions = record.get("advisor_actions", [])
    certs = [a for a in actions if a.get("action") == "certified"]
    if certs:
        print("  ADVISOR CERTIFICATIONS")
        print("  " + "\u2550" * 62)
        print()
        for c in certs:
            domain_label = c.get("domain", "?")
            level = c.get("level", "?")
            advisor_id = c.get("advisor_id", c.get("advisor", "?"))
            date = c.get("date", "?")
            evidence = c.get("evidence", "")
            print(f"  \u2713 {domain_label} Level {level} - certified by {advisor_id} ({date})")
            if evidence:
                print(f"    Evidence: {evidence}")
        print()

    remaining_certs = MAX_CERTIFICATIONS - len(certs)
    if remaining_certs > 0:
        print(f"  Advisor certifications remaining: {remaining_certs}/{MAX_CERTIFICATIONS}")
        print(f"  (Domains 6-7 cannot be certified)")
        print()


def _print_domain_progress(prefix: str, name: str, data: dict) -> None:
    """Print progress for a single domain."""
    print(f"  {prefix}: {name}")
    levels = ["level-1", "level-2", "level-3"]
    for i, lvl in enumerate(levels):
        connector = "\u2514\u2500\u2500" if i == len(levels) - 1 else "\u251c\u2500\u2500"
        lvl_data = data.get(lvl, {"status": "locked"})
        status = lvl_data.get("status", "locked")
        score = lvl_data.get("score")
        attempts = lvl_data.get("attempts")
        label = status_label(status, score, attempts)
        lvl_name = f"Level {i + 1}"
        print(f"  {connector} {lvl_name}: {label}")


def _compute_next_steps(record: dict) -> list[str]:
    """Figure out actionable next steps for the student."""
    steps = []
    # Check foundation
    fdata = record.get("foundation", {})
    for lvl_key in ["level-1", "level-2", "level-3"]:
        lvl = fdata.get(lvl_key, {})
        if lvl.get("status") in ("available", "in_progress"):
            num = lvl_key.split("-")[1]
            action = "Complete" if lvl.get("status") == "in_progress" else "Take"
            steps.append(f"{action} Foundation Level {num} assessment")
            steps.append(f"  Run: python quals_cli.py take foundation {num}")
            break

    for d in ALL_DOMAINS:
        ddata = record["domains"].get(d, {})
        dnum = d.split("-")[1]
        for lvl_key in ["level-1", "level-2", "level-3"]:
            lvl = ddata.get(lvl_key, {})
            if lvl.get("status") in ("available", "in_progress"):
                num = lvl_key.split("-")[1]
                action = "Complete" if lvl.get("status") == "in_progress" else "Take"
                steps.append(f"{action} Domain {dnum} Level {num} assessment")
                if num == "1":
                    steps.append(f"  Run: python quals_cli.py take {d} {num}")
                break
    return steps


def cmd_take(args: argparse.Namespace) -> None:
    """Take an assessment."""
    domain = args.domain
    level = args.level
    sid = resolve_student_id(getattr(args, "student_id", None))
    record = load_record(sid)

    if domain not in VALID_DOMAINS:
        print(f"Error: Unknown domain '{domain}'.")
        print(f"Valid domains: {', '.join(VALID_DOMAINS)}")
        sys.exit(1)

    if level not in (1, 2, 3):
        print("Error: Level must be 1, 2, or 3.")
        sys.exit(1)

    # L2/L3 not yet implemented
    if level > 1:
        print(f"Level {level} assessments require materials. Contact your advisor.")
        sys.exit(0)

    # Check level availability
    domain_data = get_domain_data(record, domain)
    lvl_key = f"level-{level}"
    lvl_status = domain_data.get(lvl_key, {}).get("status", "locked")

    if lvl_status == "locked":
        print(f"Error: {DOMAIN_NAMES[domain]} Level {level} is locked.")
        if level > 1:
            print(f"  You must pass Level {level - 1} first.")
        sys.exit(1)

    if lvl_status == "passed":
        print(f"{DOMAIN_NAMES[domain]} Level {level} already passed.")
        score = domain_data.get(lvl_key, {}).get("score")
        if score is not None:
            print(f"  Score: {score}%")
        print()
        print("Retake anyway? (y/n): ", end="", flush=True)
        try:
            answer = input().strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\nCancelled.")
            sys.exit(0)
        if answer != "y":
            print("Cancelled.")
            sys.exit(0)

    # Load assessment
    assessment_file = ASSESSMENTS_DIR / DOMAIN_FILE_SLUGS.get(domain, "")
    if not assessment_file.exists():
        print(f"Error: Assessment file not found: {assessment_file}")
        print("This assessment may not have been created yet.")
        sys.exit(1)

    assessment = parse_assessment(assessment_file)
    mc_questions = assessment["mc_questions"]
    sa_questions = assessment["short_answer_questions"]
    answer_key = assessment["answer_key"]
    scoring = assessment["scoring"]

    # Mark as in-progress
    domain_data[lvl_key]["status"] = "in_progress"
    set_domain_data(record, domain, domain_data)
    save_record(sid, record)

    # Record start time
    start_time = datetime.now().isoformat()

    print()
    print_box(f"Level 1 Assessment: {DOMAIN_NAMES[domain]}")
    print()
    print(f"  Time limit: 30-45 minutes (not enforced)")
    print(f"  Passing: {scoring['pass']}/{scoring['total']} points (80%)")
    print(f"  MC questions: {len(mc_questions)} ({scoring['mc_points']} points)")
    print(f"  Short answer: {len(sa_questions)} ({scoring['sa_points']} points)")
    print()
    print("  Press Enter to begin...", end="", flush=True)
    try:
        input()
    except (EOFError, KeyboardInterrupt):
        print("\nCancelled.")
        sys.exit(0)

    # Randomize MC question order
    mc_order = list(range(len(mc_questions)))
    random.shuffle(mc_order)

    # Present MC questions
    mc_answers = {}
    print()
    print("  " + "\u2550" * 50)
    print("  MULTIPLE CHOICE")
    print("  " + "\u2550" * 50)
    print()

    for idx, q_idx in enumerate(mc_order):
        q = mc_questions[q_idx]
        q_num = q["number"]
        print(f"  Question {idx + 1} of {len(mc_questions)}")
        print(f"  {'─' * 48}")
        # Wrap question text
        for line in textwrap.wrap(q["text"], width=70):
            print(f"  {line}")
        print()
        for letter, opt_text in q["options"]:
            # Wrap long options
            wrapped = textwrap.wrap(opt_text, width=64)
            print(f"    {letter}) {wrapped[0]}")
            for extra_line in wrapped[1:]:
                print(f"       {extra_line}")
        print()

        while True:
            print("  Your answer (a/b/c/d): ", end="", flush=True)
            try:
                ans = input().strip().lower()
            except (EOFError, KeyboardInterrupt):
                print("\n\n  Assessment cancelled.")
                sys.exit(0)
            if ans in ("a", "b", "c", "d"):
                mc_answers[q_num] = ans
                break
            print("  Please enter a, b, c, or d.")
        print()

    # Present short answer questions
    sa_responses = {}
    if sa_questions:
        print("  " + "\u2550" * 50)
        print("  SHORT ANSWER")
        print("  " + "\u2550" * 50)
        print("  (Enter your response. Submit with a blank line.)")
        print()

        for q in sa_questions:
            q_num = q["number"]
            print(f"  Question {q_num}")
            print(f"  {'─' * 48}")
            for line in textwrap.wrap(q["text"], width=70):
                print(f"  {line}")
            print()
            print("  Your response (blank line to finish):")
            lines = []
            while True:
                try:
                    line = input("  > ")
                except (EOFError, KeyboardInterrupt):
                    print("\n\n  Assessment cancelled.")
                    sys.exit(0)
                if line.strip() == "":
                    break
                lines.append(line)
            sa_responses[q_num] = "\n".join(lines)
            print()

    # Score MC
    end_time = datetime.now().isoformat()
    mc_correct = 0
    mc_total = len(mc_questions)
    mc_results = {}
    for q_num, student_ans in mc_answers.items():
        correct_ans = answer_key.get(q_num, "")
        is_correct = student_ans == correct_ans
        mc_results[q_num] = {
            "student_answer": student_ans,
            "correct_answer": correct_ans,
            "correct": is_correct,
        }
        if is_correct:
            mc_correct += 1

    mc_score_pct = round(mc_correct / mc_total * 100) if mc_total > 0 else 0

    # Total score: MC portion only (SA needs manual grading)
    # Each MC question is 1 point, each SA is 2 points
    mc_points = mc_correct
    total_possible = scoring["total"]
    pass_threshold = scoring["pass"]

    # For passing purposes, count MC only since SA is pending review
    # But we need 80% overall -- so if they ace MC, they might still pass
    # We'll score MC and mark SA as pending
    sa_points_pending = scoring["sa_points"]
    auto_scored_total = mc_points  # out of mc_points possible
    max_possible_total = mc_points + sa_points_pending

    # Can they pass with MC alone?
    passed_mc_only = mc_points >= pass_threshold
    # Could they pass with perfect SA?
    can_pass = max_possible_total >= pass_threshold

    # Display results
    print()
    print("  " + "\u2550" * 50)
    print("  RESULTS")
    print("  " + "\u2550" * 50)
    print()
    print(f"  Multiple Choice: {mc_correct}/{mc_total} correct")
    print()

    # Show per-question results
    for q_idx in mc_order:
        q = mc_questions[q_idx]
        q_num = q["number"]
        result = mc_results.get(q_num, {})
        mark = "\u2713" if result.get("correct") else "\u2717"
        student = result.get("student_answer", "?")
        correct = result.get("correct_answer", "?")
        if result.get("correct"):
            print(f"    {mark} Q{q_num}: {student}")
        else:
            print(f"    {mark} Q{q_num}: {student} (correct: {correct})")

    print()
    if sa_questions:
        print(f"  Short answer: {len(sa_responses)} response(s) saved for manual review")
        print(f"    (worth {sa_points_pending} points)")
        print()

    print(f"  MC Score: {mc_points}/{scoring['mc_points']} points")
    print()

    if passed_mc_only:
        print(f"  PASSED (MC alone meets threshold of {pass_threshold}/{total_possible})")
        final_status = "passed"
    elif not can_pass:
        print(f"  NOT PASSED (even with perfect short answers, max = {max_possible_total}/{total_possible}, need {pass_threshold})")
        final_status = "available"  # can retry
    else:
        print(f"  PENDING short answer review (MC: {mc_points}, need {pass_threshold}/{total_possible})")
        print(f"  With perfect short answers, total could be {max_possible_total}/{total_possible}")
        final_status = "in_progress"

    print()

    # Build attempt record
    attempts = domain_data[lvl_key].get("attempts", 0) + 1
    attempt_record = {
        "attempt": attempts,
        "start_time": start_time,
        "end_time": end_time,
        "mc_correct": mc_correct,
        "mc_total": mc_total,
        "mc_points": mc_points,
        "mc_results": mc_results,
        "sa_responses": {str(k): v for k, v in sa_responses.items()},
        "sa_pending_review": bool(sa_questions),
    }

    # Update record
    domain_data[lvl_key]["status"] = final_status
    domain_data[lvl_key]["attempts"] = attempts
    domain_data[lvl_key]["last_attempt"] = end_time
    domain_data[lvl_key]["mc_score"] = mc_correct
    domain_data[lvl_key]["mc_total"] = mc_total

    if final_status == "passed":
        domain_data[lvl_key]["score"] = mc_score_pct
        domain_data[lvl_key]["passed_at"] = datetime.now().strftime("%Y-%m-%d")
        # Unlock next level
        next_level = level + 1
        if next_level <= 3:
            next_key = f"level-{next_level}"
            if domain_data.get(next_key, {}).get("status") == "locked":
                domain_data[next_key]["status"] = "available"
                print(f"  Level {next_level} unlocked!")
                print()

    # Save attempt details separately
    attempts_dir = student_dir(record["student_id"]) / "attempts"
    attempts_dir.mkdir(exist_ok=True)
    attempt_file = attempts_dir / f"{domain}-level-{level}-attempt-{attempts}.json"
    with open(attempt_file, "w") as f:
        json.dump(attempt_record, f, indent=2)

    set_domain_data(record, domain, domain_data)
    save_record(record["student_id"], record)

    print(f"  Attempt saved to: {attempt_file}")
    print()


def cmd_certify(args: argparse.Namespace) -> None:
    """Advisor certification bypass."""
    sid = args.student_id
    domain = args.domain
    level = args.level
    advisor_id = args.advisor
    evidence = args.evidence

    record = load_record(sid)

    if domain not in VALID_DOMAINS:
        print(f"Error: Unknown domain '{domain}'.")
        print(f"Valid domains: {', '.join(VALID_DOMAINS)}")
        sys.exit(1)

    if level not in (1, 2, 3):
        print("Error: Level must be 1, 2, or 3.")
        sys.exit(1)

    # Check domain restrictions
    if domain in NO_CERTIFY_DOMAINS:
        print(f"Error: {DOMAIN_NAMES[domain]} cannot be certified by advisor.")
        print("Students must demonstrate adversarial/verification skills through assessment.")
        sys.exit(1)

    # Check certification limit
    existing_certs = [a for a in record.get("advisor_actions", [])
                      if a.get("action") == "certified"]
    if len(existing_certs) >= MAX_CERTIFICATIONS:
        print(f"Error: Maximum {MAX_CERTIFICATIONS} advisor certifications per student.")
        print(f"Already certified:")
        for c in existing_certs:
            print(f"  - {c.get('domain')} Level {c.get('level')}")
        sys.exit(1)

    # Apply certification
    domain_data = get_domain_data(record, domain)
    lvl_key = f"level-{level}"

    # Mark as passed
    domain_data[lvl_key] = {
        "status": "passed",
        "score": None,
        "passed_at": datetime.now().strftime("%Y-%m-%d"),
        "certified_by": advisor_id,
        "attempts": 0,
    }

    # Unlock next level
    next_level = level + 1
    if next_level <= 3:
        next_key = f"level-{next_level}"
        if domain_data.get(next_key, {}).get("status") == "locked":
            domain_data[next_key] = {"status": "available"}

    # Also certify all lower levels if not already passed
    for l in range(1, level):
        lower_key = f"level-{l}"
        if domain_data.get(lower_key, {}).get("status") != "passed":
            domain_data[lower_key] = {
                "status": "passed",
                "score": None,
                "passed_at": datetime.now().strftime("%Y-%m-%d"),
                "certified_by": advisor_id,
                "attempts": 0,
            }

    set_domain_data(record, domain, domain_data)

    # Log advisor action
    action_record = {
        "type": "advisor_certification",
        "action": "certified",
        "domain": domain,
        "level": level,
        "advisor": record.get("advisor", ""),
        "advisor_id": advisor_id,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "evidence": evidence,
        "attestation_signed": True,
    }
    record["advisor_actions"].append(action_record)
    save_record(sid, record)

    print()
    print_box(f"Advisor Certification Recorded")
    print()
    print(f"  Student:  {record['name']} ({sid})")
    print(f"  Domain:   {DOMAIN_NAMES[domain]}")
    print(f"  Level:    {level}")
    print(f"  Advisor:  {advisor_id}")
    print(f"  Evidence: {evidence}")
    print(f"  Date:     {action_record['date']}")
    print()
    remaining = MAX_CERTIFICATIONS - len(existing_certs) - 1
    print(f"  Certifications remaining: {remaining}/{MAX_CERTIFICATIONS}")
    print()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        prog="quals",
        description="ResearchKit Quals - PhD competency assessment system",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent("""\
            Examples:
              quals init jsmith --name "Jane Smith" --advisor "Prof. Beane"
              quals status jsmith
              quals take domain-1 1
              quals certify jsmith domain-3 2 --advisor mbeane --evidence "Stanford TM 502, A grade"
        """),
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # init
    p_init = subparsers.add_parser("init", help="Create a new student record")
    p_init.add_argument("student_id", help="Unique student identifier (e.g., jsmith)")
    p_init.add_argument("--name", required=True, help="Student's full name")
    p_init.add_argument("--advisor", required=True, help="Advisor name")

    # status
    p_status = subparsers.add_parser("status", help="Show competency progress")
    p_status.add_argument("student_id", nargs="?", default=None,
                          help="Student ID (reads from ~/.researchkit-quals/student-id if omitted)")

    # take
    p_take = subparsers.add_parser("take", help="Take a Level 1 assessment")
    p_take.add_argument("domain", help="Domain to assess (foundation, domain-1 through domain-7)")
    p_take.add_argument("level", type=int, help="Level (1, 2, or 3)")
    p_take.add_argument("--student-id", dest="student_id", default=None,
                        help="Student ID (reads from default if omitted)")

    # certify
    p_certify = subparsers.add_parser("certify", help="Advisor certification bypass")
    p_certify.add_argument("student_id", help="Student ID")
    p_certify.add_argument("domain", help="Domain to certify")
    p_certify.add_argument("level", type=int, help="Level to certify (1, 2, or 3)")
    p_certify.add_argument("--advisor", required=True, help="Advisor ID")
    p_certify.add_argument("--evidence", required=True, help="Evidence description")

    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        sys.exit(1)

    commands = {
        "init": cmd_init,
        "status": cmd_status,
        "take": cmd_take,
        "certify": cmd_certify,
    }

    commands[args.command](args)


if __name__ == "__main__":
    main()
