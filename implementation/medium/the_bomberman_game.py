"""https://www.hackerrank.com/challenges/bomber-man/problem"""


def find_nearby_bombs(grid, i, j):
    rows = len(grid)
    cols = len(grid[0])

    ans = False

    if i-1 >= 0:
        ans = ans or grid[i - 1][j] == 'O'

    if i + 1 < rows:
        ans = ans or grid[i + 1][j] == 'O'

    if j - 1 >= 0:
        ans = ans or grid[i][j - 1] == 'O'

    if j + 1 < cols:
        ans = ans or grid[i][j + 1] == 'O'

    return ans


def solution(n_time, grid):
    """solution"""

    if n_time == 1:
        return grid

    if n_time % 2 == 0:
        return ["".join(['O' for _ in i]) for i in grid]

    new_grid = [['O' for _ in i] for i in grid]

    # breakpoint()

    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            lev1 = False
            lev2 = False

            if cell == ".":
                lev1 = find_nearby_bombs(grid, i, j)

                if lev1:
                    rows = len(grid)
                    cols = len(grid[0])

                    if i-1 >= 0 and grid[i-1][j] != 'O':
                        lev2 = lev2 or not find_nearby_bombs(grid, i - 1, j)

                    if i + 1 < rows and grid[i+1][j] != 'O':
                        lev2 = lev2 or not find_nearby_bombs(grid, i + 1, j)

                    if j - 1 >= 0 and grid[i][j - 1] != 'O':
                        lev2 = lev2 or not find_nearby_bombs(grid, i, j - 1)

                    if j + 1 < cols and grid[i][j + 1] != 'O':
                        lev2 = lev2 or not find_nearby_bombs(grid, i, j + 1)

                    if lev2:
                        if n_time % 2:
                            new_grid[i][j] = "."

                    else:
                        if n_time % 4 == 3:
                            new_grid[i][j] = "."

                else:
                    if n_time % 4 == 1:
                        new_grid[i][j] = "."

            else:
                if n_time % 4 == 3:
                    new_grid[i][j] = "."

    # breakpoint()
    return new_grid
    # return ["".join(i) for i in new_grid]
