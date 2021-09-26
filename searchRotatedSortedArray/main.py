# There is an integer array nums sorted in ascending order (with distinct values).
#
# Prior to being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such
# that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For
# example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
#
# Given the array nums after the rotation and an integer target, return the index of target if it is in nums,
# or -1 if it is not in nums.
from typing import List


class Solution:
    def findPivot(self, nums: List[int]) -> int:
        first = 0
        last = len(nums) - 1
        if nums[first] < nums[last]:
            return -1
        while first < last:
            mid = first + (last - first) // 2
            if nums[first] < nums[mid]:
                first = mid
            elif nums[first] > nums[mid]:
                last = mid - 1
            else:
                first = first + 1
        return first

    def binarySearch(self, nums: List[int], first, last, target) -> int:
        if last < first:
            return -1
        while first <= last:
            mid = first + (last - first) // 2
            if nums[mid] < target:
                first = mid + 1
            elif nums[mid] > target:
                last = mid - 1
            else:
                return mid

        return -1

    def search(self, nums: List[int], target: int) -> int:
        pivot = self.findPivot(nums)
        return pivot

        if pivot == -1:
            return self.binarySearch(nums, 0, len(nums) - 1, target)
        elif nums[pivot] == target:
            return pivot
        elif nums[0] <= target:
            return self.binarySearch(nums, 0, pivot - 1, target);
        else:
            return self.binarySearch(nums, pivot + 1, len(nums) - 1, target);

sol = Solution()

sol.search([4,5,6,7,0,1,2], 6)