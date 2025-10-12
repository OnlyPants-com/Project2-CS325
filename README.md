# Jobmatcher Project for CS325 at SIUE
This project uses the Adzuna API to aquire the data for processing. This data is then processed to be in a more readable form. The data is then turned into an emebedded vector, which is then used for cosine similarity comparisons using my resume.

## Structure

```
Project1-CS325
- data
    - cleaned_jobs.json -- Preprocessed data from jobs.json
    - cleaned_resume.json -- Preprocessed the resume
    - embeddings.json -- Jobs embedded into individual vectors
    - jobs.json -- Raw job posting data from Adzuna API
    - resume_embedding.json -- Resume embedded into a single vector
    - resume.txt -- My resume in text form
- src
    - embedding.py -- Embeds the jobs individually into a combined vector
    - getdata.py -- Aquires data from Adzuna API
    - preprocess.py -- Formats the data to be in a more readable form
    - similarity.py -- Finds the cosine similarity based on resume and jobs
- README.md
- requirements.yml
```