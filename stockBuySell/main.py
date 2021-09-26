# Given an array of numbers that represent stock prices (where each number is the price for a certain day),
# find 2 days when you should buy and sell your stock for the highest profit.
#
# Example:
#
# $ stockBuySell([110, 180, 260, 40, 310, 535, 695])
# $ “buy on day 4, sell on day 7”
# ----------------------------------------------------------------------------------------------------------------------


import heapq
import sys
from typing import List
from functools import cmp_to_key
# ----------------------------------------------------------------------------------------------------------------------


class Solution:
    def stock_buy_sell_naive(self, array: List[int]):
        # O(n^2)
        buy_day = 0
        sell_day = 0
        for i in range(0, len(array) - 1):
            for j in range(i + 1, len(array)):
                if (array[j] - array[i]) > (array[sell_day] - array[buy_day]):
                    buy_day = i
                    sell_day = j
        return [buy_day, sell_day]

    def stock_buy_sell_fast_version1(self, array: List[int]):
        # O(n)
        left = 0
        right = 1
        buy_day = 0
        sell_day = 1
        if len(array) < 2:
            return [0, 0]

        while left < len(array):
            if left + 1 < len(array) and array[left + 1] < array[left] and array[left + 1] < array[buy_day]:
                left += 1
            elif right + 1 < len(array) and array[right + 1] < array[buy_day]:
                left = right
                right += 1
            elif right + 1 < len(array) and array[right + 1] > array[right] and array[right + 1] > array[sell_day]:
                right += 1
            elif right < len(array):
                right += 1
            else:
                left += 1

            if (
                (right > left) and
                (left < len(array)) and
                (right < len(array)) and
                (array[right] - array[left]) > (array[sell_day] - array[buy_day])
            ):
                buy_day = left
                sell_day = right

        if buy_day >= sell_day or array[sell_day] - array[buy_day] <= 0:
            return [0, 0]

        return [buy_day, sell_day]

    def stock_buy_sell_fast_version2(self, array: List[int]):
        best_lo = 0
        best_hi = 0
        current_lo = best_lo
        current_hi = best_hi
        for i in range(1, len(array)):
            if array[i] > array[current_hi]:
                current_hi = i
                if (array[current_hi] - array[current_lo]
                        > array[best_hi] - array[best_lo]):
                    best_lo = current_lo
                    best_hi = current_hi
            elif array[i] < array[current_lo] and i < len(array) - 1:
                current_lo = i
                current_hi = i
        return best_lo, best_hi

    def stock_buy_sell_fast_version3(self, array: List[int]):
        i = len(array) - 1
        high_idx, low_idx = i, i
        window_high, window_low = i, i
        largest_diff = 0
        while i >= 0:
            window_low = i
            if array[i] > array[window_high]:
                window_high = i

            current_diff = array[window_high] - array[window_low]
            if current_diff > largest_diff:
                high_idx = window_high
                low_idx = window_low
                largest_diff = array[window_high] - array[window_low]

            i -= 1
        return low_idx, high_idx
# ----------------------------------------------------------------------------------------------------------------------


examples = [
    [0, 8, -1,  9],
    [0, 0, 0, 0],
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [-4, -3],
    [1, 2, 3, 4, 5],
    [4, 7, 1, 2, 11],
    [5, 7, 2, 7, 3, 3, 5, 3, 0],
    [7, 6, 4, 3, 1],
    [1, 2, 4, 2, 5, 7, 2, 4, 9, 0],
    [3, 3, 5, 0, 0, 3, 1, 4],
    [3, 2, 6, 5, 0, 3],
    [2, 1, 2, 0, 1],
    [2, 4, 1],
    [2, 1, 4],
    [],
    [15],
    [110, 180, 260, 40, 310, 535, 695],
    [7, 1, 5, 3, 6, 4],
    [7, 6, 4, 3, 1],
]

sol = Solution()

for ex in examples:
    print('Naive: %s -> %s ' % (str(ex), str(sol.stock_buy_sell_naive(ex))))
    print('Fast1: %s -> %s ' % (str(ex), str(sol.stock_buy_sell_fast_version1(ex))))
    print('Fast2: %s -> %s ' % (str(ex), str(sol.stock_buy_sell_fast_version2(ex))))
    print('Fast3: %s -> %s ' % (str(ex), str(sol.stock_buy_sell_fast_version3(ex))))
    print()
# ----------------------------------------------------------------------------------------------------------------------
