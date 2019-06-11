"""https://www.hackerrank.com/challenges/richie-rich/problem"""


class HighestValuePalindrome:
    """Solution"""
    @staticmethod
    def solution(s, n, k):
        min_changes = 0
        for i, j in zip(s, s[::-1]):
            if i != j:
                min_changes += 1

        min_changes //= 2

        if min_changes > k:
            return '-1'

        double_change = k - min_changes

        i = 0
        j = len(s) - 1
        ans = s

        while i <= j:

            if s[i] != s[j]:
                c = max(s[i], s[j])
                if c != '9' and double_change > 0:
                    ans = ans[:i] + '9' + ans[i+1:]
                    ans = ans[:j] + '9' + ans[j+1:]
                    double_change -= 1

                else:
                    ans = ans[:i] + c + ans[i+1:]
                    ans = ans[:j] + c + ans[j+1:]

            else:
                if s[i] != '9' and double_change - 2 >= 0:
                    ans = ans[:i] + '9' + ans[i+1:]
                    ans = ans[:j] + '9' + ans[j+1:]
                    double_change -= 2

            i += 1
            j -= 1

        return ans
