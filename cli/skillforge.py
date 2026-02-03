#!/usr/bin/env python3
"""
SkillForge CLI - Competency-based training for mixed-methods management research

Commands:
    status      Show your current competency status
    take        Take a Level 1 assessment
    submit      Submit Level 2-3 work for evaluation
    init        Initialize student profile
"""

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional

# Configuration
SKILLFORGE_HOME = Path.home() / ".skillforge"
ASSESSMENTS_DIR = Path(__file__).parent.parent / "assessments"

DOMAINS = {
    "domain-1": "Pattern Recognition",
    "domain-2": "Theoretical Positioning",
    "domain-3": "Qualitative Mechanism",
    "domain-4": "Theoretical Framing",
    "domain-5": "Epistemological Genre",
    "domain-6": "Adversarial Evidence",
    "domain-7": "Claim Verification",
}

DOMAIN_QUESTIONS = {
    "domain-1": "Is this signal or noise?",
    "domain-2": "What makes this a contribution?",
    "domain-3": "What's actually happening here?",
    "domain-4": "How do I position this for reviewers?",
    "domain-5": "Am I discovering or testing?",
    "domain-6": "What challenges my interpretation?",
    "domain-7": "Does my evidence support my claims?",
}

# Progression rules
LEVEL_PREREQS = {
    # level 2 requires level 1 in same domain
    # level 3 requires level 2 in same domain
}

DOMAIN_PREREQS = {
    # Some domains require others first
    "domain-2": ["domain-1"],
    "domain-4": ["domain-3"],
    "domain-5": ["domain-4"],
    "domain-6": ["domain-5"],
    "domain-7": ["domain-6"],
}


def get_student_record() -> dict:
    """Load or create student record."""
    record_path = SKILLFORGE_HOME / "record.json"
    if record_path.exists():
        return json.loads(record_path.read_text())
    return {
        "student_id": None,
        "created": None,
        "domains": {},
        "attempts": [],
    }


def save_student_record(record: dict):
    """Save student record."""
    SKILLFORGE_HOME.mkdir(parents=True, exist_ok=True)
    record_path = SKILLFORGE_HOME / "record.json"
    record_path.write_text(json.dumps(record, indent=2))


def cmd_init(args):
    """Initialize student profile."""
    record = get_student_record()

    if record["student_id"]:
        print(f"Already initialized as: {record['student_id']}")
        if not args.force:
            print("Use --force to reinitialize (warning: clears progress)")
            return 1
        print("Reinitializing...")
        record = {"domains": {}, "attempts": []}

    # Get student info
    if args.name:
        name = args.name
    else:
        name = input("Your name: ").strip()

    if args.email:
        email = args.email
    else:
        email = input("Your email: ").strip()

    record["student_id"] = email.split("@")[0]
    record["name"] = name
    record["email"] = email
    record["created"] = datetime.now().isoformat()
    record["domains"] = {d: {"level": 0, "attempts": []} for d in DOMAINS}
    record["attempts"] = []

    save_student_record(record)
    print(f"\n✅ Initialized SkillForge profile for {name}")
    print(f"   Student ID: {record['student_id']}")
    print(f"\nRun 'skillforge status' to see your competency map.")
    return 0


def cmd_status(args):
    """Show competency status."""
    record = get_student_record()

    if not record["student_id"]:
        print("Not initialized. Run 'skillforge init' first.")
        return 1

    print(f"\n🎓 SkillForge Status: {record.get('name', record['student_id'])}")
    print("=" * 60)

    # Summary stats
    total_l3 = sum(1 for d in record.get("domains", {}).values() if d.get("level", 0) >= 3)
    print(f"\nLevel 3 Competencies: {total_l3}/7")

    # Domain breakdown
    print("\n" + "-" * 60)
    print(f"{'Domain':<35} {'Level':<10} {'Status':<15}")
    print("-" * 60)

    for domain_id, domain_name in DOMAINS.items():
        domain_data = record.get("domains", {}).get(domain_id, {})
        level = domain_data.get("level", 0)

        # Status indicator
        if level >= 3:
            status = "✅ Complete"
            level_str = "L3"
        elif level >= 2:
            status = "🔶 L3 available"
            level_str = "L2"
        elif level >= 1:
            status = "🔶 L2 available"
            level_str = "L1"
        else:
            # Check prereqs
            prereqs = DOMAIN_PREREQS.get(domain_id, [])
            prereqs_met = all(
                record.get("domains", {}).get(p, {}).get("level", 0) >= 1
                for p in prereqs
            )
            if prereqs_met:
                status = "⚪ L1 available"
            else:
                status = f"🔒 Requires {', '.join(prereqs)}"
            level_str = "--"

        question = DOMAIN_QUESTIONS[domain_id]
        print(f"{domain_id}: {domain_name:<24} {level_str:<10} {status}")

    print("-" * 60)

    # Next steps
    print("\n📋 Next Steps:")
    suggested = False
    for domain_id in DOMAINS:
        domain_data = record.get("domains", {}).get(domain_id, {})
        level = domain_data.get("level", 0)
        prereqs = DOMAIN_PREREQS.get(domain_id, [])
        prereqs_met = all(
            record.get("domains", {}).get(p, {}).get("level", 0) >= 1
            for p in prereqs
        )

        if level < 3 and prereqs_met:
            next_level = level + 1
            if next_level == 1:
                print(f"   skillforge take {domain_id} --level 1")
            elif next_level == 2:
                print(f"   skillforge take {domain_id} --level 2")
            else:
                print(f"   skillforge submit {domain_id} --level 3")
            suggested = True
            if suggested and level == 0:
                break  # Only show first available domain for beginners

    if not suggested:
        print("   🎉 All domains complete! You're ready for independent research.")

    print()
    return 0


