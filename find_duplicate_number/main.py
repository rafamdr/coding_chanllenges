# Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at
# least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.
#
# Example 1:
#
# Input: [1,3,4,2,2]
# Output: 2
# Example 2:
#
# Input: [3,1,3,4,2]
# Output: 3
# Note:
#
# You must not modify the array (assume the array is read only).
# You must use only constant, O(1) extra space.
# Your runtime complexity should be less than O(n2).
# There is only one duplicate number in the array, but it could be repeated more than once.
# ----------------------------------------------------------------------------------------------------------------------


from typing import List
# ----------------------------------------------------------------------------------------------------------------------


class Solution:
    def find_duplicate_number_naive(self, array: List):
        # Worst case: O(n^2)
        for i in range(0, len(array)):
            for j in range(i + 1, len(array)):
                if array[i] == array[j]:
                    return array[i]
        return None

    def find_duplicate_number_sorting(self, array: List):
        # Worst case: O(nlogn)
        array = sorted(array)
        for i in range(1, len(array)):
            if array[i] == array[i - 1]:
                return array[i]
        return None

    def find_duplicate_number_fast(self, array: List[int]):
        ptr1 = ptr2 = 0
        while True:
            ptr1 = array[ptr1]
            ptr2 = array[array[ptr2]]
            if ptr1 == ptr2:
                break
        ptr1 = 0
        while ptr1 != ptr2:
            ptr1 = array[ptr1]
            ptr2 = array[ptr2]
        return ptr2
# ----------------------------------------------------------------------------------------------------------------------


examples = [
    [1, 1],
    [1, 3, 4, 2, 2],
    [3, 1, 3, 4, 2]
]

sol = Solution()

for ex in examples:
    print('Naive: %s ' % str(sol.find_duplicate_number_naive(ex)))
    print('Sort.: %s ' % str(sol.find_duplicate_number_sorting(ex)))
    print('Fast.: %s ' % str(sol.find_duplicate_number_fast(ex)))
    print()
# ----------------------------------------------------------------------------------------------------------------------
