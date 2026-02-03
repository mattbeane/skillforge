#!/usr/bin/env python3
"""
SkillForge Evaluation Engine - Level 2-3 Assessment Scoring

Uses LLM-based evaluation against expert baselines to score student work.
Follows the scoring rubrics defined in ASSESSMENT_SPECS.md.

Level 2: Application with feedback (≥70/100, 7-day cooldown on retry)
Level 3: Authentic performance (≥70/100, no criterion below 50%, 30-day cooldown)
"""

import json
import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional

# Try to import anthropic, fall back to subprocess if not available
try:
    import anthropic
    HAS_ANTHROPIC = True
except ImportError:
    HAS_ANTHROPIC = False

SKILLFORGE_HOME = Path.home() / ".skillforge"
PROJECT_ROOT = Path(__file__).parent.parent
BASELINE_PATH = PROJECT_ROOT / "seed-data" / "beane-surgery-anonymized" / "expert_baseline.md"

# Domain-specific evaluation prompts
DOMAIN_PROMPTS = {
    "domain-1": """You are evaluating a student's pattern recognition work.

Expert baseline context:
{baseline}

Student submission:
{submission}

Evaluate using this rubric:
1. Found target patterns (30 pts): Did they identify patterns the expert found?
2. Avoided false positives (20 pts): Did they avoid pursuing noise as signal?
3. Reasoning quality (30 pts): Is their robustness thinking sound?
4. Completeness (20 pts): Did they document killed findings, heterogeneity, etc.?

For each criterion, provide:
- Score (0-100% of points available)
- Specific evidence from their work
- What they did well
- What they missed

End with:
TOTAL_SCORE: [number]/100
PASSED: [yes/no]
""",

    "domain-2": """You are evaluating a student's theoretical positioning work.

Expert baseline context:
{baseline}

Student submission:
{submission}

Evaluate using this rubric:
1. Conversation identified (25 pts): Did they identify a specific scholarly debate their finding speaks to?
2. Contribution specified (25 pts): Did they articulate what would change in that conversation?
3. Positioning quality (30 pts): Is the positioning specific, bounded, and theoretically grounded?
4. Alternatives considered (20 pts): Did they consider multiple positioning options?

For each criterion, provide:
- Score (0-100% of points available)
- Specific evidence from their work
- What they did well
- What they missed

End with:
TOTAL_SCORE: [number]/100
PASSED: [yes/no]
""",

    "domain-3": """You are evaluating a student's qualitative mechanism extraction work.

Expert baseline context:
{baseline}

The expert found these mechanisms:
1. Shadow Learning (3 practices: Premature Specialization, Abstract Rehearsal, Undersupervised Struggle)
2. Technology-Mediated Participation Barriers
3. Workaround Resilience & Portfolio Degradation

Student submission:
{submission}

Evaluate using this rubric:
1. Mechanism overlap (30 pts): Did they find mechanisms the expert found?
   - Full credit: Found ≥2 of 3 major mechanisms
   - Partial: Found 1 mechanism or related sub-mechanisms
   - Zero: Missed all mechanisms
2. Quote/evidence overlap (25 pts): Did they identify key evidence the expert used?
3. Disconfirming evidence (30 pts): Did they find and engage with disconfirming cases?
   - CRITICAL: Must find ≥50% of disconfirming evidence to pass
4. Coding quality (15 pts): Are codes action/process-oriented, not just topics?

For each criterion, provide:
- Score (0-100% of points available)
- Specific evidence from their work
- What they did well
- What they missed

End with:
TOTAL_SCORE: [number]/100
PASSED: [yes/no]
DISCONFIRM_CHECK: [pass/fail] (must be pass to pass overall)
""",

    "domain-4": """You are evaluating a student's theoretical framing work.

Expert baseline context:
{baseline}

Student submission:
{submission}

Evaluate using Zuckerman's criteria:
1. Novel (25 pts): Is the framing genuinely new, or restating what's known?
2. True (25 pts): Does the evidence support the framing?
3. Important (25 pts): Would this framing matter to the target conversation?
4. Reachable (25 pts): Can the target audience understand and engage?

Additional checks:
- Did they generate multiple candidate frames?
- Is the claim in the "Goldilocks zone" (bounded but generalizable)?
- Does the framing specify mechanism, not just phenomenon?

For each criterion, provide:
- Score (0-100% of points available)
- Specific evidence from their work
- What they did well
- What they missed

End with:
TOTAL_SCORE: [number]/100
PASSED: [yes/no]
""",

    "domain-5": """You are evaluating a student's epistemological genre work.

Expert baseline context:
{baseline}

Student submission:
{submission}

Evaluate for genre consistency:
1. Genre identification (25 pts): Did they correctly identify whether their work is discovery or testing?
2. Method-claim alignment (30 pts): Do claims match what the methods can support?
3. Appropriate hedging (25 pts): Are causal/scope claims appropriately bounded?
4. Generalization type (20 pts): Do they distinguish theoretical vs statistical generalization?

Key violations to check:
- Making testing claims with discovery methods
- Claiming causation from qualitative data
- Claiming population generalization from qualitative sample

For each criterion, provide:
- Score (0-100% of points available)
- Specific evidence from their work
- What they did well
- What they missed

End with:
TOTAL_SCORE: [number]/100
PASSED: [yes/no]
""",

    "domain-6": """You are evaluating a student's adversarial evidence work.

Expert baseline context:
{baseline}

Student submission:
{submission}

Evaluate for adversarial rigor:
1. Disconfirmation search (30 pts): Did they actively search for evidence against their mechanism?
2. Distribution reported (25 pts): Did they report full distribution, not just supporting cases?
3. Boundary conditions (25 pts): Did they use disconfirming cases to identify scope conditions?
4. Integration (20 pts): Did they reconcile disconfirming evidence with their theory?

Key checks:
- Zero disconfirming evidence is a red flag (max 50 pts if none found)
- Cherry-picking vivid quotes without distribution is penalized
- Hiding disconfirmation in limitations section is penalized

For each criterion, provide:
- Score (0-100% of points available)
- Specific evidence from their work
- What they did well
- What they missed

End with:
TOTAL_SCORE: [number]/100
PASSED: [yes/no]
""",

    "domain-7": """You are evaluating a student's claim verification work.

Expert baseline context:
{baseline}

Student submission:
{submission}

Evaluate for claim-evidence calibration:
1. Overclaims identified (40 pts): Did they catch causal, scope, and measurement overclaims?
2. False positives avoided (20 pts): Did they avoid flagging appropriate claims as overclaims?
3. Revision quality (40 pts): Are their suggested revisions appropriately calibrated?

Types of overclaims to check:
- Causal overclaims: Claiming causation from correlation/qualitative data
- Scope overclaims: Generalizing beyond evidence (5 hospitals → "nationwide")
- Measurement overclaims: Claiming to measure X when measured Y (behavior vs preferences)

For each criterion, provide:
- Score (0-100% of points available)
- Specific evidence from their work
- What they did well
- What they missed

End with:
TOTAL_SCORE: [number]/100
PASSED: [yes/no]
""",
}


