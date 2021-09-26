# Given two non-negative integers n1 and n2 represented as strings, return the product of n1 and n2, also represented 
# as a string. Neither input will start with 0, and don’t just convert it to an integer and do the math that way.

# Examples:
# $ stringMultiply(“123”, “456”)
# $ “56088”
# ---------------------------------------------------------------------------------------------------------------------


from typing import List
from functools import reduce
# ---------------------------------------------------------------------------------------------------------------------


class Solution:
    def _op_str(self, number1: str, number2: str, subtract: bool) -> str:
        carrier = 0
        sum_op = ''
        for i in range(max(len(number1), len(number2))):
            d1 = int(number1[-1 - i]) if i < len(number1) else 0
            d2 = int(number2[-1 - i]) if i < len(number2) else 0
            if subtract:
                digit_sum = 10 * int(d1 - carrier < d2) + d1 - carrier - d2
                carrier = int(d1 - carrier < d2)
                sum_op = str(digit_sum) + sum_op
            else:
                digit_sum = d1 + d2 + carrier
                carrier = digit_sum // 10
                sum_op = str(digit_sum % 10) + sum_op
        return (str(carrier) + sum_op) if carrier != 0 else sum_op   

    def _add_str(self, number1: str, number2: str) -> str:
        return self._op_str(number1, number2, False)

    def _subtract_str(self, number1: str, number2: str) -> str:
        return self._op_str(number1, number2, True)

    def _add_multiple_str(self, numbers: List[str]) -> str:
        if len(numbers) == 0: return ''
        return reduce(lambda total, n: self._add_str(total, n), numbers[1:], numbers[0])

    def _subtract_multiple_str(self, numbers: List[str]) -> str:
        if len(numbers) == 0: return ''
        return reduce(lambda total, n: self._subtract_str(total, n), numbers[1:], numbers[0])    

    def multiply_str_ref(self, number1: str, number2: str) -> str:
        return str(int(number1) * int(number2))

    def multiply_str_naive(self, number1: str, number2: str) -> str:
        sum_array = []
        for i in range(len(number2)):
            sum_op = ''
            carrier = 0
            for j in range(len(number1)):
                digit_mult = (int(number2[-1 - i]) * int(number1[-1 - j])) + carrier
                carrier = digit_mult // 10
                sum_op = str(digit_mult % 10) + sum_op
            sum_op = (str(carrier) + sum_op) if carrier != 0 else sum_op
            sum_array.append(sum_op + ('0' * i))
        return self._add_multiple_str(sum_array)

    def multiply_str_karatsuba(self, number1: str, number2: str) -> str:
        if len(number1) == 1 and len(number2) == 1:
            return str(int(number1) * int(number2))
        if len(number1) < len(number2):
            number1 = ('0' * (len(number2) - len(number1))) + number1
        elif len(number2) < len(number1):
            number2 = ('0' * (len(number1) - len(number2))) + number2
        m = len(number1)
        m_half = m // 2 + int(m % 2 > 0)
        high1, low1 = number1[:m_half], number1[m_half:]
        high2, low2 = number2[:m_half], number2[m_half:]
        z0 = self.multiply_str_karatsuba(low1, low2)
        z1 = self.multiply_str_karatsuba(self._add_str(low1, high1), self._add_str(low2, high2))
        z2 = self.multiply_str_karatsuba(high1, high2)
        return self._add_multiple_str([
            (z2 + ('0' * (2 * (m - m_half)))),
            (self._subtract_multiple_str([z1, z2, z0]) + ('0' * (m - m_half))),
            z0
        ]).lstrip('0')
# ---------------------------------------------------------------------------------------------------------------------


def main():
    examples = {
        '56088':    [ '123',   '456'     ],
        # '192888':   [ '423',   '456'     ],        
        # '0':        [ '0',     '0'       ],
        # '4':        [ '2',     '2'       ], 
        # '151704':   [ '6321',  '24'      ],
        # '2740344':  [ '6',     '456724'  ],
        # '83810205': [ '12345', '6789'    ],
    }
    sol = Solution()
    for key in examples:
        ex = examples[key]
        print('Ref......: Exp = %s  ->  Res = %s' % (key, sol.multiply_str_ref(ex[0], ex[1])))
        print('Naive....: Exp = %s  ->  Res = %s' % (key, sol.multiply_str_naive(ex[0], ex[1])))
        print('Karatsuba: Exp = %s  ->  Res = %s' % (key, sol.multiply_str_karatsuba(ex[0], ex[1])))
        print()
# ---------------------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    main()
# ---------------------------------------------------------------------------------------------------------------------
