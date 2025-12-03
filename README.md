# Jobmatcher Project for CS325 at SIUE
This project uses the Adzuna API to aquire the data for processing. This data is then processed to be in a more readable form. The data is then turned into an emebedded vector, which is then used for cosine similarity comparisons using my resume.

**Updates for Project 2:**
This version has been refactored to follow SOLID principles (Single Responsibility and Dependency Inversion), making it more maintainable, testable, and flexible.

### Prerequisites
* Python 3.10
* OpenAI API key
* Adzuna API credentials
* Resume in plain .txt file

## How to run Docker image (Bonus)
This application is containerized using Docker, allowing you to run it without installing Python or dependencies locally.

Build the image using the Dockerfile

```
docker build -t onlypantscom/job-matcher:latest
```
### Before Running (IMPORTANT)
The project relies on OpenAI and Adzuna API keys, so a new file is needed.
1. Before running, create a ```.env``` file inside the root directory
2. An API key for both Adzuna and OpenAI is needed. To get the Adzuna key, go to https://developer.adzuna.com/.
3. To get the OpenAI key, go to https://platform.openai.com/api-keys. Create an account and create a secret key.
4. Add these sections to it ```OPENAI_API_KEY=sk-proj-your-key-here```,
```ADZUNA_APP_ID=your-id-here```, and 
```ADZUNA_APP_KEY=your-key-here```
- Sidenote: this project relies on Adzuna, but it is very easy to replace it with another API.
Running it
```
docker run --env-file .env onlypantscom/job-matcher:latest
```

To run tests:
```
docker run --env-file .env onlypantscom/job-matcher:latest pytest
```

## Structure

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
├── .github/
│   └── workflows/
│       └── dockerCI.yml           -- CI/CD pipeline configuration
├── interfaces.py                   -- Abstract interface for embedding services (NEW - DIP)
├── embedding_service.py            -- OpenAI embedding service implementation (NEW - DIP)
├── job_matcher.py                  -- Main orchestrator to run full pipeline (NEW - SRP)
├── Dockerfile                      -- Docker container configuration
├── .env                            -- Environment variables (NOT committed to git)
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

## Running the Project (Option 1: Recommended)
Run this inside of the terminal:
```
python job_matcher.py
```
This does all of the steps in sequence.
1. Fetch data
2. Preprocess the data
3. Generate embeddings
4. Calculate similarities

## Running the Project (Option 2)
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