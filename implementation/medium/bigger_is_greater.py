"""
https://www.hackerrank.com/challenges/bigger-is-greater/problem
"""

class BiggerIsGreater:
    """
    solution
    """
    def solution(self, w_s):
        """solution"""
        w_s = list(w_s)
        length = len(w_s)
        i = length - 1
        while i > 0 and w_s[i - 1] >= w_s[i]:
            i -= 1

        if i <= 0:
            return "no answer"

        j = length - 1

        while w_s[j] <= w_s[i-1]:
            j -= 1

        w_s[i-1], w_s[j] = w_s[j], w_s[i-1]

        w_s[i:] = w_s[length-1:i-1:-1]

        return "".join(w_s)

    def editorial_solution(self, w_s):
        """
        solution from editorial
        """
        word = list(w_s.strip())
        start = -1
        for i in range(0, len(word) - 1):
            if word[i] < word[i + 1]:
                start = i

        if start == -1:
            return "no answer"

        end = -1
        for j in range(start + 1, len(word)):
            if word[start] < word[j]:
                end = j

        word[start], word[end] = word[end], word[start]
        a_c = word[start + 1:]
        a_c.sort()

        for j in range(start + 1, len(word)):
            word[j] = a_c[j - start - 1]

        return "".join(word)
