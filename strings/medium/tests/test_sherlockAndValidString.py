from unittest import TestCase
from ..sherlock_and_valid_strings import SherlockAndValidString


class TestSherlockAndValidString(TestCase):
    def test_solution(self):
        ans = SherlockAndValidString.solution("aaaaabc")
        self.assertEqual("NO", ans, "Failed")
