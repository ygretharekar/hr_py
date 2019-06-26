"""docstring"""


class MaximumPalindromes:
    """docstring"""
    str_case = ""
    facts = [1]
    inv = [1, 1]
    inv_facts = [1]
    odds = [0]
    alpha_count = [[0] * 26]
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    i = 0

    def initialize(self, tr_case):
        """docstring"""

        mod = 10 ** 9 + 7

        self.str_case = tr_case

        cur = 0
        for ch_ar in tr_case:
            tmp = [i for i in self.alpha_count[-1]]
            tmp[self.alpha.find(ch_ar)] += 1
            self.alpha_count.append(tmp)
            cur ^= (1 << self.alpha.find(ch_ar))
            self.odds.append(cur)

        for i in range(2, len(tr_case) + 1):
            self.inv.append((mod - mod // i * self.inv[mod % i] % mod) % mod)

        cur = 1
        for i in range(1, len(tr_case) + 1):
            cur *= i
            cur %= mod
            self.facts.append(cur)
            self.inv_facts.append((self.inv_facts[-1] * self.inv[i]) % mod)

    #pylint: disable-msg=too-many-locals
    def solution(self, left, right):
        """docstring"""

        mod = 10 ** 9 + 7

        odd = self.odds[left - 1] ^ self.odds[right]

        multi = 0
        for chara in range(26):
            if odd & (1 << chara):
                multi += 1

        letters = [(self.alpha_count[right][i] - self.alpha_count[left - 1][i]) // 2
                   for i in range(26)]

        addition = 0
        dividend = 1

        for i in letters:
            addition += i
            dividend = (dividend * self.inv_facts[i]) % mod

        multi = max(multi, 1)

        sol = (multi * (self.facts[addition] * dividend)) % mod

        self.i += 1

        return sol
