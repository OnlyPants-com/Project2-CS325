# src/preprocess.py

import json
import re
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
RAW_JOBS_FILE = DATA_DIR / "jobs.json"
CLEANED_JOBS_FILE = DATA_DIR / "cleaned_jobs.json"


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


if __name__ == "__main__":
    preprocess_jobs()
