# This week’s question:
# Given a n x m binary matrix filled with 0s and 1s, find the largest rectangle containing only 1s and return its area.
#
# Example:
# $ matrix =
#   [
#     [1, 0, 1, 0, 0],
#     [1, 0, 1, 1, 1],
#     [1, 1, 0, 1, 1],
#     [1, 0, 0, 1, 0]
#   ]
# $ largestRect(matrix)
# $ 4
# ----------------------------------------------------------------------------------------------------------------------


import math
from typing import List
# ----------------------------------------------------------------------------------------------------------------------


class Solution:
    def largest_rect_ref(self, matrix: List[List[int]]) -> int:
        rmat = [[0] * len(matrix[0])] * len(matrix)
        largest = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] > 0:
                    upsum = 0
                    dsum = 0
                    lsum = 0

                    if i - 1 > 0:
                        if rmat[i - 1][j] > 0:
                            if i - 2 > 0:
                                if rmat[i - 2][j] <= rmat[i - 1][j]:

        return 0

# ----------------------------------------------------------------------------------------------------------------------


examples = {
    'ex1=4': [
        [1, 0, 1, 0, 0],
        [1, 0, 1, 1, 1],
        [1, 1, 0, 1, 1],
        [1, 0, 0, 1, 0]
    ],
}


sol = Solution()
for ex in examples:
    resp = ex.split('=')[1]
    print('Ref...: %s -> %s : %s' % (str(ex), sol.largest_rect_ref(examples[ex]), resp))
    print()
# ----------------------------------------------------------------------------------------------------------------------
