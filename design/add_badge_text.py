#!/usr/bin/env python3
"""
Add text overlays to generated badge icons.

Usage:
    python add_badge_text.py <input_dir> <output_dir>

Example:
    python add_badge_text.py ~/Desktop/research-quals\ badges/ ./badges_final/

Requires: Pillow (pip install Pillow)
"""

import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

# Badge text definitions
BADGE_TEXT = {
    # Domain 1: Pattern Recognition
    "d1-foundation": ("SKILL-FORGE", "PATTERN RECOGNITION", "FOUNDATION"),
    "d1-practice": ("SKILL-FORGE", "PATTERN RECOGNITION", "PRACTICE"),
    "d1-mastery": ("SKILL-FORGE", "PATTERN RECOGNITION", "MASTERY"),

    # Domain 2: Theoretical Positioning
    "d2-foundation": ("SKILL-FORGE", "THEORETICAL POSITIONING", "FOUNDATION"),
    "d2-practice": ("SKILL-FORGE", "THEORETICAL POSITIONING", "PRACTICE"),
    "d2-mastery": ("SKILL-FORGE", "THEORETICAL POSITIONING", "MASTERY"),

    # Domain 3: Qualitative Mechanism
    "d3-foundation": ("SKILL-FORGE", "QUALITATIVE MECHANISM", "FOUNDATION"),
    "d3-practice": ("SKILL-FORGE", "QUALITATIVE MECHANISM", "PRACTICE"),
    "d3-mastery": ("SKILL-FORGE", "QUALITATIVE MECHANISM", "MASTERY"),

    # Domain 4: Theoretical Framing
    "d4-foundation": ("SKILL-FORGE", "THEORETICAL FRAMING", "FOUNDATION"),
    "d4-practice": ("SKILL-FORGE", "THEORETICAL FRAMING", "PRACTICE"),
    "d4-mastery": ("SKILL-FORGE", "THEORETICAL FRAMING", "MASTERY"),

    # Domain 5: Epistemological Genre
    "d5-foundation": ("SKILL-FORGE", "EPISTEMOLOGICAL GENRE", "FOUNDATION"),
    "d5-practice": ("SKILL-FORGE", "EPISTEMOLOGICAL GENRE", "PRACTICE"),
    "d5-mastery": ("SKILL-FORGE", "EPISTEMOLOGICAL GENRE", "MASTERY"),

    # Domain 6: Adversarial Evidence
    "d6-foundation": ("SKILL-FORGE", "ADVERSARIAL EVIDENCE", "FOUNDATION"),
    "d6-practice": ("SKILL-FORGE", "ADVERSARIAL EVIDENCE", "PRACTICE"),
    "d6-mastery": ("SKILL-FORGE", "ADVERSARIAL EVIDENCE", "MASTERY"),

    # Domain 7: Claim Verification
    "d7-foundation": ("SKILL-FORGE", "CLAIM VERIFICATION", "FOUNDATION"),
    "d7-practice": ("SKILL-FORGE", "CLAIM VERIFICATION", "PRACTICE"),
    "d7-mastery": ("SKILL-FORGE", "CLAIM VERIFICATION", "MASTERY"),

    # Path badges
    "path-theory-builder": ("SKILL-FORGE", "THEORY BUILDER", "PATH"),
    "path-evidence-analyst": ("SKILL-FORGE", "EVIDENCE ANALYST", "PATH"),
    "path-integrity-guardian": ("SKILL-FORGE", "INTEGRITY GUARDIAN", "PATH"),
    "path-full-researcher": ("SKILL-FORGE", "FULL RESEARCHER", "PATH"),

    # Capstone
    "capstone-ai-supervisor": ("SKILL-FORGE", "AI SUPERVISOR", "CAPSTONE"),
}

# Color schemes by level/type
COLORS = {
    "foundation": {"primary": "#CD7F32", "secondary": "#8B4513", "text": "#FFF8DC"},
    "practice": {"primary": "#C0C0C0", "secondary": "#708090", "text": "#FFFFFF"},
    "mastery": {"primary": "#FFD700", "secondary": "#B8860B", "text": "#1a1a2e"},
    "path": {"primary": "#FFD700", "secondary": "#4B0082", "text": "#FFFFFF"},
    "capstone": {"primary": "#FFD700", "secondary": "#000000", "text": "#FFD700"},
}


def get_level(badge_name: str) -> str:
    """Extract level/type from badge name."""
    if "foundation" in badge_name:
        return "foundation"
    elif "practice" in badge_name:
        return "practice"
    elif "mastery" in badge_name:
        return "mastery"
    elif "path-" in badge_name:
        return "path"
    elif "capstone" in badge_name:
        return "capstone"
    return "foundation"


