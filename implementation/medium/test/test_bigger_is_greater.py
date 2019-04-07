"""test bigger is greater"""
from .. import bigger_is_greater

def test_solution():
    """Test solution"""
    b_g = bigger_is_greater.BiggerIsGreater()
    my_list = []
    ans_list = []
    with open('implementation\\medium\\test\\bigger_is_greater_test_cases'
              +'\\bigger_is_greater_input.txt', 'r') as f_1:
        line = f_1.readline()
        while line:
            my_list.append(b_g.solution(line.strip()))
            line = f_1.readline()

    with open('implementation\\medium\\test\\bigger_is_greater_test_cases'
              +'\\bigger_is_greater_output.txt', 'r') as f_2:
        line = f_2.readline()
        while line:
            ans_list.append(line.strip())
            line = f_2.readline()

    assert all([i == j for i, j in zip(my_list, ans_list)])
