# Given a binary grid where 0 represents water and 1 represents land. An island is surrounded by water and is formed by
# connecting adjacent lands horizontally or vertically. Delete all islands that are connected to the matrix border
#
# Constraints:
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is 0 or 1.
# ----------------------------------------------------------------------------------------------------------------------


import copy
from typing import List
# ----------------------------------------------------------------------------------------------------------------------


class Solution:
    def _floodfill4(self, grid: List[List[int]], i: int, j: int, rows: int, cols: int):
        stack = []
        pos_modders = [ [-1, 0], [0, -1], [1, 0], [0, 1] ]
        stack.append([i, j])
        while len(stack) > 0:
            i = stack[-1][0]
            j = stack[-1][1]
            stack.pop()
            grid[i][j] = 0
            for pm in pos_modders:
                ni = i + pm[0]
                nj = j + pm[1]
                if (
                        0 <= ni < rows and
                        0 <= nj < cols and
                        grid[ni][nj] != 0
                ):
                    stack.append([ni, nj])

    def delete_border_islands(self, grid: List[List[int]]) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0]) if rows > 0 else 0
        for i in range(0, rows):
            if grid[i][0] != 0:
                self._floodfill4(grid, i, 0, rows, cols)
            if grid[i][cols - 1] != 0:
                self._floodfill4(grid, i, cols - 1, rows, cols)
        for j in range(0, cols):
            if grid[0][j] != 0:
                self._floodfill4(grid, 0, j, rows, cols)
            if grid[rows - 1][j] != 0:
                self._floodfill4(grid, rows - 1, j, rows, cols)
        return grid
# ----------------------------------------------------------------------------------------------------------------------


examples = {
    'ex1': {
        'input': [
            [1, 1, 1, 1, 0],
            [1, 1, 0, 0, 0],
            [1, 0, 0, 1, 0],
            [0, 1, 0, 0, 0],
            [1, 0, 0, 0, 1]
        ],
        'expected': [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
    }

}


def print_horizontal_mats(mats: List[List[List[int]]]):
    for row_idx in range(0, len(mats[0])):
        for mat in mats:
            print(mat[row_idx], end='\t\t')
        print()


sol = Solution()
for ex in examples:
    print('Ref.. Input\t\tExpected\t\tCalculated: \n')
    print_horizontal_mats([
        copy.deepcopy(examples[ex]['input']),
        examples[ex]['expected'],
        sol.delete_border_islands(copy.deepcopy(examples[ex]['input']))
    ])
    print()
# ----------------------------------------------------------------------------------------------------------------------
