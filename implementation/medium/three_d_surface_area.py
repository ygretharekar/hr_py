"https://www.hackerrank.com/challenges/3d-surface-area/problem"
class ThreeDSurfaceArea:
    "Solution"
    def solution(self, grid_weights):
        "solution"
        row_len = len(grid_weights)
        col_len = len(grid_weights[0])

        c_offset = (1, 0, -1, 0)
        r_offset = (0, 1, 0, -1)

        s_area = row_len*col_len*2

        for i in range(row_len):
            for j in range(col_len):
                for offset, elem in enumerate(c_offset):
                    row = elem + i
                    col = r_offset[offset] + j

                    adj_height = grid_weights[row][col] if (row >= 0 and col >= 0
                                                            and row < row_len and
                                                            col < col_len) else 0

                    s_area += max(0, grid_weights[i][j] - adj_height)

        return s_area
