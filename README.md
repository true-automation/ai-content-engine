📦 ai-content-engine
Modular AI-powered content generation system for scripts, voiceovers, thumbnails, metadata & automated rendering.

ai-content-engine is a fully automated content production pipeline designed for high-volume creators, agencies, and AI-driven automation systems.
It allows you to generate scripts → voiceovers → video scenes → subtitles → thumbnails → metadata with a single command or API call.

Built for:

TikTok / Reels / Shorts

YouTube long/short-form

B2B content creation workflows

Fully automated posting systems (n8n, custom bots, browser agents)

🚀 Key Features

AI Script Generator (OpenAI / Groq)

AI Voiceover Generation (ElevenLabs / OpenAI TTS)

Video Assembly Pipeline (FFmpeg)

Auto Subtitles (Whisper / faster-whisper)

Thumbnail Generator (DALL·E / Midjourney API)

Auto Metadata Generation (titles, hashtags, keywords, descriptions)

JSON-based content plan system

Local or cloud storage (VPS, S3, GCS)

Extensible plugin architecture

📁 Directory Structure
ai-content-engine/
 ├── src/
 │   ├── ai/
 │   │   ├── script_generator.py
 │   │   ├── voiceover.py
 │   │   ├── subtitles.py
 │   │   ├── metadata.py
 │   │   └── thumbnail.py
 │   ├── video/
 │   │   ├── builder.py
 │   │   └── effects.py
 │   ├── workflows/
 │   │   ├── generate_content.py
 │   │   └── batch_runner.py
 │   └── utils/
 │       ├── logging.py
 │       ├── storage.py
 │       └── config.py
 ├── content/
 │   ├── scripts/
 │   ├── voice/
 │   ├── videos/
 │   ├── thumbnails/
 │   └── subtitles/
 ├── examples/
 │   └── demo_request.json
 ├── .env.example
 ├── requirements.txt
 ├── README.md
 └── LICENSE

⚙️ Installation
git clone https://github.com/yourusername/ai-content-engine.git
cd ai-content-engine

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
cp .env.example .env


Update your .env file:

OPENAI_API_KEY=xxxx
ELEVENLABS_API_KEY=xxxx
STORAGE_PATH=./content

🧠 How It Works

User Input

topic

style

duration

platform (TikTok/Shorts/YouTube)

AI Creates Script

AI Creates Voiceover

Video Builder assembles clips + subtitles + music

Thumbnail AI generates cover

Output stored in /content/...

📌 Quick Start
Generate one complete content package:
python src/workflows/generate_content.py --topic "AI tools 2025"

Generate 10 videos (batch):
python src/workflows/batch_runner.py --file examples/demo_request.json

🧩 Example JSON Input
{
  "topic": "Productivity hacks for software engineers",
  "style": "motivational",
  "platform": "tiktok",
  "voice": "male-energetic",
  "duration": 30
}

🖼 Output Example Structure
content/
  scripts/2025-11-25_productivity.txt
  voice/2025-11-25_productivity.wav
  videos/2025-11-25_productivity.mp4
  thumbnails/2025-11-25_productivity.png
  subtitles/2025-11-25_productivity.srt

🧪 Extensible Plugin Architecture

You can easily plug in:

New AI models

Custom voices

CapCut API

DaVinci Resolve scripts

n8n / Zapier triggers

Custom rendering templates

Each module is replaceable.

🛠 Tech Stack

Python 3.11

OpenAI API

ElevenLabs API

FFmpeg

Whisper / faster-whisper

PIL / OpenCV

Rich (CLI UI)

pydantic (config & schema)

asyncio

🧵 Roadmap

 Multi-template rendering system

 Character animation support

 Music generation module

 Voice clone library

 Real-time content API

 Web dashboard UI

 Full CLI "wizard" mode

📝 License

MIT License

👨‍💻 Maintainer

Babi Panda
AI Automation Engineer
Creator of multi-platform automation content systems
