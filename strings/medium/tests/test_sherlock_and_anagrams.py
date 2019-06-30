"""docstring"""

from unittest import TestCase
from ..sherlock_and_anagrams import SherlockAndAnagrams


class TestSherlockAndAnagrams(TestCase):
    """docstring"""
    def test_solution(self):
        """docstring"""
        sher_ana = SherlockAndAnagrams()
        string = "abba"
        ans = sher_ana.solution(string)
        self.assertEqual(4, ans, "failed")
