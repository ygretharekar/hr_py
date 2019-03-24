"""
https://www.hackerrank.com/challenges/encryption/problem
"""

class Encryption:
    """
        solving
    """
    def solution(self):
        """solution"""
        inp_str = input().replace(" ", "")
        import math
        l_b = math.floor(math.sqrt(len(inp_str)))
        u_b = math.ceil(math.sqrt(len(inp_str)))

        if l_b*u_b < len(inp_str):
            l_b = u_b

        ans = ["" for i in range(u_b)]

        for i in range(u_b):
            ans[i] = ans[i] + inp_str[i::u_b]
        ret = " ".join(ans)

        print(ret)
