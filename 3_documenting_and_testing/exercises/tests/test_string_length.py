import unittest

from ..string_length import string_length

class TestStringLength(unittest.TestCase):
    """ """

    def test_minimal_list_input(self):
        """"""
        self.assertEqual(string_length([]), None)

    def test_minimal_string_input(self):
        """"""
        self.assertEqual(string_length(''), None)
