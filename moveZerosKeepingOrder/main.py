# Given an integer array, move all 0s to the end of it while maintaining the relative order of the non-zeroes. Bonus:
# do this without making a copy of the array!
#
# Example:
#
# $ moveZeroes([0,2,0,3,8])
# $ [2,3,8,0,0]
# ----------------------------------------------------------------------------------------------------------------------


from typing import List
# ----------------------------------------------------------------------------------------------------------------------


class Solution:
    def move_zeros_v2(self, array: List):
        # swapping non-zeros elements in the beginning of array
        # Time: O(n); Space: O(1)
        pos_to_swap = 0
        for i in range(len(array)):
            if array[i] != 0:
                array[pos_to_swap], array[i] = array[i], array[pos_to_swap]
                pos_to_swap += 1
        return array
# ----------------------------------------------------------------------------------------------------------------------


examples = [
    # [0, 0, 0, 0, 4, 0],
    # [6, 5, 4, 0],
    # [0, 0, 0],
    # [0, 0],
    # [0],
    # [1, 0],
    # [0, 1],
    # [],
    # [1, 2, 0, 1, 0, 0, 3, 6],
    [0, 1, 2, 0, 1, 0, 0, 3, 6],
    # [0, 0, 0, 0, 0, 0, 1111, 1, 1, 1, 1],
    # [0, 1, 2, 3, 4],
    # [1, 2, 3, 4],
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4],
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 0],
]

sol = Solution()
for ex in examples:
    print('V2: %s' % sol.move_zeros_v2(ex.copy()))
    print('-------------------------------------------------')
# ----------------------------------------------------------------------------------------------------------------------
