"""
https://www.hackerrank.com/challenges/the-time-in-words/problem
"""
class TheTimeInWords:
    "solution"

    def solution(self, a_1, a_2):
        "time in words"
        numbers = (
            "zero",
            "one",
            "two",
            "three",
            "four",
            "five",
            "six",
            "seven",
            "eight",
            "nine",
            "ten",
            "eleven",
            "twelve",
            "thirteen",
            "fourteen",
            "fifteen",
            "sixteen",
            "seventeen",
            "eighteen",
            "nineteen",
            "twenty",
            "twenty one",
            "twenty two",
            "twenty three",
            "twenty four",
            "twenty five",
            "twenty six",
            "twenty seven",
            "twenty eight",
            "twenty nine"
        )

        if a_2 == 0:
            return numbers[a_1] + " o' clock"

        elif a_2 == 1:
            return "one minute past " + numbers[a_1]

        elif a_2 == 30:
            return "half past " + numbers[a_1]


        elif a_2 == 59:
            return "one minute to " + numbers[a_1+1]

        elif a_2 == 45:
            return "quarter to " + numbers[a_1+1]

        elif a_2 == 15:
            return "quarter past " + numbers[a_1]

        elif a_2 < 30:
            return numbers[a_2] + " minutes past " + numbers[a_1]

        elif a_2 > 30:
            return numbers[60-a_2] + " minutes to " + numbers[a_1+1]
