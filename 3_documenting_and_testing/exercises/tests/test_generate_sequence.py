import unittest

from ..generate_sequence import generate_sequence


class TestGenerateSequence(unittest.TestCase):
    """ """

    def test_minimal_input(self):
        """"""
        self.assertEqual(generate_sequence(0), [])
