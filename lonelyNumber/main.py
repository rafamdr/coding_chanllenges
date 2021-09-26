# Given three numbers, return their product. But, if one of the numbers is the same as another, it does not count: If
# two numbers are similar, return the lonely number. If all numbers are same, return 1.
#
# Example:
#
# $ lonelyNumber(1,2,3)
# $ 6
#
# $ lonelyNumber(6,6,4)
# $ 4
#
# $ lonelyNumber(7,7,7)
# $ 1
# ----------------------------------------------------------------------------------------------------------------------


from collections import Counter
# ----------------------------------------------------------------------------------------------------------------------


class Solution:
    def lonely_number_ref(self, a: int, b: int, c: int) -> int:
        if a != b:
            if b != c:
                if a != c:
                    return a * b * c
                else:
                    return b
            else:
                return a
        else:
            if b != c:
                return c
            else:
                return 1

    def lonely_number_opt1(self, a: int, b: int, c: int) -> int:
        if a != b:
            return (a*b*c if a != c else b) if b != c else a
        else:
            return c if b != c else 1

    def lonely_number_opt2(self, a: int, b: int, c: int) -> int:
        arr = sorted([a, b, c])
        if arr[0] == arr[1]:
            return 1 if arr[1] == arr[2] else arr[2]
        elif arr[1] == arr[2]:
            return arr[0]
        return a * b * c
# ----------------------------------------------------------------------------------------------------------------------


examples = {
    tuple([1, 2, 3]): 6,
    tuple([6, 6, 4]): 4,
    tuple([4, 6, 6]): 4,
    tuple([6, 4, 6]): 4,
    tuple([7, 7, 7]): 1,
}

sol = Solution()
for ex in examples:
    print('Ref..: %s = %s <-> %s' % (ex, examples[ex], sol.lonely_number_ref(ex[0], ex[1], ex[2])))
    print('Opt1.: %s = %s <-> %s' % (ex, examples[ex], sol.lonely_number_opt1(ex[0], ex[1], ex[2])))
    print('Opt2.: %s = %s <-> %s' % (ex, examples[ex], sol.lonely_number_opt2(ex[0], ex[1], ex[2])))
    print()
# ----------------------------------------------------------------------------------------------------------------------
