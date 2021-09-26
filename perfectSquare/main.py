# Given a positive integer n, write a function that returns true if it is a perfect square and false otherwise. Don’t
# use any built-in math functions like sqrt. Hint: Use binary search!
#
#
# Examples:
# $ perfectSquare(25)
# $ true
# $ perfectSquare(10) $ false
# ----------------------------------------------------------------------------------------------------------------------


import sys
# ----------------------------------------------------------------------------------------------------------------------


class Solution:
    def is_perfect_square_ref(self, number: int):
        if number < 0:
            return False
        if number <= 1:
            return True
        first = 2
        last = number // 2
        while first <= last:
            mid = first + (last - first) // 2
            squared = mid * mid
            if squared == number:
                return True
            elif squared > number:
                last = mid - 1
            else:
                first = mid + 1
        return False

    def cheating(self, n: int):
        if n < 0:
            return False
        r = n ** 0.5
        return r == int(r)
# ----------------------------------------------------------------------------------------------------------------------


examples = [
    16, 3, 0xFFFFFFFF4564, 40401, 121, 65536, 4,    9,    8,    63,    1,    0,    2,    25,    -1,    121
]
sol = Solution()
for ex in examples:
    print('Ref..: %d -> %s ' % (ex, str(sol.is_perfect_square_ref(ex))))
    print('Cheat.: %d -> %s ' % (ex, str(sol.cheating(ex))))
    print()
# ----------------------------------------------------------------------------------------------------------------------
