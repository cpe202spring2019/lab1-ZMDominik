import unittest
from lab1 import max_list_iter as m
from lab1 import reverse_rec as r
from lab1 import bin_search as b

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter_none_list(self):
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            m(tlist)

    def test_max_list_iter_neg_list(self):
        tlist = [-30, -14, -12, -55]
        self.assertEqual(m(tlist), -12)

    def test_max_list_iter_pos_list(self):
        tlist = [20, 29, 7, 33, 7]
        self.assertEqual(m(tlist), 33)

    def test_max_list_iter_mult_max_val(self):
        tlist = [15, 22, 22]
        self.assertEqual(m(tlist), 22)

    def test_max_list_iter_all_same_num(self):
        tlist = [3, 3, 3]
        self.assertEqual(m(tlist), 3)

    def test_max_list_iter_empty_list(self):
        self.assertEqual(m([]), None)

    def test_reverse_rec_odd_len(self):
        self.assertEqual(r([1, 2, 3]), [3, 2, 1])

    def test_reverse_rec_even_len(self):
        self.assertEqual(r([1, 2, 3, 4]), [4, 3, 2, 1])

    def test_reverse_rec_none_list(self):
        tlist = None
        with self.assertRaises(ValueError):
            r(tlist)

    def test_reverse_rec_empty_list(self):
        self.assertEqual(r([]), [])

    def test_bin_search_no_repeats_in_list(self):
        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]
        self.assertEqual(b(4, 0, len(list_val)-1, list_val), 4)

    def test_bin_search_two_in_list(self):
        tlist = [0, 1, 2, 3, 3, 4, 5]
        self.assertEqual(b(3, 0, len(tlist)-1, tlist), 3)

    def test_bin_search_val_error(self):
        tlist = None
        with self.assertRaises(ValueError):
            b(1, 0, 2, tlist)

    def test_bin_search_no_val(self):
        tlist = [0, 2, 3, 4, 5, 6]
        self.assertEqual(b(1, 0, len(tlist)-1, tlist), None)

    def test_bin_search_empty_list(self):
        tlist = []
        self.assertEqual(b(1, 0, 1, tlist), None)


if __name__ == "__main__":
        unittest.main()

    
