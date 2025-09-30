import requests
import json
import os

# Adzuna API was used and registered for, giving the ID and KEY
API_URL = "https://api.adzuna.com/v1/api/jobs/us/search/1"
APP_ID = "0b620397"
APP_KEY = "f01e3b3defed7cf622fc7c887a4d2038"

PARAMS = {
    "app_id": APP_ID,
    "app_key": APP_KEY,
    "results_per_page": 20,
    "what": "computer science",   # keyword
    "where": "St. Louis",         # location
    "content-type": "application/json"
}

# -----------------------
# Fetch jobs
# -----------------------
def fetch_jobs():
    try:
        response = requests.get(API_URL, params=PARAMS)
        response.raise_for_status()  # raises HTTPError if bad response
        data = response.json()

        # Extract only the fields wanted
        jobs = []
        for job in data.get("results", []):
            jobs.append({
                "title": job.get("title"),
                "company": job.get("company", {}).get("display_name"),
                "location": job.get("location", {}).get("display_name"),
                "description": job.get("description"),
                "redirect_url": job.get("redirect_url")
            })

        return jobs

    except requests.exceptions.RequestException as e:
        print(f"Error fetching jobs: {e}")
        return []

# -----------------------
# Save to file
# -----------------------
def save_jobs(jobs, filename="../data/jobs.json"):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(jobs, f, indent=2, ensure_ascii=False)
    print(f"Saved {len(jobs)} jobs to {filename}")

# -----------------------
# Main
# -----------------------
if __name__ == "__main__":
    jobs = fetch_jobs()
    if jobs:
        save_jobs(jobs)
