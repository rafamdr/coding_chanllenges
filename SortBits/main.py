# Given an integer array arr, sort the integers in arr in ascending order by the number of 1’s in their binary
# representation and return the sorted array.
#
# Examples:
# $ sortBits([0,1,2,3,4,5,6,7,8])
# $ [0,1,2,4,8,3,5,6,7]
# ----------------------------------------------------------------------------------------------------------------------


from typing import List
import numpy
import sys
# ----------------------------------------------------------------------------------------------------------------------


class Solution:
    def sort_bits_ref(self, numbers: List[int]) -> List[int]:
        def count_set_bits(num: int):
            count = 0
            if num < 0:
                num = num & 0x7FFFFFFFFFFFFFFF if sys.maxsize > 2**32 else num & 0x7FFFFFFF
                count += 1
            while num != 0:
                count += num & 1
                num >>= 1
            return count
        return sorted(numbers, key=lambda x: count_set_bits(x))

    def sort_bits_fast(self, numbers: List[int]) -> List[int]:
        coef = [0x55555555, 0x33333333, 0x0F0F0F0F, 0x01010101, 24]
        if sys.maxsize > 2 ** 32:
            coef = [0x5555555555555555, 0x3333333333333333, 0x0f0f0f0f0f0f0f0f, 0x0101010101010101, 56]

        def count_set_bits(num: int):
            num = num - ((num >> 1) & coef[0])
            num = (num & coef[1]) + ((num >> 2) & coef[1])
            num = (num + (num >> 4)) & coef[2]
            return (num * coef[3]) >> coef[4]
        return sorted(numbers, key=lambda x: count_set_bits(x))
# ----------------------------------------------------------------------------------------------------------------------


examples = [
    [0, 1, 2, 3, 4, 5, 6, 7, 8],
    [1, 1, 1, 3, 5, 9],
    [-1, -1, 0, 1, 1, 1, 3, 5, 9],
    [3, 1, 7, 5, 4],
    [0, 2, 2, 4, 0, 1, 0, 1, 3],
    [-2, -1, 4, 2, 1, 9, 10, 4],
    [-1, 4, 2, 1, 9, 10],
    [1000, -1, -2, -23423],
    [2, 1],
    [0],
    [0, 0],
    [1, 1],
    [1],
    [4],
    [],
    [1, 3, 3],
    [1, 2, 3],
    [1, 2, 0],
    [2, 3, 1],
    [3, 4, -1, 1],
    [7, 8, 9, 11, 12]
]
sol = Solution()
for ex in examples:
    print('Ref.: %s -> %s ' % (str(ex), sol.sort_bits_ref(ex)))
    print('Fast: %s -> %s ' % (str(ex), sol.sort_bits_fast(ex)))
    print()
# ----------------------------------------------------------------------------------------------------------------------
