# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of
# islands.
# # An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water.
#
# Example 1:
#
# Input: grid = [
#   [1,1,1,1,0],
#   [1,1,0,1,0],
#   [1,1,0,0,0],
#   [0,0,0,0,0]
# ]
# Output: 1
# Example 2:
#
# Input: grid = [
#   [1,1,0,0,0],
#   [1,1,0,0,0],
#   [0,0,1,0,0],
#   [0,0,0,1,1]
# ]
# Output: 3
#
#
# Constraints:
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is 0 or 1.
# ----------------------------------------------------------------------------------------------------------------------


import numpy as np
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

    def num_islands(self, grid: List[List[int]]) -> int:
        resp = 0
        rows = len(grid)
        cols = len(grid[0]) if rows > 0 else 0
        for i in range(0, rows):
            for j in range(0, cols):
                if grid[i][j] != 0:
                    self._floodfill4(grid, i, j, rows, cols)
                    resp += 1
        return resp
# ----------------------------------------------------------------------------------------------------------------------


examples = {
    1: [
        [1, 1, 1, 1, 0],
        [1, 1, 0, 1, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ],
    3: [
        [1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 1]
    ]
}

sol = Solution()
for ex in examples:
    print('Ref..: %s -> %s \n %s ' % (str(ex), str(sol.num_islands(examples[ex])), np.array(examples[ex])))
    print()
# ----------------------------------------------------------------------------------------------------------------------
