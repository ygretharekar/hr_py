import io
from unittest import TestCase, mock
from ..almost_sorted import AlmostSorted


class TestAlmostSorted(TestCase):

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, n, expected_output, mock_stdout):
        AlmostSorted.solution(n)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_solution(self):
        arr = [1, 5, 4, 3, 2, 6]
        self.assert_stdout(arr, 'yes\nreversed 1 4')
