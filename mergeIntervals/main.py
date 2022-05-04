# Given an array of intervals, merge the overlapping intervals, and return an array of the resulting intervals.
#
# Example:
#
# $ mergeIntervals([[1,4],[2,6],[8,10],[15,20]])
# $ [[1,6],[8,10],[15,20]]
#
# $ mergeIntervals([[1,2],[2,7]])
# $ [[1,7]]
# ----------------------------------------------------------------------------------------------------------------------
import heapq
from typing import List
from collections import deque
# ----------------------------------------------------------------------------------------------------------------------


class Solution:
    def merge_intervals(self, array: List[List[int]]) -> List[List[int]]:
        heapq.heapify(array)  # O(n)
        result = [heapq.heappop(array)] if len(array) > 0 else []
        while array:  # O(n log n)
            new_interval = heapq.heappop(array)
            if new_interval[0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], new_interval[1])
            else:
                result.append(new_interval)
        return result

    def merge_sorted_intervals(self, array: List[List[int]]) -> deque[List[List[int]]]:
        result = deque([array.pop()]) if len(array) > 0 else deque([])
        while array:  # O(n)
            new_interval = array.pop()
            if new_interval[1] >= result[0][0]:
                result[0][0] = min(result[0][0], new_interval[0])
            else:
                result.appendleft(new_interval)
        return result
# ----------------------------------------------------------------------------------------------------------------------


examples = {
    'ex1': {
        'input': [[1, 4], [2, 6], [8, 10], [15, 20]],
        'expected': [[1, 6], [8, 10], [15, 20]],
    },
    'ex2': {
        'input': [[15, 20], [1, 4], [8, 10], [2, 6]],
        'expected': [[1, 6], [8, 10], [15, 20]],
    },
    'ex3': {
        'input': [[1, 2], [2, 7]],
        'expected': [[1, 7]],
    },
    'ex4': {
        'input': [[1, 2]],
        'expected': [[1, 2]],
    },
    'ex5': {
        'input': [],
        'expected': [],
    },
    'ex6': {
        'input': [[1, 4], [4, 6], [8, 10], [15, 20]],
        'expected': [[1, 6], [8, 10], [15, 20]],
    },
    'ex7': {
        'input': [[1, 4], [4, 6], [8, 10], [-15, 20]],
        'expected': [[-15, 20]],
    },
}

sol = Solution()
for ex in examples:
    input_ex, expected = examples[ex]['input'], examples[ex]['expected']
    print('Ref..: %s:\n%s\n%s' % (input_ex, expected, sol.merge_intervals(input_ex.copy())))
    print()
# ----------------------------------------------------------------------------------------------------------------------
