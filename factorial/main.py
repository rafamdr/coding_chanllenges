# ----------------------------------------------------------------------------------------------------------------------


class Solution:
    def rec_factorial(self, number: int):
        if number == 1:
            return 1
        else:
            return number * self.rec_factorial(number - 1)

    def it_factorial(self, number: int):
        res = 1
        for i in range(2, number + 1):
            res *= i
        return res
# ----------------------------------------------------------------------------------------------------------------------


sol = Solution()
examples = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for ex in examples:
    print('Rec: %d! = %d' % (ex, sol.rec_factorial(ex)))
    print('It: %d! = %d' % (ex, sol.it_factorial(ex)))
# ----------------------------------------------------------------------------------------------------------------------
