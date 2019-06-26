from unittest import TestCase
from ..maximum_palindromes import MaximumPalindromes


class TestMaximumPalindromes(TestCase):
    def test_initialize(self):
        self.fail()

    def test_solution(self):
        s = ''

        mp = MaximumPalindromes()

        # mp.initialize(s)

        ans = []

        with open("strings\\medium\\tests\\test_cases\\maximum_palindromes_tc22_input.txt") \
                as i_file:
            inp = i_file.readline()
            s = inp.strip()
            mp.initialize(s)
            i_file.readline()
            inp = i_file.readline()
            while inp:
                l, r = map(int, inp.split())
                ans.append(mp.solution(l, r))
                inp = i_file.readline()

        with open("strings\\medium\\tests\\test_cases\\maximum_palindromes_tc22_output.txt") \
                as o_file:
            out = o_file.readlines()

        out = list(map(lambda x: int(x.strip()), out))

        not_equal = [i[0] for i, j in zip(enumerate(out), enumerate(ans)) if i[1] != j[1]]

        self.assertSequenceEqual(out, ans, "failed")
