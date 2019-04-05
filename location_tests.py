import unittest
from location import Location

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc), "Location('SLO', 35.3, -120.7)")

        loc2 = Location("Paris", 48.9, 2.4)
        self.assertEqual(repr(loc2), "Location('Paris', 48.9, 2.4)")

    def test_eq_wrong_type(self):
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = 3
        self.assertFalse(loc1 == loc2)

    def test_eq_wrong_name(self):
        loc1 = Location("SLO",35.3, -120.7)
        loc2 = Location("Obispo", 35.3, -120.7)
        self.assertFalse(loc1 == loc2)

    def test_eq_wrong_lat(self):
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location("SLO", 50, -120.7)
        self.assertFalse(loc1 == loc2)

    def test_eq_wrong_lon(self):
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location("SLO", 35.3, -1.7)
        self.assertFalse(loc1 == loc2)

    def test_eq_all_right(self):
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location("SLO", 35.3, -120.7)
        self.assertTrue(loc1 == loc2)

    def test_eq_all_wrong(self):
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location("Paris", 48.9, 2.4)
        self.assertFalse(loc1 == loc2)

if __name__ == "__main__":
        unittest.main()
