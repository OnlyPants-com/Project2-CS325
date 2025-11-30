import requests #type: ignore
import json
import os
import time

SEARCH_KEYWORD = "computer science"
SEARCH_LOCATION = "St. Louis"
NUM_PAGES = 3              
RESULTS_PER_PAGE = 50      


# Adzuna API credentials
APP_ID = "0b620397"
APP_KEY = "f01e3b3defed7cf622fc7c887a4d2038"

def fetch_jobs_from_page(page_number):
    # Adzuna API URL with page number
    api_url = f"https://api.adzuna.com/v1/api/jobs/us/search/{page_number}"
    
    params = {
        "app_id": APP_ID,
        "app_key": APP_KEY,
        "results_per_page": RESULTS_PER_PAGE,
        "what": SEARCH_KEYWORD,
        "where": SEARCH_LOCATION,
        "content-type": "application/json"
    }
    
    try:
        print(f"  Fetching page {page_number}...")
        response = requests.get(api_url, params=params)
        response.raise_for_status()
        data = response.json()
        
        # Extract job data
        jobs = []
        for job in data.get("results", []):
            jobs.append({
                "title": job.get("title"),
                "company": job.get("company", {}).get("display_name"),
                "location": job.get("location", {}).get("display_name"),
                "description": job.get("description"),
                "redirect_url": job.get("redirect_url")
            })
        
        print(f"Got {len(jobs)} jobs from page {page_number}")
        return jobs
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching page {page_number}: {e}")
        return []


def fetch_jobs():
    all_jobs = []
    
    print(f"\nFetching '{SEARCH_KEYWORD}' jobs in '{SEARCH_LOCATION}'")
    print(f"Getting {NUM_PAGES} page(s) with {RESULTS_PER_PAGE} results per page")
    print("-" * 50)
    
    for page_num in range(1, NUM_PAGES + 1):
        jobs = fetch_jobs_from_page(page_num)
        all_jobs.extend(jobs)
        
        # Be nice to the API - small delay between requests
        if page_num < NUM_PAGES:
            time.sleep(0.5)  # Wait 0.5 seconds between pages
    
    print("-" * 50)
    print(f"Total jobs fetched: {len(all_jobs)}")
    
    return all_jobs


def save_jobs(jobs, filename="data/jobs.json"):
    #Save jobs to JSON file.
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(jobs, f, indent=2, ensure_ascii=False)
    print(f"Saved {len(jobs)} jobs to {filename}")


if __name__ == "__main__":
    jobs = fetch_jobs()
    if jobs:
        save_jobs(jobs)
    else:
        print("No jobs found.")
