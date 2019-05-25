"test for the grid search"
from .. import the_grid_search


def test_solution():
    "test solution"
    grid_search = the_grid_search.GridSearch()
    grid = []

    pattern = []

    with open('implementation\\medium\\test\\the_grid_search_test_cases'
              + '\\the_grid_search_input.txt', 'r') as f_1:
        line = f_1.readline()
        while line:
            grid.append(str(line).strip())
            line = f_1.readline()

    with open('implementation\\medium\\test\\the_grid_search_test_cases'
              + '\\the_grid_search_input2.txt', 'r') as f_2:
        line = f_2.readline()
        while line:
            pattern.append(str(line).strip())
            line = f_2.readline()

    assert grid_search.solution(grid, pattern) == "YES"
