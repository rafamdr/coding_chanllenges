import math
from functools import reduce
from typing import List
# ----------------------------------------------------------------------------------------------------------------------


class Solution:
    def gimme_pizza(self, arr: List, pizza_slices: int) -> int:
        return math.ceil(reduce(lambda amount, item: amount + item['num'], arr, 0) / pizza_slices)
# ----------------------------------------------------------------------------------------------------------------------


sol = Solution()
print(sol.gimme_pizza([], 8))
print(sol.gimme_pizza([{'name': 'Cassidy', 'num': 4}], 8))
print(sol.gimme_pizza([{'name': 'Joe', 'num': 9}, {'name': 'Cami', 'num': 3}, {'name': 'Cassidy', 'num': 4}], 8))
print(sol.gimme_pizza([{'name': 'Joe', 'num': 9}, {'name': 'Cami', 'num': 4}, {'name': 'Cassidy', 'num': 4}], 8))
print(sol.gimme_pizza([{'name': 'Joe', 'num': 9}, {'name': 'Cami', 'num': 4}, {'name': 'Cassidy', 'num': 4}], 1))
# ----------------------------------------------------------------------------------------------------------------------
