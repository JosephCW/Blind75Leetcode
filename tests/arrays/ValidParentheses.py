import unittest

from arrays.ValidParentheses import ValidParentheses


class ValidParenthesesTests(unittest.TestCase):
    def test_given_non_matching_close_then_false(self):
        vp = ValidParentheses()
        self.assertFalse(vp.isValid('(]'))

    def test_given_valid_parens_then_true(self):
        vp = ValidParentheses()
        self.assertTrue(vp.isValid('()'))
        self.assertTrue(vp.isValid('[]'))
        self.assertTrue(vp.isValid('{}'))

    def test_given_staggered_parens_then_false(self):
        vp = ValidParentheses()
        self.assertFalse(vp.isValid('{[}]'))

    def test_given_nested_parens_then_true(self):
        vp = ValidParentheses()
        self.assertTrue(vp.isValid('{{{}}}'))
        self.assertTrue(vp.isValid('[{[]}]'))
        self.assertTrue(vp.isValid('([{}])'))

    def test_given_multiple_pairs_then_true(self):
        vp = ValidParentheses()
        self.assertTrue(vp.isValid('{}[({})()]()'))

