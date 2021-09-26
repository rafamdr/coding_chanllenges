# Given an integer n, return true if n^3 and n have the same set of digits.
#
# Example:
#
# $ sameDigits(1) // true
# $ sameDigits(10) // true
# $ sameDigits(251894) // true
# $ sameDigits(251895) // false
# ----------------------------------------------------------------------------------------------------------------------
import functools
from typing import List


class Solution:
    def _get_digits_set(self, num) -> List:
        digits_set = [False] * 10
        while num > 0:
            digits_set[num % 10] = True
            num = num // 10
        return digits_set

    def same_digits(self, num) -> bool:
        digits_set = self._get_digits_set(num)
        digits_pow_set = self._get_digits_set(num * num * num)
        return functools.reduce(lambda i, j: i and j, map(lambda m, k: m == k, digits_set, digits_pow_set), True)
# ----------------------------------------------------------------------------------------------------------------------


examples = {
    1: True,
    10: True,
    251894: True,
    251895: False,
}

sol = Solution()
for ex in examples:
    res = sol.same_digits(ex)
    print('Ref...: %d -> %s : %s' % (ex, str(examples[ex]), str(res)))
# ----------------------------------------------------------------------------------------------------------------------
