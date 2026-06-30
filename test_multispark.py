# test_multispark.py
"""
Tests for MultiSpark module.
"""

import unittest
from multispark import MultiSpark

class TestMultiSpark(unittest.TestCase):
    """Test cases for MultiSpark class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MultiSpark()
        self.assertIsInstance(instance, MultiSpark)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MultiSpark()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
