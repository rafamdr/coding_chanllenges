# This week’s question:
# Given an n x n matay, rotate it 90 degrees without making a new matay.
#
# Example:
# $ rotate90([[1,2,3],[4,5,6],[7,8,9]])
# $ [[7,4,1],[8,5,2],[9,6,3]]
# ----------------------------------------------------------------------------------------------------------------------


import copy
import functools
from typing import List
# ----------------------------------------------------------------------------------------------------------------------


class Solution:
    def max_pformat(self, m: List[List]) -> str:
        res = ''
        for line in m:
            res += str(line) + '\n'
        return res

    def rotate90_triangle(self, mat: List[List]) -> List[List]:
        side = len(mat)
        for i in range(side):
            for j in range(i + 1):
                if j == i:
                    temp_i = i
                    temp_j = side - j - 1
                else:
                    temp_i = j
                    temp_j = side - i - 1
                mat[i][j], mat[temp_i][temp_j] = mat[temp_i][temp_j], mat[i][j]
        for i in range(side):
            for j in range(i + 1, side):
                if j + i >= side:
                    mat[i][j], mat[j][side - i - 1] = mat[j][side - i - 1], mat[i][j]
        return mat
    
    def rotate90_transpose(self, mat: List[List]) -> List[List]:
        side = len(mat)
        for i in range(side):
            for j in range(i, side):
                mat[j][i], mat[i][j] = mat[i][j], mat[j][i]
        for i in range(side):
            for j in range(side//2):
                mat[i][j], mat[i][side - 1 - j] = mat[i][side - 1 - j], mat[i][j]
        return mat
# ----------------------------------------------------------------------------------------------------------------------


examples = {
    'ex0': [
    ],
    'ex1': [
        [1],
    ],
    'ex2': [
        [1, 2],
        [3, 4],
    ],
    'ex3': [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ],
    'ex4': [
        [1, 2,  3,  4],
        [5, 6,  7,  8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ],
    'ex5': [
        [1,  2,  3,  4,  5],
        [6,  7,  8,  9,  10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25],
    ]
}

sol = Solution()

for ex in examples:
    print('Ref.: \n%s->\n%s ' %
          (sol.max_pformat(examples[ex]), sol.max_pformat(sol.rotate90_triangle(copy.deepcopy(examples[ex])))))
    print('Trp.: \n%s->\n%s ' %
          (sol.max_pformat(examples[ex]), sol.max_pformat(sol.rotate90_transpose(copy.deepcopy(examples[ex])))))
# ----------------------------------------------------------------------------------------------------------------------
