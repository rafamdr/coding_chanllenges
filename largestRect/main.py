# Given a 2D array of 0s and 1s, return the size of the largest rectangle of 1s in the array.
#
# Example:
#
# let islands = [
# 0,0,0,1,0
# 1,1,0,0,1
# 1,1,0,0,0
# 0,0,1,0,0
# ]
#
# $ largestRect(islands)
# $ '2x2'
# ----------------------------------------------------------------------------------------------------------------------


import enum
from copy import deepcopy
from typing import List
import numpy as np
# ----------------------------------------------------------------------------------------------------------------------


class DonutsMode(enum.Enum):
    HOLES_ALLOWED = 1,
    FILLED = 2
# ----------------------------------------------------------------------------------------------------------------------


class Solution:
    def largest_rect_v1(self, grid: List[List[int]]) -> str:
        rows, cols = len(grid), len(grid[0])
        grid_lines = [[0 for _ in range(0, cols)] for _ in range(0, rows)]
        grid_cols = [[0 for _ in range(0, cols)] for _ in range(0, rows)]
        grid_result = [[0 for _ in range(0, cols)] for _ in range(0, rows)]
        max_col_count = max_row_count = 0
        for i in range(0, rows):
            for j in range(0, cols):
                if grid[i][j] != 0:
                    grid_lines[i][j] = 1 if i == 0 else grid_lines[i - 1][j] + 1
                    grid_cols[i][j] = 1 if j == 0 else grid_cols[i][j - 1] + 1
                grid_result[i][j] = max(grid_lines[i][j], grid_cols[i][j])
                if (grid_lines[i][j] * grid_cols[i][j]) > (max_row_count * max_col_count):
                    max_row_count, max_col_count = grid_lines[i][j], grid_cols[i][j]
        return f'{max_row_count}x{max_col_count}'

    def largest_rect_v2(self, grid: List[List[int]]) -> str:
        rows, cols = len(grid), len(grid[0])
        grid_result = [[0 for _ in range(0, cols)] for _ in range(0, rows)]
        grid_lines = [[0 for _ in range(0, cols)] for _ in range(0, rows)]
        max_col_count = max_row_count = 0
        for i in range(0, rows):
            grid_cols = [0 for _ in range(0, cols)]
            for j in range(0, cols):
                if grid[i][j] != 0:
                    grid_lines[i][j] = 1 if i == 0 else grid_lines[i - 1][j] + 1
                    grid_cols[j] = 1 if j == 0 else grid_cols[j - 1] + 1
                grid_result[i][j] = max(grid_lines[i][j], grid_cols[j])
                if (grid_lines[i][j] * grid_cols[j]) > (max_row_count * max_col_count):
                    max_row_count, max_col_count = grid_lines[i][j], grid_cols[j]
        return f'{max_row_count}x{max_col_count}'

    def largest_rect_v3(self, grid: List[List[int]], donuts_mode=DonutsMode.FILLED) -> str:
        rows, cols = len(grid), len(grid[0])
        grid_result = [[0 for _ in range(0, cols)] for _ in range(0, rows)]
        last_grid_line = grid_line = [0 for _ in range(0, cols)]
        max_col_count = max_row_count = 0
        for i in range(0, rows):
            grid_cols = [0 for _ in range(0, cols)]
            for j in range(0, cols):
                if grid[i][j] != 0:
                    grid_line[j] = 1 if i == 0 else last_grid_line[j] + 1
                    grid_cols[j] = 1 if j == 0 else grid_cols[j - 1] + 1
                grid_result[i][j] = max(grid_line[j], grid_cols[j])
                if (grid_line[j] * grid_cols[j]) > (max_row_count * max_col_count):
                    max_row_count, max_col_count = grid_line[j], grid_cols[j]
            last_grid_line = deepcopy(grid_line)
        return f'{max_row_count}x{max_col_count}'

    def get_largest_range(self, line):
        curr_idx = -1
        curr_sum = max_sum = 0
        curr_row_count = row_count = 0
        i = col_count = 0
        for i, value in enumerate(line):
            if curr_idx == -1:
                if value > 0:
                    curr_idx = i
                    curr_sum += value
                    curr_row_count = value
            else:
                if value > 0:
                    curr_sum += value
                    curr_row_count = min(curr_row_count, value)
                else:
                    if curr_sum > max_sum:
                        max_sum = curr_sum
                        col_count = i - curr_idx
                        row_count = curr_row_count
                    curr_idx = -1
                    curr_sum = 0

        if curr_idx != -1:
            if curr_sum > max_sum:
                col_count = i - curr_idx + 1
                row_count = curr_row_count

        return row_count, col_count

    def largest_rect_v4(self, grid: List[List[int]]) -> str:
        rows, cols = len(grid), len(grid[0])
        max_col_count = max_row_count = 0
        line = [0 for _ in range(0, cols)]
        for i in range(0, rows):
            for j in range(0, cols):
                line[j] = line[j] + 1 if grid[i][j] == 1 else 0
            height, width = self.get_largest_range(line)
            if (width * height) > (max_row_count * max_col_count):
                max_row_count, max_col_count = height, width
        return f'{max_row_count}x{max_col_count}'

    def largest_rect_v5(self, grid: List[List[int]], donuts_mode=DonutsMode.HOLES_ALLOWED) -> str:
        rows, cols = len(grid), len(grid[0])
        max_col_count = max_row_count = 0
        line = [0 for _ in range(0, cols)]
        for i in range(0, rows):
            for j in range(0, cols):
                if 0 < j < cols - 1 and donuts_mode == DonutsMode.HOLES_ALLOWED:
                    if grid[i][j] > 0:
                        if line[j] < 0:
                            line[j] = line[j - 1]
                        else:
                            line[j] = line[j] + 1
                    else:
                        if line[j] < 0:
                            if line[j - 1] == 0 or line[j + 1] == 0:
                                line[j] = 0
                        else:
                            if line[j - 1] != 0 and line[j + 1] != 0:
                                line[j] = -1
                            else:
                                line[j] = 0
                else:
                    line[j] = line[j] + 1 if grid[i][j] == 1 else 0
            height, width = self.get_largest_range(line)
            if (width * height) > (max_row_count * max_col_count):
                max_row_count, max_col_count = height, width
        return f'{max_row_count}x{max_col_count}'

    def get_largest_range_v2(self, line):
        curr_idx = None
        i = col_count = curr_sum = max_sum = curr_row_count = row_count = 0
        for i, value in enumerate(line):
            if value > 0:
                curr_sum += value
                curr_row_count = min(curr_row_count or value, value)
                curr_idx = i if curr_idx is None else curr_idx
            else:
                if curr_sum > max_sum and curr_idx is not None:
                    max_sum = curr_sum
                    col_count = i - curr_idx
                    row_count = curr_row_count
                curr_row_count = curr_idx = None
                curr_sum = 0
        if curr_idx is not None:
            if curr_sum > max_sum:
                col_count = i - curr_idx + 1
                row_count = curr_row_count
        return row_count, col_count

    def largest_rect_v6(self, grid: List[List[int]], donuts_mode=DonutsMode.HOLES_ALLOWED) -> str:
        rows, cols = len(grid), len(grid[0])
        max_col_count = max_row_count = 0
        line = [0 for _ in range(0, cols)]
        for i in range(0, rows):
            for j in range(0, cols):
                if 0 < j < cols - 1 and donuts_mode == DonutsMode.HOLES_ALLOWED:
                    if grid[i][j] > 0:
                        line[j] = line[j - 1] if (line[j] < 0) else line[j] + 1
                    else:
                        line[j] = -1 if(line[j - 1] != 0 and line[j + 1] != 0) else 0
                else:
                    line[j] = line[j] + 1 if grid[i][j] == 1 else 0
            height, width = self.get_largest_range_v2(line)
            if (width * height) > (max_row_count * max_col_count):
                max_row_count, max_col_count = height, width
        return f'{max_row_count}x{max_col_count}'
