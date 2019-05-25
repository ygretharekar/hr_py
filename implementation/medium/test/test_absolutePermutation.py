from unittest import TestCase
from .. import absolute_permutation


class TestAbsolutePermutation(TestCase):
    def test_solution(self):
        # assert absolute_permutation.AbsolutePermutation.solution(10, 1) == [2, 1, 4, 3, 6, 5, 8, 7, 10, 9]
        # assert absolute_permutation.solution(8, 2) == [3, 4, 1, 2, 7, 8, 5, 6]
        assert absolute_permutation.solution(10, 3) == [-1]
