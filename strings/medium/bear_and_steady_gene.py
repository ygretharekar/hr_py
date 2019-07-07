"""docstring"""


class BearAndSteadyGene:
    """docstring"""
    def solution(self, gene):
        """docstring"""

        gene_length = len(gene)

        cnt = {'A': 0, 'C': 0, 'G':0, 'T': 0}

        min_length = gene_length - 1

        j_out = 0

        for j,  letter in enumerate(gene[::-1]):
            if cnt[letter] == gene_length // 4:
                break

            cnt[letter] = cnt[letter] + 1
            j_out = j

        j = gene_length - j_out - 1

        min_length = j

        for i, letter in enumerate(gene):
            cnt[letter] = cnt[letter] + 1

            while j < gene_length and cnt[letter] > gene_length // 4:
                pass

        return min_length
