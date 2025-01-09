import unittest

from ..generate_incremental_sequence import generate_incremental_sequence


class TestGenerateIncrementalSequence(unittest.TestCase):
    """ """

    def test_minimal_input(self):
        """"""
        self.assertEqual(generate_incremental_sequence(0, 0), [])
