# Given a basic Lisp-like string expression, parse it (where the available functions are add, subtract, multiply,
# and divide, and they all take in 2 values).
#
# Examples:
# $ babyLisp(‘(add 1 2)’)
# $ 3
# $ babyLisp(‘(multiply 4 (add 2 3))’) $ 20
# ----------------------------------------------------------------------------------------------------------------------


from typing import Tuple
# ----------------------------------------------------------------------------------------------------------------------


class Solution:
    def __init__(self):
        self._set_seps = set([')', ' '])
        self._map_funcs = {
            '(': self._parenthesis_fn,
            'multiply': self._multiply_fn,
            'divide': self._divide_fn,
            'add': self._add_fn,
            'subtract': self._subtract_fn
        }

    def _get_next_idx(self, expr: str) -> Tuple[int, int]:
        start_idx = 0
        idx = 0
        while idx < len(expr) and expr[idx] in self._set_seps:
            start_idx += 1
            idx += 1
        if expr[idx] == '(':
            return start_idx, idx + 1
        while idx < len(expr) and expr[idx] not in self._set_seps:
            idx += 1
        return start_idx, idx

    def _parenthesis_fn(self, expression):
        return self._parse(expression)

    def _get_operands(self, expression):
        op1, expression = self._parse(expression)
        op2, expression = self._parse(expression)
        return op1, op2, expression

    def _multiply_fn(self, expression):
        op1, op2, expression = self._get_operands(expression)
        return op1 * op2, expression

    def _divide_fn(self, expression):
        op1, op2, expression = self._get_operands(expression)
        return op1 // op2, expression

    def _add_fn(self, expression):
        op1, op2, expression = self._get_operands(expression)
        return op1 + op2, expression

    def _subtract_fn(self, expression):
        op1, op2, expression = self._get_operands(expression)
        return op1 - op2, expression

    def _parse(self, expression: str) -> Tuple[int, str]:
        start_idx, idx = self._get_next_idx(expression)
        stringosa = expression[start_idx:idx]
        if stringosa in self._map_funcs:
            return self._map_funcs[stringosa](expression[idx:])
        else:
            return int(stringosa), expression[idx:]

    def baby_list_parse(self, expression: str) -> int:
        res, _ = self._parse(expression)
        return res
# ----------------------------------------------------------------------------------------------------------------------


examples = [
    '(add 1 2)',
    '(multiply 4 (add 2 3))',
    'multiply 4 (add 2 3)',
    'multiply (add 78 912) (divide (subtract 44 2) 2)',
    '(multiply (add 78 912) (divide (subtract 44 2) 2))',
    'divide (multiply (add 78 912) (divide (subtract 44 2) 2)) 2',
]
sol = Solution()
for ex in examples:
    print('Ref.: %s -> %s ' % (str(ex), sol.baby_list_parse(ex)))
    print()
# ----------------------------------------------------------------------------------------------------------------------
