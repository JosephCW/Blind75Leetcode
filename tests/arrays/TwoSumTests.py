import unittest

from arrays.TwoSum import TwoSum


class TwoSumTests(unittest.TestCase):
    def test_given_valid_params_valid_answer_returned(self):
        ts = TwoSum()
        self.assertIn(ts.two_sum([1, 4, 7, 9, 2], 16), ([2, 3], [3, 2]))
        self.assertIn(ts.two_sum([2, 7, 11, 15], 9), ([0, 1], [1, 0]))
        self.assertIn(ts.two_sum([3, 2, 4], 6), ([1, 2], [2, 1]))
        self.assertIn(ts.two_sum([3, 3], 6), ([0, 1], [1, 0]))

    def test_given_same_index_twice_fail(self):
        ts = TwoSum()
        self.assertEqual(ts.two_sum([1, 3, 5], 2), None)
