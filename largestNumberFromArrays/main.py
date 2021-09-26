# You’re given two integer arrays (n and m), and an integer k. Using the digits from n and m, return the largest
# number you can of length k.
#
# Example:
# n = [3,4,6,5]
# m = [9,0,2,5,8,3]
# k = 5
# $ maxNum(n, m, k)
# $ 98653
# ----------------------------------------------------------------------------------------------------------------------


import heapq
from typing import List
# ----------------------------------------------------------------------------------------------------------------------


class Solution:
    def max_num_ref(self, n: List[int], m: List[int], k: int) -> int:
        heap_arr = []
        heapq.heapify(heap_arr)

        def add_to_heap(h: List[int], elem: int, k: int):
            if len(h) < k:
                heapq.heappush(h, elem)
            elif elem > h[0]:
                heapq.heapreplace(h, elem)

        for elem in n:  # n * log(k)
            add_to_heap(heap_arr, elem, k)

        for elem in m:  # m * log(k)
            add_to_heap(heap_arr, elem, k)

        result = 0
        cnt = 1

        while len(heap_arr) > 0:  # summation log(k) 1 to k = log(k!)
            result += heapq.heappop(heap_arr) * cnt
            cnt *= 10

        return result
# ----------------------------------------------------------------------------------------------------------------------


examples = [
    {
        'n': [3, 4, 6, 1],
        'm': [9, 0, 2, 5, 8, 3],
        'k': 5,
        'resp': 98653,
    },
    {
        'n': [],
        'm': [],
        'k': 5,
        'resp': 0,
    },
    {
        'n': [1],
        'm': [],
        'k': 5,
        'resp': 1,
    },
    {
        'n': [1, 1, 1, 1, 2],
        'm': [],
        'k': 5,
        'resp': 21111,
    },
]

sol = Solution()
for ex in examples:
    print('Ref...: %s -> %s : %s' % (str(ex), sol.max_num_ref(ex['n'], ex['m'], ex['k']), ex['resp']))
    print()
# ----------------------------------------------------------------------------------------------------------------------
