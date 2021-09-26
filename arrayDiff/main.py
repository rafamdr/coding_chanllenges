# This week’s question: Given an array of integers and a target value, return the number of pairs of array elements
# that have a difference equal to a target value.
#
# Examples:
# $ arrayDiff([1, 2, 3, 4], 1)
# $ 3 // 2 - 1 = 1, 3 - 2 = 1, and 4 - 3 = 1
# ----------------------------------------------------------------------------------------------------------------------


from functools import reduce
from typing import List
# ----------------------------------------------------------------------------------------------------------------------


class Solution:
    def array_diff_ref(self, arr: List[int], diff: int) -> int:
        count_diff = 0
        temp_set = set(arr)
        for number in arr:
            count_diff += int(number + diff in temp_set)
        return count_diff

    def array_diff_small(self, arr: List[int], diff: int) -> int:
        temp_set = set(arr)
        return reduce(lambda count, number: count + int(number + diff in temp_set), arr, 0)
# ----------------------------------------------------------------------------------------------------------------------


examples = {
    (1, 2, 3, 4): 1,
    (1, 3, 2, 4): 1,
    (4, 3, 2, 1): 1,
    (4, 3, 2, 1): 16,
    (2, 4, 6, 8, 9, 11, 10): 2
}


sol = Solution()

for ex in examples:
    print('Ref...: %s -> %s ' % (str(ex), sol.array_diff_ref(list(ex), examples[ex])))
    print('Small.: %s -> %s ' % (str(ex), sol.array_diff_small(list(ex), examples[ex])))
    print()
# ----------------------------------------------------------------------------------------------------------------------
