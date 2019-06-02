from unittest import TestCase
from ..emas_supercomputer import EmaSupercomputer


class TestEmaSupercomputer(TestCase):
    def test_within_range(self):
        self.fail()

    def test_solution(self):
        # grid = [
        #     'BBBGBBGBBG',
        #     'BBGGGBGBBG',
        #     'BBBGBBGBBG',
        #     'BBBGGGGGGG',
        #     'BBBGBBGBBG',
        #     'BBBGBBGBBG',
        #     'BBBGBBGBBG',
        #     'BBBBBBBBBB',
        # ]

        # grid = [
        #     'BBBBBGBGBBB',
        #     'BBGBBGBBGBB',
        #     'BGGGGGGGGGB',
        #     'BBGBBGBBGBB',
        #     'BBBBBGBBBBB'
        # ]

        # grid = [
        #     'BBBBBGGBGG',
        #     'GGGGGGGGGG',
        #     'GGGGGGGGGG',
        #     'BBBBBGGBGG',
        #     'BBBBBGGBGG',
        #     'GGGGGGGGGG',
        #     'BBBBBGGBGG',
        #     'GGGGGGGGGG',
        #     'BBBBBGGBGG',
        #     'GGGGGGGGGG',
        # ]

        # grid = [
        #     'GBGBGGB',
        #     'GBGBGGB',
        #     'GBGBGGB',
        #     'GGGGGGG',
        #     'GGGGGGG',
        #     'GBGBGGB',
        #     'GBGBGGB',
        # ]

        # grid = [
        #     'GGGGGGGG',
        #     'GBGBGGBG',
        #     'GBGBGGBG',
        #     'GGGGGGGG',
        #     'GBGBGGBG',
        #     'GGGGGGGG',
        #     'GBGBGGBG',
        #     'GGGGGGGG',
        # ]

        # grid = [
        #     'GBBGGBGGBBGGGB',
        #     'GBBGGBGGBBGGGB',
        #     'GBBGGBGGBBGGGB',
        #     'GBBGGBGGBBGGGB',
        #     'GGGGGGGGGGGGGG',
        #     'GBBGGBGGBBGGGB',
        #     'GGGGGGGGGGGGGG',
        #     'GBBGGBGGBBGGGB',
        #     'GBBGGBGGBBGGGB',
        #     'GGGGGGGGGGGGGG',
        #     'GGGGGGGGGGGGGG',
        #     'GGGGGGGGGGGGGG',
        #     'GBBGGBGGBBGGGB',
        # ]

        grid = [
            'GGGGGGGGGGGG',
            'GBGGBBBBBBBG',
            'GBGGBBBBBBBG',
            'GGGGGGGGGGGG',
            'GGGGGGGGGGGG',
            'GGGGGGGGGGGG',
            'GGGGGGGGGGGG',
            'GBGGBBBBBBBG',
            'GBGGBBBBBBBG',
            'GBGGBBBBBBBG',
            'GGGGGGGGGGGG',
            'GBGGBBBBBBBG',
        ]

        ans = EmaSupercomputer.solution(grid)

        # self.assertEqual(45, ans, "Failed") tc 3
        # self.assertEqual(81, ans, "Failed")  # tc 5
        # self.assertEqual(85, ans, "Failed")  # tc 10
        # self.assertEqual(225, ans, "Failed")  # tc 10
        self.assertEqual(81, ans, "Failed")  # tc 10
