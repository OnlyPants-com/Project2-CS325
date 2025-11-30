"""
Unit tests demonstrating mocking of the embedding service.
"""
import unittest
import sys
import os
from typing import List

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from interfaces import IEmbeddingService


class MockEmbeddingService(IEmbeddingService):
    """Mock embedding service for testing without API calls."""
    
    def get_embedding(self, text: str) -> List[float]:
        length = len(text)
        return [0.1 * (i + length % 10) for i in range(5)]


class TestEmbeddingService(unittest.TestCase):
    """Test the embedding functionality using mocks."""
    
    def test_mock_embedding_returns_list(self):
        mock_service = MockEmbeddingService()
        result = mock_service.get_embedding("test text")
        
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)
    
    def test_mock_embedding_no_api_call(self):
        mock_service = MockEmbeddingService()
        
        embedding1 = mock_service.get_embedding("Software Engineer")
        embedding2 = mock_service.get_embedding("Data Scientist")
        
        self.assertEqual(len(embedding1), 5)
        self.assertEqual(len(embedding2), 5)
        self.assertNotEqual(embedding1, embedding2)


if __name__ == "__main__":
    unittest.main()