def load_assessment(domain: str, level: int) -> Optional[dict]:
    """Load assessment questions from markdown file."""
    # Map level 1 files
    level_1_files = {
        "domain-1": "level-1-domain-1-pattern-recognition.md",
        "domain-3": "level-1-domain-3-qualitative-mechanism.md",
        "domain-7": "level-1-domain-7-claim-verification.md",
    }

    if level == 1 and domain in level_1_files:
        file_path = ASSESSMENTS_DIR / level_1_files[domain]
        if file_path.exists():
            return parse_assessment_md(file_path)

    return None


def parse_assessment_md(file_path: Path) -> dict:
    """Parse assessment markdown into structured questions."""
    content = file_path.read_text()

    questions = []
    current_q = None
    in_options = False
    correct_answer = None
    why_text = None
    model_answer = []
    in_model_answer = False

    lines = content.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i]

        # Start of new question
        if line.startswith("### Question "):
            if current_q:
                # Save previous question
                if current_q.get("type") == "mc":
                    current_q["correct"] = correct_answer
                    current_q["explanation"] = why_text
                elif current_q.get("type") == "short":
                    current_q["model_answer"] = "\n".join(model_answer)
                questions.append(current_q)

            q_num = int(line.replace("### Question ", "").strip())
            # Read next line for question text
            i += 1
            q_text = ""
            while i < len(lines) and not lines[i].startswith("- ") and not lines[i].startswith("**"):
                if lines[i].strip():
                    q_text += lines[i] + " "
                i += 1

            current_q = {
                "number": q_num,
                "question": q_text.strip(),
                "options": [],
                "type": "mc",  # default, will change if short answer
            }
            correct_answer = None
            why_text = None
            model_answer = []
            in_model_answer = False
            in_options = True
            continue

        # Options for MC
        if in_options and line.startswith("- "):
            option = line[2:].strip()
            # Parse "a) text" format
            if len(option) >= 3 and option[1] == ")":
                letter = option[0].lower()
                text = option[3:].strip()
                current_q["options"].append({"letter": letter, "text": text})

        # Correct answer
        if line.startswith("**Correct**:"):
            correct_answer = line.replace("**Correct**:", "").strip().lower()
            in_options = False

        # Explanation
        if line.startswith("**Why**:"):
            why_text = line.replace("**Why**:", "").strip()

        # Short answer detection
        if "**Model answer should include**:" in line or "**Model answer should include any" in line:
            current_q["type"] = "short"
            in_model_answer = True
            in_options = False

        # Collect model answer bullets
        if in_model_answer and line.startswith("- "):
            model_answer.append(line[2:].strip())

        i += 1

    # Don't forget last question
    if current_q:
        if current_q.get("type") == "mc":
            current_q["correct"] = correct_answer
            current_q["explanation"] = why_text
        elif current_q.get("type") == "short":
            current_q["model_answer"] = "\n".join(model_answer)
        questions.append(current_q)

    # Extract metadata
    time_limit = "30-45 minutes"
    passing = "80%"

    for line in lines[:30]:
        if "**Time**:" in line:
            time_limit = line.split("**Time**:")[1].strip()
        if "**Passing**:" in line:
            passing = line.split("**Passing**:")[1].strip()

    return {
        "file": str(file_path),
        "time_limit": time_limit,
        "passing": passing,
        "questions": questions,
    }


