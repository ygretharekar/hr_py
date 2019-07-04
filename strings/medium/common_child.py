"""docstring"""


class CommonChild:
    """docstring"""
    def solution(self, a_str, b_str):
        """docstring"""
        # d_p = [[0] * (len(a_str) + 1)  for __ in range(len(b_str) + 1)]
        d_p = [[0] * (len(a_str) + 1)  for _ in range(2)]

        for i in range(len(a_str)):
            a_0 = i % 2
            a_1 = (i + 1) % 2

            for j in range(len(b_str)):
                if a_str[i] == b_str[j]:
                    d_p[a_1][j + 1] = d_p[a_0][j] + 1
                else:
                    d_p[a_1][j + 1] = max(d_p[a_0][j + 1], d_p[a_1][j])

        return d_p[(i + 1) % 2][-1]
