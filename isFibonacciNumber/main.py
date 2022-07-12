# Given a Fibonacci number, give the previous Fibonacci number. If the number given is not a Fibonacci number, return -1
# ----------------------------------------------------------------------------------------------------------------------
import math


# ----------------------------------------------------------------------------------------------------------------------


class Fibonacci:
    def __init__(self):
        self._denominator = ((1 + math.sqrt(5))/2.0)

    def _is_perfect_int_square(self, number: int) -> bool:
        root = math.isqrt(number)
        return (root * root) == number

    def is_fibonacci_number(self, number: int) -> bool:
        # `number` is Fibonacci if and only if one or both of (5*n2 + 4) or (5*n2 – 4) is a perfect square
        temp_calc = 5 * (number * number)
        return (
            self._is_perfect_int_square(temp_calc + 4) or
            self._is_perfect_int_square(temp_calc - 4)
        )

    def previous_fibonacci(self, number: int):
        # The ratio of two adjacent numbers in the Fibonacci series rapidly approaches ((1 + sqrt(5)) / 2). So if N is
        # divided by ((1 + sqrt(5)) / 2) and then rounded, the resultant number will be the previous Fibonacci number.
        if self.is_fibonacci_number(number):
            return round(number / self._denominator)
        return -1
# ----------------------------------------------------------------------------------------------------------------------


examples = {
    -345: -1,
    0: 0,
    13: 8,
    8: 5,
    6: -1,
}

sol = Fibonacci()
for ex in examples:
    print('Ref..: %s -> %d : %d ' % (ex, examples[ex], sol.previous_fibonacci(ex)))
    print()
# ----------------------------------------------------------------------------------------------------------------------
