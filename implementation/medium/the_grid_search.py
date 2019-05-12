"grid search"
class GridSearch:
    "the grid search"
    def solution(self, grid, pattern):
        "solution"
        if not grid and not pattern:
            return "YES"

        if len(pattern) > len(grid):
            return "NO"

        elif len(pattern[0]) > len(grid[0]):
            return "NO"

        r_len = len(grid)
        c_len = len(grid[0])

        r_pat_len = len(pattern)
        c_pat_len = len(pattern[0])

        for i in range(r_len - r_pat_len + 1):
            for j in range(c_len - c_pat_len + 1):
                if pattern[0][0] == grid[i][j]:
                    pat_pass = True
                    for a_i in range(r_pat_len):
                        for b_i in range(c_pat_len):
                            if pattern[a_i][b_i] != grid[i+a_i][j+b_i]:
                                pat_pass = False
                                break
                        if not pat_pass:
                            break

                    if pat_pass:
                        return "YES"

        return "NO"
