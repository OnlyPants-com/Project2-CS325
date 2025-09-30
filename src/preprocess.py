# src/preprocess.py

import json
import re
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
RAW_JOBS_FILE = DATA_DIR / "jobs.json"
CLEANED_JOBS_FILE = DATA_DIR / "cleaned_jobs.json"
RESUME_FILE = DATA_DIR / "resume.txt"
CLEANED_RESUME_FILE = DATA_DIR / "cleaned_resume.json"


def clean_text(text: str) -> str:
    """Remove HTML tags, special characters, extra spaces, lowercase."""
    if not text:
        return "N/A"
    text = re.sub(r"<.*?>", " ", text)                # remove HTML tags
    text = re.sub(r"[^a-zA-Z0-9\s.,]", " ", text)     # remove special chars
    text = re.sub(r"\s+", " ", text)                  # collapse whitespace
    return text.strip().lower()                       # normalize


def preprocess_jobs():
    """Load raw_jobs.json, clean text, save to cleaned_jobs.json."""
    if not RAW_JOBS_FILE.exists():
        raise FileNotFoundError(f"{RAW_JOBS_FILE} not found. Run getdata.py first.")

    with open(RAW_JOBS_FILE, "r", encoding="utf-8") as f:
        raw_jobs = json.load(f)

    cleaned_jobs = []
    for job in raw_jobs:
        cleaned_jobs.append({
            "title": clean_text(job.get("title", "")),
            "company": clean_text(job.get("company", "")),
            "location": clean_text(job.get("location", "")),
            "description": clean_text(job.get("description", "")),
            "redirect_url": job.get("redirect_url", "N/A")
        })

    with open(CLEANED_JOBS_FILE, "w", encoding="utf-8") as f:
        json.dump(cleaned_jobs, f, indent=2)

    print(f"Cleaned jobs saved to {CLEANED_JOBS_FILE}")

def preprocess_resume():
    """Load resume.txt, extract key sections, clean, save to cleaned_resume.json."""
    if not RESUME_FILE.exists():
        raise FileNotFoundError(f"{RESUME_FILE} not found. Please add your resume.txt.")

    with open(RESUME_FILE, "r", encoding="latin-1") as f:
        resume_text = f.read()

    # Normalize text
    resume_text = resume_text.replace("\r", "\n")

    # Very simple section extraction by keywords
    sections = {
        "experience": "",
        "skills": "",
        "education": ""
    }

    current_section = None
    for line in resume_text.split("\n"):
        line_clean = line.strip().lower()

        if "experience" in line_clean:
            current_section = "experience"
            continue
        elif "skill" in line_clean:
            current_section = "skills"
            continue
        elif "education" in line_clean:
            current_section = "education"
            continue

        if current_section:
            sections[current_section] += " " + line

    # Clean each section
    for key in sections:
        sections[key] = clean_text(sections[key])

    with open(CLEANED_RESUME_FILE, "w", encoding="utf-8") as f:
        json.dump(sections, f, indent=2)

    print(f"Cleaned resume saved to {CLEANED_RESUME_FILE}")

if __name__ == "__main__":
    preprocess_jobs()
    preprocess_resume()
