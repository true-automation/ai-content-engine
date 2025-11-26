# ==============================================
# generate_script.py — Gemini API Version
# Author: Your Name
# Purpose: Generate short-form content scripts 
#          using Gemini 1.5 Flash / Pro
# ==============================================

import os
import json
from pathlib import Path
from google import genai

# ----------------------------------------------
# CONFIG
# ----------------------------------------------

OUTPUT_DIR = Path("content/generated_scripts")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

GEMINI_MODEL = "gemini-1.5-flash"   # fast + cheap (recommended)
# GEMINI_MODEL = "gemini-1.5-pro"   # higher quality (more expensive)

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise Exception("ERROR: Set environment variable GEMINI_API_KEY first!")


# ----------------------------------------------
# INITIALIZE CLIENT
# ----------------------------------------------

client = genai.Client(api_key=API_KEY)


# ----------------------------------------------
# PROMPT TEMPLATE
# ----------------------------------------------

SCRIPT_PROMPT = """
You are a professional content scriptwriter for TikTok, Instagram Reels, and YouTube Shorts.

Write a short, engaging, high-retention video script with:
- Strong hook in the first 3 seconds
- Simple conversational language
- Clear storytelling or value
- 8–12 sentences maximum
- Optional CTA at the end

Topic: "{topic}"

Output format must be JSON only:

{
  "title": "...",
  "script": [
    "sentence 1",
    "sentence 2",
    ...
  ]
}
"""


# ----------------------------------------------
# GENERATE SCRIPT FUNCTION
# ----------------------------------------------

def generate_script(topic: str):
    print(f"🔥 Generating script for topic: {topic}")

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=SCRIPT_PROMPT.format(topic=topic),
    )

    # Gemini often outputs text — ensure it's JSON
    raw_text = response.text

    try:
        data = json.loads(raw_text)
    except json.JSONDecodeError:
        print("⚠️ Gemini returned non-JSON, attempting cleanup...")
        cleaned = raw_text[
            raw_text.find("{") : raw_text.rfind("}") + 1
        ]
        data = json.loads(cleaned)

    # Save output ---------------------------------
    file_path = OUTPUT_DIR / f"{topic.replace(' ', '_')}.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"✅ Script saved: {file_path}")
    return data


# ----------------------------------------------
# MAIN PROGRAM
# ----------------------------------------------

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Generate content scripts using Gemini")
    parser.add_argument("--topic", required=True, help="Topic for the script")

    args = parser.parse_args()
    generate_script(args.topic)
