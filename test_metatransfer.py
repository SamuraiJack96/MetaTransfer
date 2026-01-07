# test_metatransfer.py
"""
Tests for MetaTransfer module.
"""

import unittest
from metatransfer import MetaTransfer

class TestMetaTransfer(unittest.TestCase):
    """Test cases for MetaTransfer class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MetaTransfer()
        self.assertIsInstance(instance, MetaTransfer)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MetaTransfer()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
