# Given an array that was once sorted in ascending order is rotated at some pivot unknown to you beforehand (so [0,2,
# 4,7,9] might become [7,9,0,2,4], for example). Find the minimum value in that array in O(n) or less.
# ----------------------------------------------------------------------------------------------------------------------


from typing import List
# ----------------------------------------------------------------------------------------------------------------------


class Solution:
    def find_min_ref(self, arr: List[int]) -> int:
        # O(n)
        return min(arr)

    def find_min_try1(self, arr: List[int]) -> int:
        # O(n)
        first = 0
        last = len(arr) - 1
        while first < last - 1:
            mid = first + (last - first) // 2
            if arr[first] >= arr[last]:
                while arr[mid] > arr[(mid - 1) % len(arr)]:
                    mid = (mid - 1) % len(arr)
                first = mid
            else:
                last = mid
        return min(arr[first], arr[last])

    def find_min_try2(self, arr: List[int]) -> int:
        # O(logn)
        first = 0
        last = len(arr) - 1
        if arr[first] < arr[last]:
            return arr[first]
        while first < last:
            mid = first + (last - first) // 2
            if arr[mid] < arr[last]:
                last = mid
            else:
                first = mid + 1
        return arr[first]
# ----------------------------------------------------------------------------------------------------------------------


examples = [
    [7, 9, 0, 2, 4, 7],
    [5, 4, 3, 2, 1, 0],
    [0, 2, 4, 7, 9],
    [7, 9, 0, 2, 4],
    [2, 1],
    [1, 2],
    [1, 2, 3],
    [3, 2, 1],
    [1],
    [5, 6, 7, 8, 9, -2, 0, 2, 4],
    [7, 8, 9, -2, 0, 2, 4, 5, 6],
    [8, 9, -3, -2, 0, 2, 4, 5, 6, 7],
    [9, -3, -2, 0, 2, 4, 5, 6, 7, 8],
    [-3, -2, 0, 2, 4, 5, 6, 7, 8, 9],
    [-2, 0, 2, 4, 5, 6, 7, 8, 9, -3],
    [0, 2, 4, 5, 6, 7, 8, 9, -3, -2],
]


sol = Solution()

for ex in examples:
    print('Ref.: %s -> %s ' % (str(ex), sol.find_min_ref(ex)))
    print('Try1: %s -> %s ' % (str(ex), sol.find_min_try1(ex)))
    print('Try2: %s -> %s ' % (str(ex), sol.find_min_try2(ex)))
    print()
# ----------------------------------------------------------------------------------------------------------------------
