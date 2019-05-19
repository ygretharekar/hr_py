"""https://www.hackerrank.com/challenges/absolute-permutation/problem"""
from typing import List


class AbsolutePermutation:
    """Solution"""
    pass


def solution(n, k):
    """solution"""

    if not k:
        return [i + 1 for i in range(n)]

    if n % 2:
        return [-1]

    elif n % k != 0 or (n // k) % 2:
        return [-1]

    elif k > n / 2:
        return [-1]

    else:

        ans_list: List[int] = [i + 1 for i in range(n)]

        for i in range(0, n - k, k * 2):
            for j in range(i, i + k):
                ans_list[j], ans_list[j + k] = ans_list[j + k], ans_list[j]

        return ans_list
