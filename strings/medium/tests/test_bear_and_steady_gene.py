"""docstring"""

from unittest import TestCase
from ..bear_and_steady_gene import BearAndSteadyGene as BG


class TestSherlockAndAnagrams(TestCase):
    """docstring"""
    def test_solution(self):
        """docstring"""
        b_g = BG()
        gene = "GAAATAAA"

        ans = b_g.solution(gene)

        self.assertEqual(5, ans, "failed")
