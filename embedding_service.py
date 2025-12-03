"""Concrete implementation of IEmbeddingService using OpenAI."""
from typing import List
from openai import OpenAI #type: ignore
from interfaces import IEmbeddingService
import os
from dotenv import load_dotenv #type: ignore
load_dotenv()


class OpenAIEmbeddingService(IEmbeddingService):
    def __init__(self, api_key: str, model: str = "text-embedding-3-small"):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model = model
    
    def get_embedding(self, text: str) -> List[float]:
        response = self.client.embeddings.create(
            model=self.model,
            input=text
        )
        return response.data[0].embedding