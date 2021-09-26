import sys
from typing import List, Set
# ----------------------------------------------------------------------------------------------------------------------


class Solution:

    def _floodfill4(self, grid: List[List[int]], i: int, j: int, rows: int, cols: int, visited: Set):
        locpeak = sys.maxsize
        peak_sum = 0
        peak_count = 0
        water = 0
        stack = []
        pos_modders = [ [-1, 0], [0, -1], [1, 0], [0, 1] ]
        stack.append([i, j])
        while len(stack) > 0:
            i = stack[-1][0]
            j = stack[-1][1]
            stack.pop()

            for pm in pos_modders:
                ni = i + pm[0]
                nj = j + pm[1]
                if (
                    0 <= ni < rows and
                    0 <= nj < cols and
                    (ni, nj) not in visited
                ):
                    if grid[ni][nj] > grid[i][j]:
                        if grid[ni][nj] < locpeak:
                            locpeak = grid[ni][nj]
                    else:
                        if(
                            ni == 0 or
                            nj == 0 or
                            ni == rows - 1 or
                            nj == cols - 1
                        ):
                            return 0
                        else:
                            stack.append([ni, nj])

            peak_sum += grid[i][j]
            peak_count += 1
            grid[i][j] = -1

        return water

    def trapRainWater2d(self, grid: List[List[int]]) -> int:
        resp = 0
        rows = len(grid)
        cols = len(grid[0]) if rows > 0 else 0
        visited = set()
        for i in range(1, rows - 1):
            for j in range(1, cols - 1):
                if grid[i][j] >= 0:
                    self._floodfill4(grid, i, j, rows, cols, visited)
                    resp += 1

        return resp
# ----------------------------------------------------------------------------------------------------------------------


sol = Solution()
#res = sol.trapRainWater2d([[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]])

res = sol.trapRainWater2d(
    [
        [1,4,4,3,1,3,2],
        [4,1,2,1,3,2,4],
        [2,4,4,3,2,3,1]
    ]
)
print(res)
# ----------------------------------------------------------------------------------------------------------------------
