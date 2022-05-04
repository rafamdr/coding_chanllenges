# Given an unsorted array of integers and a number n, find the subarray of length n that has the largest sum.
#
# Example:
#
# $ largestSubarraySum([3,1,4,1,5,9,2,6], 3)
# $ [9, 2, 6]
# ----------------------------------------------------------------------------------------------------------------------

from typing import List, Dict
# ----------------------------------------------------------------------------------------------------------------------


class Solution:

    def largest_subarray_sum(self, array: List[int], n: int) -> List[int]:
        curr_start_pos = max_start_pos = 0
        curr_sum = max_sum = sum(array[0: min(n, len(array))])
        for i in range(n, len(array)):
            curr_sum = curr_sum - array[curr_start_pos] + array[i]
            curr_start_pos += 1
            if curr_sum > max_sum:
                max_sum = curr_sum
                max_start_pos = curr_start_pos
        return array[max_start_pos: max_start_pos + n]
# ----------------------------------------------------------------------------------------------------------------------


examples = {
    (tuple([]), 3): [],
    (tuple([3, 1]), 3): [3, 1],
    (tuple([3, 1, 4]), 3): [3, 1, 4],
    (tuple([3, 1, 4, 1, 5, 9, 2, 6]), 3): [9, 2, 6],
    (tuple([3, 1, 4, 1, 5, 9, 2, 6, 2]), 3): [9, 2, 6],
    (tuple([3, 1, 4, 1, 5, 9, 2, 6, 2]), 0): [],
    (tuple([3, 1, 4, 1, 5, 9, 2, 6, 2]), 1): [9]
}

sol = Solution()
for ex in examples:
    array_ex, n_ex = ex
    print('Ref..: %s <-> %s == %s' % (ex, examples[ex], sol.largest_subarray_sum(list(array_ex), n_ex)))
    print()
# ----------------------------------------------------------------------------------------------------------------------
