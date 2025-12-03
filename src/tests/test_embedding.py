import unittest
import sys
import os
from typing import List

sys.path.insert(0, '/home')

from interfaces import IEmbeddingService


class MockEmbeddingService(IEmbeddingService):
    """Mock embedding service for testing without API calls."""
    
    def get_embedding(self, text: str) -> List[float]:
        length = len(text)
        return [0.1 * (i + length % 10) for i in range(5)]


class TestEmbeddingService(unittest.TestCase):
    """Test the embedding functionality using mocks."""
    
    def setUp(self):
        self.mock_service = MockEmbeddingService()
    
    def test_mock_embedding_returns_list(self):
        result = self.mock_service.get_embedding("test text")
        
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)
    
    def test_mock_embedding_no_api_call(self):
        embedding1 = self.mock_service.get_embedding("Software Engineer")
        embedding2 = self.mock_service.get_embedding("Data Scientist")
        
        self.assertEqual(len(embedding1), 5)
        self.assertEqual(len(embedding2), 5)
        self.assertNotEqual(embedding1, embedding2)
    
    def test_empty_string_embedding(self):
        result = self.mock_service.get_embedding("")
        
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 5)
    
    def test_embedding_values_are_floats(self):
        result = self.mock_service.get_embedding("test")
        
        for value in result:
            self.assertIsInstance(value, float)
    
    def test_long_text_embedding(self):
        long_text = "This is a very long text " * 100
        result = self.mock_service.get_embedding(long_text)
        
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 5)
    
    def test_special_characters_embedding(self):
        special_text = "Hello, World! @#$%^&*() 123"
        result = self.mock_service.get_embedding(special_text)
        
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 5)
    
    def test_embedding_consistency(self):
        text = "Consistent text"
        embedding1 = self.mock_service.get_embedding(text)
        embedding2 = self.mock_service.get_embedding(text)
        
        self.assertEqual(embedding1, embedding2)
    
    def test_embedding_dimension(self):
        texts = ["short", "medium length text", "very long text with many words here"]
        
        for text in texts:
            result = self.mock_service.get_embedding(text)
            self.assertEqual(len(result), 5, f"Failed for text: {text}")


if __name__ == "__main__":
    unittest.main()