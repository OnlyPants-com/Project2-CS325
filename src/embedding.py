import os
import json
import sys

#Add parent directory to path to import from embedding_service
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from embedding_service import OpenAIEmbeddingService

# File locations
CLEANED_JOBS_FILE = "data/cleaned_jobs.json"
CLEANED_RESUME_FILE = "data/cleaned_resume.json"
JOB_OUTPUT_FILE = "data/embeddings.json"
RESUME_EMBEDDING_FILE = "data/resume_embedding.json"

API_KEY = "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"

embedding_service = OpenAIEmbeddingService(
    api_key=API_KEY,
    model="text-embedding-3-small"
)

def get_embedding(text: str):
    # Generate an embedding for the given text using OpenAI.

    # MODIFIED TO USE OpenAIEmbeddingService from embedding_service.py
    return embedding_service.get_embedding(text)

def embed_job_postings():
    with open(CLEANED_JOBS_FILE, "r", encoding="utf-8") as f:
        jobs = json.load(f)

    job_embeddings = []
    print("Embedding job postings...")
    for job in jobs:
        text = (
            f"Title: {job.get('title', '')}\n"
            f"Company: {job.get('company', '')}\n"
            f"Location: {job.get('location', '')}\n"
            f"Description: {job.get('description', '')}"
        )
        embedding = get_embedding(text)
        job_embeddings.append({
            "title": job.get("title", ""),
            "company": job.get("company", ""),
            "location": job.get("location", ""),
            "embedding": embedding
        })
    with open(JOB_OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(job_embeddings, f, indent=2)

    print(f"Saved {len(job_embeddings)} job embeddings to {JOB_OUTPUT_FILE}")
    return job_embeddings


def embed_resume():
    print("\nEmbedding resume...")
    with open(CLEANED_RESUME_FILE, "r", encoding="utf-8") as f:
        resume_text = f.read().strip()

    try:
        embedding = get_embedding(resume_text)
        data = {"embedding": embedding}
        with open(RESUME_EMBEDDING_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        print(f"Saved resume embedding to {RESUME_EMBEDDING_FILE}")
        return embedding
    except Exception as e:
        print(f"Error embedding resume: {e}")
        return None

def main():
    embed_job_postings()
    embed_resume()


if __name__ == "__main__":
    main()