def load_font(size: int) -> ImageFont.FreeTypeFont:
    """Load a font, falling back to default if needed."""
    # Try common system fonts
    font_paths = [
        "/System/Library/Fonts/Helvetica.ttc",
        "/System/Library/Fonts/SFNSDisplay.ttf",
        "/Library/Fonts/Arial.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    ]

    for path in font_paths:
        try:
            return ImageFont.truetype(path, size)
        except (OSError, IOError):
            continue

    # Fall back to default
    return ImageFont.load_default()


def add_text_to_badge(
    input_path: Path,
    output_path: Path,
    top_text: str,
    middle_text: str,
    bottom_text: str,
    colors: dict,
):
    """Add text overlays to a badge image."""
    # Load image
    img = Image.open(input_path).convert("RGBA")
    width, height = img.size

    # Create drawing context
    draw = ImageDraw.Draw(img)

    # Font sizes relative to image size
    top_font_size = int(height * 0.06)
    middle_font_size = int(height * 0.05)
    bottom_font_size = int(height * 0.04)

    top_font = load_font(top_font_size)
    middle_font = load_font(middle_font_size)
    bottom_font = load_font(bottom_font_size)

    # Text color
    text_color = colors["text"]

    # Calculate positions (centered)
    # Top text: near top of badge
    top_bbox = draw.textbbox((0, 0), top_text, font=top_font)
    top_width = top_bbox[2] - top_bbox[0]
    top_x = (width - top_width) // 2
    top_y = int(height * 0.12)

    # Middle text: lower portion
    mid_bbox = draw.textbbox((0, 0), middle_text, font=middle_font)
    mid_width = mid_bbox[2] - mid_bbox[0]
    mid_x = (width - mid_width) // 2
    mid_y = int(height * 0.72)

    # Bottom text: below middle
    bot_bbox = draw.textbbox((0, 0), bottom_text, font=bottom_font)
    bot_width = bot_bbox[2] - bot_bbox[0]
    bot_x = (width - bot_width) // 2
    bot_y = int(height * 0.82)

    # Draw text with slight shadow for depth
    shadow_color = "#00000080"
    shadow_offset = 2

    # Top text
    draw.text((top_x + shadow_offset, top_y + shadow_offset), top_text, font=top_font, fill=shadow_color)
    draw.text((top_x, top_y), top_text, font=top_font, fill=text_color)

    # Middle text
    draw.text((mid_x + shadow_offset, mid_y + shadow_offset), middle_text, font=middle_font, fill=shadow_color)
    draw.text((mid_x, mid_y), middle_text, font=middle_font, fill=text_color)

    # Bottom text
    draw.text((bot_x + shadow_offset, bot_y + shadow_offset), bottom_text, font=bottom_font, fill=shadow_color)
    draw.text((bot_x, bot_y), bottom_text, font=bottom_font, fill=text_color)

    # Save
    output_path.parent.mkdir(parents=True, exist_ok=True)
    img.save(output_path, "PNG")
    print(f"  ✓ {output_path.name}")


def process_badges(input_dir: Path, output_dir: Path):
    """Process all badge images in input directory."""
    print(f"\nProcessing badges from: {input_dir}")
    print(f"Output to: {output_dir}\n")

    processed = 0
    skipped = 0

    for input_file in input_dir.glob("*.png"):
        # Try to match filename to badge definition
        badge_name = input_file.stem.lower()

        # Handle various naming conventions
        # e.g., "d1-foundation", "D1_Foundation", "d1foundation"
        normalized = badge_name.replace("_", "-").replace(" ", "-")

        if normalized not in BADGE_TEXT:
            # Try without hyphens
            for key in BADGE_TEXT:
                if key.replace("-", "") == normalized.replace("-", ""):
                    normalized = key
                    break

        if normalized not in BADGE_TEXT:
            print(f"  ⚠ Skipping {input_file.name} (no matching badge definition)")
            skipped += 1
            continue

        top, middle, bottom = BADGE_TEXT[normalized]
        level = get_level(normalized)
        colors = COLORS[level]

        output_path = output_dir / f"{normalized}.png"
        add_text_to_badge(input_file, output_path, top, middle, bottom, colors)
        processed += 1

    print(f"\nDone! Processed: {processed}, Skipped: {skipped}")


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        print("\nBadge definitions available:")
        for name in sorted(BADGE_TEXT.keys()):
            texts = BADGE_TEXT[name]
            print(f"  {name}: {texts[1]} ({texts[2]})")
        sys.exit(1)

    input_dir = Path(sys.argv[1]).expanduser()
    output_dir = Path(sys.argv[2]).expanduser()

    if not input_dir.exists():
        print(f"Error: Input directory not found: {input_dir}")
        sys.exit(1)

    process_badges(input_dir, output_dir)


if __name__ == "__main__":
    main()
