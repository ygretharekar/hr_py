"""docstring"""


class BearAndSteadyGene:
    """docstring"""
    def solution(self, gene):
        """docstring"""
        gene_prime = {
            'A': 2,
            'C': 3,
            'T': 5,
            'G': 7
        }

        from functools import reduce

        ans = reduce(lambda a, x: a * gene_prime[x], gene, 1)

        l_4 = len(gene) // 4

        if ans % (2 ** l_4) != 0:
            pass

        return ans
