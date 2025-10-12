import json
import numpy as np #type: ignore
from scipy.spatial.distance import cosine #type: ignore

EMBEDDINGS_PATH = "data/embeddings.json"
RESUME_PATH = "data/resume_embedding.json"

def load_embeddings():
    #Load job embeddings (list of job entries).
    with open(EMBEDDINGS_PATH, "r", encoding="utf-8") as f:
        jobs = json.load(f)
    return jobs

def load_resume_embedding():
    #Load the student's resume embedding vector.
    with open(RESUME_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    return np.array(data["embedding"])

def compute_similarity(job_embedding, resume_embedding):
    #Compute cosine similarity between two embeddings.
    return 1 - cosine(job_embedding, resume_embedding)

def main():
    print("Loading embeddings...")
    jobs = load_embeddings()
    resume_embedding = load_resume_embedding()

    print(f"Loaded {len(jobs)} job postings.")

    results = []
    for job in jobs:
        job_vector = np.array(job["embedding"])
        similarity = compute_similarity(job_vector, resume_embedding)

        results.append({
            "title": job["title"],
            "company": job.get("company", "Unknown"),
            "location": job.get("location", "Unknown"),
            "similarity": similarity
        })

    # Sort by similarity (descending)
    results.sort(key=lambda x: x["similarity"], reverse=True)

    # --- Display Top 10 ---
    print("\nTop 10 Most Similar Jobs:\n")
    for i, job in enumerate(results[:10], start=1):
        print(f"{i}. {job['title']} ({job['company']}, {job['location']})")
        print(f"   Similarity: {job['similarity']:.4f}\n")

if __name__ == "__main__":
    main()
