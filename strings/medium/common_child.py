"""docstring"""


class CommonChild:
    """docstring"""
    def solution(self, a_str, b_str):
        """docstring"""
        d_p = [[0 for _ in range(len(a_str) + 1)] for __ in range(len(b_str) + 1)]



        for i, x_char in enumerate(a_str):
            for j, y_char in enumerate(b_str):
                if x_char == y_char:
                    d_p[i + 1][j + 1] = d_p[i][j] + 1
                else:
                    d_p[i + 1][j + 1] = max(d_p[i][j + 1], d_p[i + 1][j])

        return d_p[-1][-1]
