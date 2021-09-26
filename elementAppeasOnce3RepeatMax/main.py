# Given an array where every element occurs three times, except one element which occurs only once. Find the element
# that occurs once. Expected time complexity is O(n) and O(1) extra space.
#
# Examples:
#
# Input: arr[] = {12, 1, 12, 3, 12, 1, 1, 2, 3, 3}
# Output: 2
# In the given array all element appear three times except 2 which appears once.
#
# Input: arr[] = {10, 20, 10, 30, 10, 30, 30}
# Output: 20
# In the given array all element appear three times except 20 which appears once.
# ----------------------------------------------------------------------------------------------------------------------


from typing import List
import collections
# ----------------------------------------------------------------------------------------------------------------------


class Solution:
    def appears_one_k_repeat_ref(self, t: List[int], r: int) -> int:
        window = {}
        for item in t:
            if item not in window:
                window[item] = 1
            else:
                window[item] += 1
                if window[item] >= r:
                    del window[item]


        return 0
# ----------------------------------------------------------------------------------------------------------------------


examples = [
    {
        't': [12, 1, 12, 3, 12, 1, 1, 2, 3, 3],
        'r': 3,
        'resp': 2,
    },

    {
        't': [10, 20, 10, 30, 10, 30, 30],
        'r': 3,
        'resp': 20,
    },
]

sol = Solution()
for ex in examples:
    print('Ref...: %s -> %s : %s' % (str(ex), sol.appears_one_k_repeat_ref(ex['t'], ex['r']), ex['resp']))
    print()
# ----------------------------------------------------------------------------------------------------------------------
