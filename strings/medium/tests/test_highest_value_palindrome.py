from unittest import TestCase
from ..highest_value_palindrome import HighestValuePalindrome


class TestHighestValuePalindrome(TestCase):

    def test_solution(self):
        inp = ''
        output = ''

        with open('strings\\medium\\tests\\test_cases' +
                  '\\tc10_highest_value_palindrome.txt') as file:
            inp = file.read()
            inp.strip()

        with open('strings\\medium\\tests\\test_cases' +
                  '\\op10_highest_value_palindrome.txt') as file:
            output = file.read()
            output.strip()

        # 77543 58343

        ans = HighestValuePalindrome.solution(inp, 77543, 58343)

        with open('strings\\medium\\tests\\test_cases' +
                  '\\myop10_highest_value_palindrome.txt', 'w+') as file:
            file.write(ans)

        self.assertEqual(output, ans, "failed")