# ----------------------------------------------------------------------------------------------------------------------


examples = {
    '2x2': [
        [0, 0, 0, 1, 0],
        [1, 1, 0, 0, 1],
        [1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
    ],
    '2x3': [
        [0, 0, 0, 1, 0],
        [1, 1, 1, 0, 1],
        [1, 1, 1, 0, 0],
        [0, 0, 1, 0, 0],
    ],
    '3x3': [
        [0, 0, 0, 1, 0],
        [1, 1, 1, 0, 1],
        [1, 1, 1, 0, 0],
        [1, 1, 1, 0, 1],
    ],
    '3x3 v2': [
        [0, 0, 0, 1, 0],
        [1, 1, 1, 0, 1],
        [1, 0, 1, 0, 0],
        [1, 1, 1, 0, 1],
    ],
    '1x1': [
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ],
    '1x1 v2': [
        [1],
    ],
    '1x4': [
        [1, 1, 1, 1],
    ],
    '4x1': [
        [1, 1, 0, 1, 0],
        [1, 0, 1, 0, 0],
        [1, 0, 1, 0, 0],
        [1, 0, 1, 0, 0],
    ],
    '4x5': [
        [0, 0, 0, 1, 0],
        [1, 1, 1, 0, 0],
        [1, 0, 1, 0, 0],
        [1, 1, 1, 0, 0],
        [1, 1, 1, 0, 0],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
    ],
    '6x3': [
        [0, 0, 0, 1, 0],
        [1, 1, 1, 0, 0],
        [1, 0, 1, 0, 0],
        [1, 1, 1, 0, 0],
        [1, 1, 1, 0, 0],
        [1, 0, 1, 0, 0],
        [1, 1, 1, 0, 0],
    ],
    '7x3': [
        [0, 0, 0, 1, 0, 0, 1, 0],
        [1, 1, 1, 0, 0, 1, 1, 0],
        [1, 0, 1, 0, 0, 1, 1, 1],
        [1, 1, 1, 0, 0, 1, 1, 1],
        [1, 1, 1, 0, 0, 1, 1, 1],
        [1, 0, 1, 0, 0, 1, 1, 1],
        [1, 1, 1, 0, 0, 1, 1, 1],
        [1, 1, 1, 0, 0, 1, 1, 1],
    ],
}

sol = Solution()
for ex in examples:
    print('Ref..: %s -> %s ' % (str(ex), str(sol.largest_rect_v1(examples[ex]))))
    print('v2...: %s -> %s ' % (str(ex), str(sol.largest_rect_v2(examples[ex]))))
    print('v3...: %s -> %s ' % (str(ex), str(sol.largest_rect_v3(examples[ex]))))
    print('v4...: %s -> %s ' % (str(ex), str(sol.largest_rect_v4(examples[ex]))))
    print('v5...: %s -> %s ' % (str(ex), str(sol.largest_rect_v5(examples[ex]))))
    print('v6...: %s -> %s ' % (str(ex), str(sol.largest_rect_v6(examples[ex]))))
    print('%s ' % np.array(examples[ex]))
    print()
# ----------------------------------------------------------------------------------------------------------------------
