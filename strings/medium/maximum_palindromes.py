class MaximumPalindromes:
    s = ""

    def initialize(self, s):
        self.s = s

    def solution(self, l, r):
        string = self.s
        s_str = string[l - 1:r]
        from collections import Counter

        mod = 10 ** 9 + 7

        let_cnt = Counter(s_str)

        max_odd = 0

        max_odd_letters = []

        for i in let_cnt:
            if let_cnt[i] % 2 == 1:
                if max_odd < let_cnt[i]:
                    max_odd = let_cnt[i]
                max_odd_letters.append(i)

        # even_let = {k: v for k, v in let_cnt.items() if v % 2 == 0}
        even_let = {k: v if v % 2 == 0 else v - 1 for k, v in let_cnt.items()}

        def get_fact(n):
            # if n > 0:
            #     return n*get_fact(n - 1)
            # else:
            #     return 1
            ans = 1
            if n > 1:
                for j in range(1, n + 1):
                    ans *= j

            return ans

        addition = 0
        dividend = 1

        for i in even_let.values():
            addition += i // 2
            dividend *= get_fact(i // 2)

        # addition += max_odd - 1 if max_odd > 0 else 0
        # dividend *= get_fact(max_odd - 1)

        multi = len(max_odd_letters) if max_odd > 0 else 1

        sol = (multi * (get_fact(addition) // dividend)) % mod

        return sol
