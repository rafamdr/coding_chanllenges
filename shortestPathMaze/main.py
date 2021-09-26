# Given a MxN matrix where each element can either be 0 or 1. We need to find the shortest path between a given
# source cell to a destination cell. The path can only be created out of a cell if its value is 1. Expected time
# complexity is O(MN). For example –
#
# Input:
# mat[ROW][COL]  = {{1, 0, 1, 1, 1, 1, 0, 1, 1, 1 },
#                   {1, 0, 1, 0, 1, 1, 1, 0, 1, 1 },
#                   {1, 1, 1, 0, 1, 1, 0, 1, 0, 1 },
#                   {0, 0, 0, 0, 1, 0, 0, 0, 0, 1 },
#                   {1, 1, 1, 0, 1, 1, 1, 0, 1, 0 },
#                   {1, 0, 1, 1, 1, 1, 0, 1, 0, 0 },
#                   {1, 0, 0, 0, 0, 0, 0, 0, 0, 1 },
#                   {1, 0, 1, 1, 1, 1, 0, 1, 1, 1 },
#                   {1, 1, 0, 0, 0, 0, 1, 0, 0, 1 }};
# Source = {0, 0};
# Destination = {3, 4};
#
# Output:
# Shortest Path is 11
# ----------------------------------------------------------------------------------------------------------------------


from collections import deque
from typing import List
# ----------------------------------------------------------------------------------------------------------------------


class Solution:
    def shortest_path_maze(self, mat: List[List[int]], source: List[int], dest: List[int]) -> [int, List]:
        if mat[source[0]][source[1]] != 1 or mat[dest[0]][dest[1]] != 1:
            return -1, []
        queue = deque()
        queue.append([source, 0, [source]])
        possible_moves = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        rows, cols = len(mat), len(mat[0])
        visited = [[False for i in range(cols)] for j in range(rows)]
        while len(queue) > 0:
            [cx, cy], cost, path = queue.popleft()
            if [cx, cy] == dest:
                return cost, path
            for mx, my in possible_moves:
                nx, ny = cx + mx, cy + my
                if (0 <= nx < rows) and (0 <= ny < cols) and mat[nx][ny] == 1 and (visited[nx][ny] is False):
                    queue.append([[nx, ny], cost + 1, path + [[nx, ny]]])
                    visited[nx][ny] = True
        return -1, []
# ----------------------------------------------------------------------------------------------------------------------


examples = [
    {
        'mat': [
             [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
             [1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
             [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
             [0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
             [1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
             [1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
             [1, 1, 0, 0, 0, 0, 1, 0, 0, 1]
        ],
        'Source': [0, 0],
        'Destination': [3, 4],
        'ExpectedResult': [11, [[0, 0], [1, 0], [2, 0], [2, 1], [2, 2], [1, 2], [0, 2], [0, 3], [0, 4], [1, 4], [2, 4],
                                [3, 4]]]
    },
]

sol = Solution()
for ex in examples:
    print(
        'Ref...:\n %s :\n %s' % (
            str(ex['ExpectedResult']),
            str(sol.shortest_path_maze(ex['mat'], ex['Source'], ex['Destination']))
        )
    )
    print()
# ----------------------------------------------------------------------------------------------------------------------
