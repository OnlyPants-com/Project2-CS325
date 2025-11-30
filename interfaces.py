"""
Abstract interfaces for Dependency Inversion Principle (DIP).
"""
from abc import ABC, abstractmethod
from typing import List


class IEmbeddingService(ABC):
    """Abstract interface for embedding services."""
    
    @abstractmethod
    def get_embedding(self, text: str) -> List[float]:
        pass