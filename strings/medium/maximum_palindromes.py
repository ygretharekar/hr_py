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

        # def get_pow(num, power):
        #     """docstring"""
        #     # num %= mod
        #     res = 1
        #     while power > 0:
        #         if power & 1:
        #             res = (res * num) % mod

        #         num = (num * num) % mod

        #         power >>= 1
        #     return res

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

        print("start")

        cur = 1
        for i in range(1, len(tr_case) + 1):
            cur *= i
            cur %= mod
            self.facts.append(cur)
            # self.inv_facts.append(get_pow(self.facts[i], mod - 2))
            self.inv_facts.append((self.inv_facts[-1] * self.inv[i]) % mod)
            print(f"{i} : {self.inv_facts[i]}")

    #pylint: disable-msg=too-many-locals
    def solution(self, left, right):
        """docstring"""
        # string = self.str_case
        # s_str = string[left - 1:right]
        # from collections import Counter

        mod = 10 ** 9 + 7

        # let_cnt = Counter(s_str)

        # max_odd = 0

        # max_odd_letters = []

        # for i in let_cnt:
        #     if let_cnt[i] % 2 == 1:
        #         if max_odd < let_cnt[i]:
        #             max_odd = let_cnt[i]
        #         max_odd_letters.append(i)

        # even_let = {k: v for k, v in let_cnt.items() if v % 2 == 0}
        # even_let = {k: v if v % 2 == 0 else v - 1 for k, v in let_cnt.items()}

        # facts = [1]

        # inv_facts = [get_pow(1, mod - 2)]

        # def get_fact(num):
        #     """aaa"""
        #     # if num > 0:
        #     #     return num*get_fact(num - 1)
        #     # else:

        #     #     return 1
        #     ans = 1
        #     if num > 1:
        #         for j in range(1, num + 1):
        #             ans *= j

        #     return ans

        odd = self.odds[left - 1] ^ self.odds[right]

        multi = 0
        for chara in range(26):
            if odd & (1 << chara):
                multi += 1

        letters = [(self.alpha_count[right][i] - self.alpha_count[left - 1][i]) // 2
                   for i in range(26)]

        addition = 0
        dividend = 1

        # for i in even_let.values():
        for i in letters:
            addition += i
            dividend = (dividend * self.inv_facts[i]) % mod

        # addition += max_odd - 1 if max_odd > 0 else 0
        # dividend *= get_fact(max_odd - 1)

        # multi = len(max_odd_letters) if max_odd > 0 else 1

        multi = max(multi, 1)

        sol = (multi * (self.facts[addition] * dividend)) % mod

        self.i += 1

        print(f"ans {self.i}: {sol}")

        return sol
