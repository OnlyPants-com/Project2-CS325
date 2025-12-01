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

This allows orchestration with what to run vs how to run it. Each script keeps its single responsibility, while still having the JobMatcher change.


## 2. Dependency Inversion Principle (DIP)
**Definition:**  High-level modules should not depend on low-level modules. Both should depend on abstractions.

**Why I Chose DIP**
The original embedding.py had a hard-coded dependency on the OpenAI API. This created critical problems.

- Original Code:

``` python
# embedding.py
from openai import OpenAI

#Can't swap providers, can't test without API
client = OpenAI(api_key="sk-proj-...")

def get_embedding(text: str):
    # Directly calling OpenAI
    response = client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=text
    )
    return response.data[0].embedding
```

**How I Implemented DIP**
Used 3 steps:
1. Created absraction (```interfaces.py```)
``` python
from abc import ABC, abstractmethod
from typing import List

class IEmbeddingService(ABC):
    """
    Abstract interface for embedding services.
    This is the ABSTRACTION that high-level code depends on.
    """
    
    @abstractmethod
    def get_embedding(self, text: str) -> List[float]:
        """Generate an embedding vector for the given text."""
        pass
```

2. Created Concrete Implementation of OpenAI (```embedding_service.py```)
``` python
from openai import OpenAI
from interfaces import IEmbeddingService

class OpenAIEmbeddingService(IEmbeddingService):
    """
    Implements the abstraction using OpenAI's API.
    """
    
    def __init__(self, api_key: str, model: str = "text-embedding-3-small"):
        self.client = OpenAI(api_key=api_key)
        self.model = model
    
    def get_embedding(self, text: str) -> List[float]:
        response = self.client.embeddings.create(
            model=self.model,
            input=text
        )
        return response.data[0].embedding
```

3. Modified High-Level Code to Depend on Abstraction (```embedding.py```)

BEFORE:
``` python
from openai import OpenAI

# Direct dependency on concrete OpenAI class - BAD!
client = OpenAI(api_key="sk-proj-...")

def get_embedding(text: str):
    # Tightly coupled to OpenAI
    response = client.embeddings.create(...)
    return response.data[0].embedding
```

AFTER:
``` python
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from embedding_service import OpenAIEmbeddingService

# Dependency injection - inject the concrete service
embedding_service = OpenAIEmbeddingService(
    api_key=API_KEY,
    model="text-embedding-3-small"
)

def get_embedding(text: str):
    # Now depends on IEmbeddingService interface (via embedding_service)
    return embedding_service.get_embedding(text)
```