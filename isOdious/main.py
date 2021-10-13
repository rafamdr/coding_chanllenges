# An “odious number” is a non-negative number that has an odd number of 1s in its binary expansion. Write a function
# that returns true if a given number is odious.
#
# Example:
#
# $ isOdious(14)
# $ true
#
# $ isOdious(5)
# $ false
# ----------------------------------------------------------------------------------------------------------------------


import sys
# ----------------------------------------------------------------------------------------------------------------------


class Solution:
    def is_odious(self, num: int) -> bool:
        if num < 0:
            return False
        # Counting bits: https://tinyurl.com/nzs6hx4w
        if sys.maxsize > 2 ** 32:  # is 64 bit system?
            coef = [0x5555555555555555, 0x3333333333333333,
                    0x0f0f0f0f0f0f0f0f, 0x0101010101010101, 56]
        else:
            coef = [0x55555555, 0x33333333,
                    0x0F0F0F0F, 0x01010101, 24]
        num = num - ((num >> 1) & coef[0])
        num = (num & coef[1]) + ((num >> 2) & coef[1])
        num = (num + (num >> 4)) & coef[2]
        count = (num * coef[3]) >> coef[4]
        return count & 1 == 1
# ----------------------------------------------------------------------------------------------------------------------


examples = {
    14: True,
    5: False,
    1: True,
    0: False
}

sol = Solution()
for ex in examples:
    print('Ref..: %d -> %s : %s' % (ex, examples[ex], str(sol.is_odious(ex))))
# ----------------------------------------------------------------------------------------------------------------------
