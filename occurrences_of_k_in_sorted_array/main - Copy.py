from typing import List
# ----------------------------------------------------------------------------------------------------------------------


class Example:
    def __init__(self, arr: List, k):
        self.arr = arr
        self.k = k
# ----------------------------------------------------------------------------------------------------------------------


class Solution:
    def binary_search(self, arr: List, k):
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] < k:
                left = mid + 1
            elif arr[mid] > k:
                right = mid - 1
            else:
                return mid

        return -1

    def occurrences_of_k_in_sorted_array(self, arr: List, k):
        res1 = self.binary_search([-1, -1, 0, 1, 1, 1, 3, 5, 9], 1)
        res2 = self.binary_search([-1, -1, 0, 1, 1, 1], 1)

        #res = self.binary_search(arr, k)
        return 0
# ----------------------------------------------------------------------------------------------------------------------


sol = Solution()
examples = [
    Example([1, 1, 1, 3, 5, 9], 1),
    Example([-1, -1, 0, 1, 1, 1, 3, 5, 9], 1),
]

for ex in examples:
    res = sol.occurrences_of_k_in_sorted_array(ex.arr, ex.k)
    print('Result = %d' % res)

# ----------------------------------------------------------------------------------------------------------------------
