# Jobmatcher Project for CS325 at SIUE
This project uses the Adzuna API to aquire the data for processing. This data is then processed to be in a more readable form. The data is then turned into an emebedded vector, which is then used for cosine similarity comparisons using the students resume.

## Structure

```
Project1-CS325
- data
    - cleaned_jobs.json <code style="color : aquamarine"> Cleaned job postings from Adzuna</code>
    - cleaned_resume.json
    - embeddings.json
    - jobs.json
    - resume_embedding.json
    - resume.txt
- src
    - embedding.py
    - getdata.py
    - preprocess.py
    - similarity.py
- README.md
- requirements.yml
```