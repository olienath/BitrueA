# test_bitrueapi.py
"""
Tests for BitrueAPI module.
"""

import unittest
from bitrueapi import BitrueAPI

class TestBitrueAPI(unittest.TestCase):
    """Test cases for BitrueAPI class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BitrueAPI()
        self.assertIsInstance(instance, BitrueAPI)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BitrueAPI()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