def run_level1_assessment(assessment: dict, domain: str) -> tuple[int, int, list]:
    """Run interactive Level 1 assessment. Returns (score, total, responses)."""
    questions = assessment["questions"]
    mc_questions = [q for q in questions if q["type"] == "mc"]
    short_questions = [q for q in questions if q["type"] == "short"]

    print(f"\n📝 Level 1 Assessment: {DOMAINS[domain]}")
    print("=" * 60)
    print(f"Time: {assessment['time_limit']}")
    print(f"Passing: {assessment['passing']}")
    print(f"Questions: {len(mc_questions)} multiple choice + {len(short_questions)} short answer")
    print("=" * 60)

    input("\nPress Enter to begin...")

    responses = []
    mc_correct = 0

    # Multiple choice section
    print("\n--- Section A: Multiple Choice ---\n")

    for q in mc_questions:
        print(f"\nQuestion {q['number']}:")
        print(q["question"])
        print()
        for opt in q["options"]:
            print(f"  {opt['letter']}) {opt['text']}")

        while True:
            answer = input("\nYour answer (a/b/c/d): ").strip().lower()
            if answer in ["a", "b", "c", "d"]:
                break
            print("Please enter a, b, c, or d")

        is_correct = answer == q["correct"]
        if is_correct:
            mc_correct += 1

        responses.append({
            "question": q["number"],
            "type": "mc",
            "answer": answer,
            "correct": q["correct"],
            "is_correct": is_correct,
        })

    # Short answer section
    print("\n--- Section B: Short Answer ---\n")

    for q in short_questions:
        print(f"\nQuestion {q['number']}:")
        print(q["question"])
        print("\n(Type your answer, then press Enter twice to submit)")

        lines = []
        while True:
            line = input()
            if line == "" and lines and lines[-1] == "":
                break
            lines.append(line)

        answer = "\n".join(lines[:-1] if lines and lines[-1] == "" else lines)

        responses.append({
            "question": q["number"],
            "type": "short",
            "answer": answer,
            "model_answer": q.get("model_answer", ""),
        })

    # Calculate score
    mc_total = len(mc_questions)
    short_total = len(short_questions) * 2  # 2 points each

    print("\n" + "=" * 60)
    print("Assessment Complete!")
    print("=" * 60)

    # Show MC results immediately
    print(f"\nMultiple Choice: {mc_correct}/{mc_total}")

    # Short answers need review
    print(f"\nShort Answer: Pending review ({len(short_questions)} questions, {short_total} points)")

    # For now, assume short answers get full credit (self-assessment)
    print("\nFor Level 1, short answers are self-assessed.")
    print("Compare your answers to the model answers:\n")

    short_score = 0
    for resp in responses:
        if resp["type"] == "short":
            print(f"Question {resp['question']}:")
            print(f"Your answer: {resp['answer'][:200]}..." if len(resp["answer"]) > 200 else f"Your answer: {resp['answer']}")
            print(f"\nModel answer should include:")
            for line in resp["model_answer"].split("\n"):
                print(f"  • {line}")

            while True:
                self_score = input("\nHow many points? (0/1/2): ").strip()
                if self_score in ["0", "1", "2"]:
                    short_score += int(self_score)
                    resp["self_score"] = int(self_score)
                    break
            print()

    total_score = mc_correct + short_score
    total_possible = mc_total + short_total
    percentage = (total_score / total_possible) * 100

    return total_score, total_possible, responses, percentage


