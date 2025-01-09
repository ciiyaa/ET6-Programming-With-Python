import unittest

from ..sort_and_merge import sort_and_merge


class TestSortAndMerge(unittest.TestCase):
    """ """

    def test_minimal_input(self):
        """"""
        self.assertEqual(sort_and_merge([], []), [])
