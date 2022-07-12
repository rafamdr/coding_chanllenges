# Given an n x m matrix where all the units are 0s except for an 1 for “start”, a 2 for “end”, and 3s for walls,
# find the shortest paths that you can take to get from 1 to 2, while working around 3s.
#
# Example:
#
# let grid = [
# [1,0,0],
# [0,0,2]
# ]
#
# let grid2 = [
# [1,3,0],
# [0,0,2]
# ]
#
# $ startToEnd(grid)
# $ [['right', 'right', 'down'], ['right', 'down', 'right'], ['down', 'right', 'right']]
#
# $ startToEnd(grid2)
# $ [['down', 'right', 'right']]
# ----------------------------------------------------------------------------------------------------------------------


import enum
from typing import List
# ----------------------------------------------------------------------------------------------------------------------


class Cell(enum.Enum):
    EMPTY = 0
    START = 1
    END = 2
    WALL = 3
# ----------------------------------------------------------------------------------------------------------------------


class Direction(enum.Enum):
    left = (0, -1)
    up = (-1, 0)
    right = (0, 1)
    down = (1, 0)
# ----------------------------------------------------------------------------------------------------------------------


class Solution:
    def _get_distance(self, p1: tuple[int, int], p2: tuple[int, int]):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    def _shortest_paths(self, grid: List[List[int]], start: tuple[int, int], end: tuple[int, int]) -> List[List[str]]:
        rows, cols = len(grid), len(grid[0])
        paths = []
        stack = [[start[0], start[1], []]]
        while len(stack) > 0:
            i, j, path = stack.pop()
            if (i, j) == end:
                paths.append(path)
            for pm in Direction:
                ni, nj = i + pm.value[0], j + pm.value[1]
                if (
                    0 <= ni < rows and 0 <= nj < cols and
                    grid[ni][nj] in [Cell.EMPTY.value, Cell.END.value] and
                    self._get_distance((ni, nj), end) <= self._get_distance((i, j), end)
                ):
                    stack.append([ni, nj, path + [str(pm.name)]])
        return paths

    def _find_endpoints(self, grid: List[List[int]]):
        si = sj = ei = ej = -1
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == Cell.START.value:
                    si, sj = i, j
                elif grid[i][j] == Cell.END.value:
                    ei, ej = i, j
        return (si, sj), (ei, ej)

    def start_to_end(self, grid: List[List[int]]) -> List[List[str]]:
        start, end = self._find_endpoints(grid)
        return self._shortest_paths(grid, start, end)
# ----------------------------------------------------------------------------------------------------------------------


examples = {
    # 'ex1': {
    #     'input': [
    #         [1, 0, 0],
    #         [0, 0, 2]
    #     ],
    #     'expected': [['right', 'right', 'down'], ['right', 'down', 'right'], ['down', 'right', 'right']]
    # },
    # 'ex2': {
    #     'input': [
    #         [1, 3, 0],
    #         [0, 0, 2]
    #     ],
    #     'expected': [['down', 'right', 'right']]
    # },
    'ex3': {
        'input': [
            [0, 1, 3, 0],
            [0, 0, 3, 0],
            [0, 0, 3, 2],
            [0, 0, 3, 0],
            [0, 0, 0, 0],
        ],
        'expected': [['down', 'right', 'right']]
    },
}


sol = Solution()

for ex in examples:
    input_ex, expected_ex = examples[ex]['input'], examples[ex]['expected']
    print(
        'Ref...: \n\tInput: %s \n\tExpected: %s\n\tOutput: %s' % (
            input_ex, expected_ex, sol.start_to_end(examples[ex]['input'])
        )
    )
    print()
# ----------------------------------------------------------------------------------------------------------------------
