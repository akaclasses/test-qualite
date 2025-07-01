import unittest
import sys
import os

# Ajouter le dossier src au path pour importer nos modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from calculator import calculate_discount, get_tax_amount

class TestCalculator(unittest.TestCase):
    
    def test_premium_customer_high_price(self):
        """Test client premium avec prix élevé"""
        result = calculate_discount(1500, "premium")
        expected = 1500 * 0.2  # 20% de remise
        self.assertEqual(result, expected)
    
    def test_premium_customer_low_price(self):
        """Test client premium avec prix bas"""
        result = calculate_discount(500, "premium")
        expected = 500 * 0.1  # 10% de remise
        self.assertEqual(result, expected)
    
    def test_regular_customer(self):
        """Test client régulier"""
        result = calculate_discount(800, "regular")
        expected = 800 * 0.05  # 5% de remise
        self.assertEqual(result, expected)
    
    def test_unknown_customer_type(self):
        """Test type de client inconnu"""
        result = calculate_discount(1000, "unknown")
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()