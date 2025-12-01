# Jobmatcher Project for CS325 at SIUE
This project uses the Adzuna API to aquire the data for processing. This data is then processed to be in a more readable form. The data is then turned into an emebedded vector, which is then used for cosine similarity comparisons using my resume.

**Updates for Project 2:**
This version has been refactored to follow SOLID principles (Single Responsibility and Dependency Inversion), making it more maintainable, testable, and flexible.

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
- requirements.yml -- Conda environment file
```
```
Project2-CS325/
├── data/
│   ├── cleaned_jobs.json           -- Preprocessed data from jobs.json
│   ├── cleaned_resume.json         -- Preprocessed resume sections
│   ├── embeddings.json             -- Jobs embedded into individual vectors
│   ├── jobs.json                   -- Raw job posting data from Adzuna API
│   ├── resume_embedding.json       -- Resume embedded into a single vector
│   └── resume.txt                  -- Your resume in text form (YOU MUST ADD THIS)
├── src/
│   ├── embedding.py                -- Embeds jobs and resume into vectors (MODIFIED for DIP)
│   ├── getdata.py                  -- Acquires data from Adzuna API (UPDATED for multiple pages)
│   ├── preprocess.py               -- Formats data to be in a more readable form
│   └── similarity.py               -- Finds cosine similarity based on resume and jobs
├── tests/
│   └── test_embedding.py           -- Unit tests with mocking (no API calls needed)
├── diagrams/
│   ├── UML Class Diagram.png       -- UML class diagram showing architecture
│   └── UML Sequence Diagram.png    -- UML sequence diagram showing workflow
├── interfaces.py                   -- Abstract interface for embedding services (NEW - DIP)
├── embedding_service.py            -- OpenAI embedding service implementation (NEW - DIP)
├── job_matcher.py                  -- Main orchestrator to run full pipeline (NEW - SRP)
├── requirements.txt                -- pip dependencies
├── requirements.yml                -- Conda environment file
├── README.md                       -- This file
└── REFACTORING.md                  -- Documentation of SOLID principles applied
```

## Setup
A conda environment was used for this project, therefore, a conda environment must be created to run the project. This environment has all of the required dependencies needed for the project to run (hopefully).
```
conda env create -f requirements.yml
conda activate "name of environment"
```

## Running the Project
First, the data must be aquired and then preprocessed. To do this, the ```getdata.py``` and the ```preprocess.py``` scripts are needed.

Run this in the command line (FROM ROOT DIRECTORY, OR ELSE IT WILL HAVE AN ERROR):

When running in the command line, executions may appear as ```.\src\getdata.py```, ```.\src\preprocess.py``` and so on. This is okay, the program will still run.
### Get the Data
```
python src/getdata.py
```
This saves the raw data to: ```data/jobs.json```
### Preprocess the Data
```
python src/preprocess.py
```
This process the data by removing HTML tags, special characters, and turning the whole string into lowercase
 
Saves the cleaned versions to: ```data/cleaned_jobs.json``` and ```data/cleaned_resume.json```
### Embed the Data into Vectors
```
python src/embedding.py
```
This process embeds the individual job postings to ```data/embeddings.json``` and the resume embedding to ```resume_embedding.json```
### Find the Best-Matching Jobs
```
python src/similarity.py
```
This process uses cosine similarity to compute the top 10 most suitable jobs based on the resume. The results are output into the terminal.