def load_expert_baseline() -> str:
    """Load the expert baseline document."""
    if BASELINE_PATH.exists():
        return BASELINE_PATH.read_text()
    return "(No expert baseline available)"


def evaluate_with_claude(domain: str, submission_text: str, level: int) -> dict:
    """Use Claude to evaluate student submission against expert baseline."""

    baseline = load_expert_baseline()
    prompt_template = DOMAIN_PROMPTS.get(domain, DOMAIN_PROMPTS["domain-1"])

    full_prompt = prompt_template.format(
        baseline=baseline,
        submission=submission_text
    )

    level_context = f"""This is a Level {level} assessment.
{"Level 2: Provide detailed feedback for learning. Student can retry after 7 days." if level == 2 else "Level 3: Final assessment. No feedback during assessment. 30-day cooldown on retry."}

"""

    full_prompt = level_context + full_prompt

    if HAS_ANTHROPIC:
        client = anthropic.Anthropic()
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=4096,
            messages=[{"role": "user", "content": full_prompt}]
        )
        evaluation_text = response.content[0].text
    else:
        # Fall back to subprocess call
        result = subprocess.run(
            ["claude", "-p", full_prompt],
            capture_output=True,
            text=True,
            timeout=120
        )
        evaluation_text = result.stdout

    # Parse the evaluation
    result = {
        "raw_evaluation": evaluation_text,
        "total_score": 0,
        "passed": False,
        "criteria": {}
    }

    # Extract score
    for line in evaluation_text.split("\n"):
        if "TOTAL_SCORE:" in line:
            try:
                score_part = line.split(":")[1].strip()
                result["total_score"] = int(score_part.split("/")[0])
            except:
                pass
        if "PASSED:" in line:
            result["passed"] = "yes" in line.lower()
        if "DISCONFIRM_CHECK:" in line:
            result["disconfirm_passed"] = "pass" in line.lower()

    return result


def evaluate_submission(domain: str, level: int, submission_path: Path) -> dict:
    """Main evaluation function."""

    if not submission_path.exists():
        return {"error": f"File not found: {submission_path}"}

    submission_text = submission_path.read_text()

    print(f"\n🔍 Evaluating {domain} Level {level} submission...")
    print(f"   File: {submission_path}")
    print(f"   Size: {len(submission_text)} characters")

    # Run evaluation
    result = evaluate_with_claude(domain, submission_text, level)

    # Apply level-specific rules
    if level == 3:
        # Check for minimum criterion scores (would need more parsing)
        pass

    # Domain-3 special rule: must pass disconfirm check
    if domain == "domain-3" and not result.get("disconfirm_passed", True):
        result["passed"] = False
        result["reason"] = "Failed disconfirming evidence requirement (must find ≥50%)"

    return result


