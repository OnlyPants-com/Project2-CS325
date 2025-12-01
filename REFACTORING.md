# Two SOLID Principles Implemented
## 1. Single Responsibility Principle (SRP)
**Definition:** A class should have only one reason to change.

**Why I Chose SRP**

In Project 1, the application consisted of four separate scripts (getdata.py, preprocess.py, embedding.py, similarity.py), each executed manually by the user. While these scripts were already somewhat separated by function, there was no clear orchestration layer, and no class structure to demonstrate SRP.

**How I Implemented SRP**

I created a JobMatcher class whose single responsibility is to orchestrate the workflow. 

- ```job_matcher.py```
``` python
class JobMatcher:
    """
    Single Responsibility: Coordinates the workflow only.
    Does NOT do fetching, preprocessing, embedding, or similarity calculations.
    """
    
    def run_full_pipeline(self):
        """Orchestrates the pipeline by calling existing script"""
        steps = [
            ("Fetching jobs from Adzuna...", "src/getdata.py"),
            ("Preprocessing data...", "src/preprocess.py"),
            ("Generating embeddings...", "src/embedding.py"),
            ("Calculating similarities...", "src/similarity.py")
        ]
        
        for step_name, script in steps:
            print(f"\n{step_name}")
            subprocess.run([sys.executable, script], check=True)
```


## 2. Dependency Inversion Principle (DIP)
**Definition:**  High-level modules should not depend on low-level modules. Both should depend on abstractions.