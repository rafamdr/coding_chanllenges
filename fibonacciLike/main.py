# Given an array of increasing integers, find the length of the longest fibonacci-like subsequence of the array. If
# one does not exist, return 0. A sequence is “fibonacci-like” if X_i + X_{i+1} = X_{i+2}.
#
# Example:
# $ fibonacciLike([1,3,7,11,12,14,18])
# $ 3 -> these sequences: [1,11,12], [3,11,14] or [7,11,18]
# ----------------------------------------------------------------------------------------------------------------------


from typing import List
# ----------------------------------------------------------------------------------------------------------------------


class Solution:
    def fibonacci_like_ref(self, array: List[int]):
        # O(n^2) with O(n) extra space
        max_cnt = 0
        fib_mem = {}
        for pos, val in enumerate(array):
            for other_pos in range(0, pos):


        return max_cnt
# ----------------------------------------------------------------------------------------------------------------------


examples = [
     [2, 4, 5, 6, 7, 8, 11, 13, 14, 15, 21, 22, 34],
     [1, 2, 3, 4, 5, 6, 7, 8],
     [-1, 2, 1],
     [1, 2, 3, 5, 8, 13, 21, 34],
     [1, 3, 7, 11, 12, 14, 18],
     [0],
     [0, 0],
     [1, 1],
     [1],
     [4],
     [],
     [1, 3, 3],
     [1, 2, 3],
     [7, 8, 9, 11, 12]
]

sol = Solution()

for ex in examples:
    print('Ref..: %s -> %s ' % (str(ex), str(sol.fibonacci_like_ref(ex))))
    # print('Fast.: %s -> %s ' % (str(ex), str(sol.fibonacci_like_fast(ex))))
    print()
# ----------------------------------------------------------------------------------------------------------------------
