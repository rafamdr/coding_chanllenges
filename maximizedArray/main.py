# Given two integer arrays of size n, return a new array of size n such that n consists of only unique elements and
# the sum of all its elements is maximum.
#
# Example:
#
# let arr1 = [7, 4, 10, 0, 1]
# let arr2 = [9, 7, 2, 3, 6]
#
# $ maximizedArray(arr1, arr2)
# $ [9, 7, 6, 4, 10]
# ----------------------------------------------------------------------------------------------------------------------

import heapq
from typing import List, Set


# ----------------------------------------------------------------------------------------------------------------------


class Solution:
    def maximized_array(self, array1: List[int], array2: List[int]) -> Set[int]:
        unique = set(array1)
        heap = list(unique)
        heapq.heapify(heap)
        for new_elem in array2:
            if new_elem not in unique:
                if len(heap) < len(array2):
                    heapq.heappush(heap, new_elem)
                    unique.add(new_elem)
                elif new_elem > heap[0]:
                    old_elem = heapq.heapreplace(heap, new_elem)
                    unique.remove(old_elem)
                    unique.add(new_elem)
        return unique
# ----------------------------------------------------------------------------------------------------------------------


examples = {
    'ex1': {
        'input': [
            [7, 4, 10, 0, 1],
            [9, 7, 2, 3, 6]
        ],
        'expected': {9, 7, 6, 4, 10}
    },
    'ex2': {
        'input': [
            [7, 4, 10, 10, 10, 0, 1],
            [9, 7, 2, 3, 6, 2, 5]
        ],
        'expected': {9, 7, 6, 5, 4, 3, 10}
    }
}

sol = Solution()
for ex in examples:
    input_ex, expected = examples[ex]['input'], examples[ex]['expected']
    print(
        'Ref..: %s:\n\tExp: %s\n\tRes: %s' % (
            input_ex,
            expected,
            sol.maximized_array(input_ex[0], input_ex[1])
        )
    )
    print()
# ----------------------------------------------------------------------------------------------------------------------
