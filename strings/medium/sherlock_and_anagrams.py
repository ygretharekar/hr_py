"""docstring"""


class SherlockAndAnagrams:
    """docstring"""
    def solution(self, string):
        """docstring"""

        prime_nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
                      43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]

        str_len = len(string)

        from collections import defaultdict
        ana_dict = defaultdict(int)

        for length in range(1, str_len + 1):
            for i in range(str_len - length + 1):
                j = i + length
                key = 1
                for k in range(i, j):
                    key = key * prime_nums[ord(string[k]) - ord('a')]
                ana_dict[key] += 1

        ans = sum([i * (i - 1) // 2 for i in ana_dict.values() if i > 1])

        return ans