def cmd_take(args):
    """Take an assessment."""
    record = get_student_record()

    if not record["student_id"]:
        print("Not initialized. Run 'skillforge init' first.")
        return 1

    domain = args.domain
    level = args.level

    # Validate domain
    if domain not in DOMAINS:
        print(f"Unknown domain: {domain}")
        print(f"Valid domains: {', '.join(DOMAINS.keys())}")
        return 1

    # Check prerequisites
    prereqs = DOMAIN_PREREQS.get(domain, [])
    for prereq in prereqs:
        prereq_level = record.get("domains", {}).get(prereq, {}).get("level", 0)
        if prereq_level < 1:
            print(f"🔒 {domain} requires {prereq} Level 1 first.")
            print(f"   Run: skillforge take {prereq} --level 1")
            return 1

    current_level = record.get("domains", {}).get(domain, {}).get("level", 0)
    if level > current_level + 1:
        print(f"🔒 You must pass Level {current_level + 1} before Level {level}")
        return 1

    # Load assessment
    assessment = load_assessment(domain, level)
    if not assessment:
        print(f"❌ No assessment available for {domain} Level {level}")
        print("   Available assessments: domain-1, domain-3, domain-7 (Level 1 only)")
        return 1

    # Run the assessment
    if level == 1:
        score, total, responses, percentage = run_level1_assessment(assessment, domain)

        passed = percentage >= 80

        print("\n" + "=" * 60)
        print(f"Final Score: {score}/{total} ({percentage:.0f}%)")
        print(f"Required: 80%")

        if passed:
            print("\n✅ PASSED!")
            # Update record
            if domain not in record["domains"]:
                record["domains"][domain] = {"level": 0, "attempts": []}
            record["domains"][domain]["level"] = max(record["domains"][domain]["level"], 1)
            record["domains"][domain]["attempts"].append({
                "level": 1,
                "date": datetime.now().isoformat(),
                "score": score,
                "total": total,
                "percentage": percentage,
                "passed": True,
            })
            save_student_record(record)
            print(f"\n{DOMAINS[domain]} Level 1 complete!")
            print(f"Run 'skillforge status' to see your updated progress.")
        else:
            print("\n❌ Not yet. Review the material and try again.")
            record["attempts"].append({
                "domain": domain,
                "level": 1,
                "date": datetime.now().isoformat(),
                "score": score,
                "total": total,
                "percentage": percentage,
                "passed": False,
            })
            save_student_record(record)
    else:
        print(f"Level {level} assessments require file submission.")
        print(f"Run: skillforge submit {domain} --level {level} --file your_work.md")

    return 0


def cmd_submit(args):
    """Submit work for Level 2-3 evaluation."""
    record = get_student_record()

    if not record["student_id"]:
        print("Not initialized. Run 'skillforge init' first.")
        return 1

    domain = args.domain
    level = args.level
    file_path = Path(args.file)

    if not file_path.exists():
        print(f"File not found: {file_path}")
        return 1

    # Check prerequisites
    current_level = record.get("domains", {}).get(domain, {}).get("level", 0)
    if level > current_level + 1:
        print(f"🔒 You must pass Level {current_level + 1} before Level {level}")
        return 1

    # For now, just log the submission
    submission = {
        "domain": domain,
        "level": level,
        "file": str(file_path),
        "date": datetime.now().isoformat(),
        "status": "pending_review",
    }

    # Save submission
    submissions_dir = SKILLFORGE_HOME / "submissions"
    submissions_dir.mkdir(parents=True, exist_ok=True)

    submission_id = f"{domain}-L{level}-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
    submission_path = submissions_dir / f"{submission_id}.json"
    submission_path.write_text(json.dumps(submission, indent=2))

    # Copy submitted file
    import shutil
    submitted_file = submissions_dir / f"{submission_id}-work{file_path.suffix}"
    shutil.copy(file_path, submitted_file)

    print(f"\n📤 Submission received!")
    print(f"   Domain: {DOMAINS[domain]}")
    print(f"   Level: {level}")
    print(f"   Submission ID: {submission_id}")
    print(f"\nYour work will be evaluated against the expert baseline.")
    print("You'll receive feedback when evaluation is complete.")

    return 0


def main():
    parser = argparse.ArgumentParser(
        description="SkillForge - Competency-based training for mixed-methods research",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    skillforge init                     Initialize your profile
    skillforge status                   See your competency map
    skillforge take domain-1 --level 1  Take Pattern Recognition L1
    skillforge submit domain-3 --level 2 --file my-coding.md
        """
    )

    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    # init
    init_parser = subparsers.add_parser("init", help="Initialize student profile")
    init_parser.add_argument("--name", help="Your name")
    init_parser.add_argument("--email", help="Your email")
    init_parser.add_argument("--force", action="store_true", help="Reinitialize (clears progress)")

    # status
    status_parser = subparsers.add_parser("status", help="Show competency status")

    # take
    take_parser = subparsers.add_parser("take", help="Take an assessment")
    take_parser.add_argument("domain", help="Domain to assess (e.g., domain-1)")
    take_parser.add_argument("--level", "-l", type=int, default=1, help="Level (1, 2, or 3)")

    # submit
    submit_parser = subparsers.add_parser("submit", help="Submit work for evaluation")
    submit_parser.add_argument("domain", help="Domain (e.g., domain-3)")
    submit_parser.add_argument("--level", "-l", type=int, required=True, help="Level (2 or 3)")
    submit_parser.add_argument("--file", "-f", required=True, help="File to submit")

    args = parser.parse_args()

    if args.command == "init":
        return cmd_init(args)
    elif args.command == "status":
        return cmd_status(args)
    elif args.command == "take":
        return cmd_take(args)
    elif args.command == "submit":
        return cmd_submit(args)
    else:
        parser.print_help()
        return 0


if __name__ == "__main__":
    sys.exit(main())
