# Given a string expression with the symbols T for true, F for false, & for AND, | for OR, and ^ for XOR,
# count the number of ways we can parenthesize the expression so that its value evaluates to true.
#
# Example:
#
# $ evaluateExp('T|T&F^T')
# $ 4 // ((T|T)&(F^T)), (T|(T&(F^T))), (((T|T)&F)^T) and (T|((T&F)^T))
# ----------------------------------------------------------------------------------------------------------------------


from typing import List, Tuple
import re


# ----------------------------------------------------------------------------------------------------------------------


class Solution:
    def _get_next_idx(self, expr: str) -> Tuple[int, int]:
        start_index = 0
        if match := re.match(r"([T|F][|&^]+[T|F])", expr[start_index:]):
            group = match.group()

            return 0, 0

        return -1, -1

    def evaluate_exp(self, expression: str) -> List[str]:
        start_idx, idx = self._get_next_idx(expression)
        stringosa = expression[start_idx:idx]
        return []


# ----------------------------------------------------------------------------------------------------------------------


examples = {
    'T|T&F^T': {'((T|T)&(F^T))', '(T|(T&(F^T)))', '(((T|T)&F)^T)', '(T|((T&F)^T))'}
}

sol = Solution()
for ex in examples:
    print('Ref..: %s -> %s : %s ' % (ex, examples[ex], str(sol.evaluate_exp(ex))))
    print()
# ----------------------------------------------------------------------------------------------------------------------
"""

T|T     T&F     F^T                  
true    false   true

T|






"""