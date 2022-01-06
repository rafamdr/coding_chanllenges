# You’re in charge of the fireworks display, and you have a list of fireworks to shoot off. You want to make sure you
# don’t fire the same colors twice in a row. Given an array of fireworks, return a valid firing order. You decide how
# you want an impossible solution to work!
#
# Example:
#
# $ orderFireworks(['green','green','green','red','red','blue'])
# $ ['green','red','green','red','green','blue']
# ----------------------------------------------------------------------------------------------------------------------
import heapq
from typing import List
import re
from collections import Counter, defaultdict


# ----------------------------------------------------------------------------------------------------------------------


class Solution:
    def order_fireworks_v1(self, colors: List[str]) -> List[str]:
        histogram_descend = list(sorted(Counter(colors).items(), key=lambda item: item[1], reverse=True))
        last_color = None
        used_idx = 0
        result = []
        while len(histogram_descend) > 0:
            color, freq = histogram_descend[used_idx]
            if last_color == color:
                return []
            result.append(color)
            last_color = color
            if (freq - 1) > 0:
                histogram_descend[used_idx] = (color, freq - 1)
                used_idx = (used_idx + 1) % len(histogram_descend)
            else:
                del histogram_descend[used_idx]
                used_idx = 0
        return result

    def order_fireworks_v2(self, colors: List[str]) -> List[str]:
        heapq.heapify(max_heap := [(-pair[1], pair[0]) for pair in Counter(colors).items()])
        saved_item = None
        result = []
        while len(max_heap) > 0:
            if saved_item:
                neg_freq, color = heapq.heapreplace(max_heap, saved_item)
                saved_item = None
            else:
                neg_freq, color = heapq.heappop(max_heap)
            freq = -neg_freq
            result.append(color)
            if (freq - 1) > 0:
                saved_item = (-(freq - 1), color)
        return result if saved_item is None else []
# ----------------------------------------------------------------------------------------------------------------------


examples = {
    'ex1': {
        'array': ['red', 'red', 'blue', 'green', 'green', 'green'],
        'expected': True
    },

    'ex2': {
        'array': ['green', 'green', 'green', 'red', 'red', 'blue', 'blue'],
        'expected': True
    },

    'ex3': {
        'array': ['green', 'green', 'green', 'red', 'red', 'blue', 'blue', 'blue'],
        'expected': True
    },

    'ex4': {
        'array': ['green', 'green', 'green'],
        'expected': False
    },

    'ex5': {
        'array': ['blue', 'green', 'green', 'green'],
        'expected': False
    },

    'ex6': {
        'array': [],
        'expected': False
    },
}


def check_result(array: List[str]):
    if len(array) == 0:
        return False
    for i in range(1, len(array)):
        if array[i] == array[i - 1]:
            return False
    return True


def print_specific_solution_result(in_array: List[str], expected: bool, method):
    result = method(in_array.copy())
    check_result(result)
    print('%s..:\n%s:\n[%s <==> %s] \nRes: %s\n' % (method.__name__, in_array, expected, check_result(result), result))


sol = Solution()
for ex in examples:
    examp = examples[ex]
    print_specific_solution_result(examp['array'], examp['expected'], sol.order_fireworks_v1)
    print_specific_solution_result(examp['array'], examp['expected'], sol.order_fireworks_v2)
# ----------------------------------------------------------------------------------------------------------------------