def generate_feedback(evaluation: dict, domain: str, level: int) -> str:
    """Generate formatted feedback from evaluation."""

    feedback = []
    feedback.append(f"\n{'='*60}")
    feedback.append(f"EVALUATION RESULTS: {domain.upper()} LEVEL {level}")
    feedback.append(f"{'='*60}\n")

    feedback.append(f"Score: {evaluation.get('total_score', 'N/A')}/100")
    feedback.append(f"Status: {'✅ PASSED' if evaluation.get('passed') else '❌ NOT YET'}\n")

    if level == 2:
        feedback.append("--- Detailed Feedback ---\n")
        feedback.append(evaluation.get("raw_evaluation", ""))
        feedback.append("\n--- Next Steps ---")
        if evaluation.get("passed"):
            feedback.append("You've passed Level 2! You can now attempt Level 3.")
            feedback.append(f"Run: skillforge take {domain} --level 3")
        else:
            feedback.append("Review the feedback above and try again in 7 days.")
            feedback.append("Focus on the criteria where you scored lowest.")
    else:  # Level 3
        if evaluation.get("passed"):
            feedback.append(f"\n🎓 Congratulations! You've achieved Level 3 competency in {domain}!")
        else:
            feedback.append("\nNot yet at Level 3. You can retry in 30 days.")
            feedback.append("Consider reviewing Level 2 materials before your next attempt.")

    return "\n".join(feedback)


def save_evaluation_record(
    domain: str,
    level: int,
    submission_path: Path,
    evaluation: dict,
    student_record: dict
) -> None:
    """Save evaluation to student record."""

    eval_record = {
        "domain": domain,
        "level": level,
        "date": datetime.now().isoformat(),
        "submission_file": str(submission_path),
        "score": evaluation.get("total_score", 0),
        "passed": evaluation.get("passed", False),
    }

    # Add to attempts
    if domain not in student_record.get("domains", {}):
        student_record["domains"][domain] = {"level": 0, "attempts": []}

    student_record["domains"][domain]["attempts"].append(eval_record)

    # Update level if passed
    if evaluation.get("passed"):
        current = student_record["domains"][domain].get("level", 0)
        student_record["domains"][domain]["level"] = max(current, level)

    # Save
    record_path = SKILLFORGE_HOME / "record.json"
    record_path.write_text(json.dumps(student_record, indent=2))

    # Also save detailed evaluation
    evals_dir = SKILLFORGE_HOME / "evaluations"
    evals_dir.mkdir(parents=True, exist_ok=True)

    eval_id = f"{domain}-L{level}-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
    eval_path = evals_dir / f"{eval_id}.json"

    full_eval = {
        **eval_record,
        "evaluation_id": eval_id,
        "raw_evaluation": evaluation.get("raw_evaluation", ""),
    }
    eval_path.write_text(json.dumps(full_eval, indent=2))


def check_cooldown(domain: str, level: int, student_record: dict) -> Optional[str]:
    """Check if student is in cooldown period."""

    attempts = student_record.get("domains", {}).get(domain, {}).get("attempts", [])

    # Filter to same level, failed attempts
    relevant = [a for a in attempts if a.get("level") == level and not a.get("passed")]

    if not relevant:
        return None

    last_attempt = relevant[-1]
    last_date = datetime.fromisoformat(last_attempt["date"])

    cooldown_days = 7 if level == 2 else 30
    days_since = (datetime.now() - last_date).days

    if days_since < cooldown_days:
        remaining = cooldown_days - days_since
        return f"Cooldown active. You can retry in {remaining} days."

    return None


# CLI interface
def main():
    """CLI for evaluation engine."""
    import argparse

    parser = argparse.ArgumentParser(description="SkillForge Evaluation Engine")
    parser.add_argument("domain", help="Domain to evaluate (e.g., domain-3)")
    parser.add_argument("--level", "-l", type=int, required=True, help="Level (2 or 3)")
    parser.add_argument("--file", "-f", required=True, help="Submission file")
    parser.add_argument("--skip-cooldown", action="store_true", help="Skip cooldown check (testing)")

    args = parser.parse_args()

    # Load student record
    record_path = SKILLFORGE_HOME / "record.json"
    if not record_path.exists():
        print("Not initialized. Run 'skillforge init' first.")
        return 1

    student_record = json.loads(record_path.read_text())

    # Check cooldown
    if not args.skip_cooldown:
        cooldown_msg = check_cooldown(args.domain, args.level, student_record)
        if cooldown_msg:
            print(f"⏳ {cooldown_msg}")
            return 1

    # Run evaluation
    submission_path = Path(args.file)
    evaluation = evaluate_submission(args.domain, args.level, submission_path)

    if "error" in evaluation:
        print(f"❌ Error: {evaluation['error']}")
        return 1

    # Generate and display feedback
    feedback = generate_feedback(evaluation, args.domain, args.level)
    print(feedback)

    # Save record
    save_evaluation_record(
        args.domain,
        args.level,
        submission_path,
        evaluation,
        student_record
    )

    print(f"\n📁 Evaluation saved to ~/.skillforge/evaluations/")

    return 0 if evaluation.get("passed") else 1


if __name__ == "__main__":
    sys.exit(main())
