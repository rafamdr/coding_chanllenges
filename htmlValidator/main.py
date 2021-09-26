# Given a string that is an HTML-like code snippet, return whether or not the tags are valid.
#
# Examples:
# $ htmlValidator('<tag>I love coding <Component />!</tag>')
# $ true
# ----------------------------------------------------------------------------------------------------------------------


from typing import Tuple
import re
# ----------------------------------------------------------------------------------------------------------------------


class Solution:
    def _get_next_idx(self, expr: str, start: int) -> Tuple[int, int]:
        start_idx = -1
        idx = -1
        start_idx = expr.find('<', start)
        if start_idx != -1:
            start_idx += 1
            idx = expr.find('>', start_idx)
        return start_idx, idx

    def _parse(self, expression: str) -> bool:
        stack_expr = []
        start_idx = 0
        while start_idx != -1:
            start_idx, idx = self._get_next_idx(expression, start_idx)
            stringosa = expression[start_idx:idx]
            if start_idx != -1:
                if re.match(r'.+/', stringosa):
                    pass
                elif len(stack_expr) > 0 and re.match(stack_expr[-1], stringosa):
                    stack_expr.pop()
                else:
                    stack_expr.append(r'[ ]*/[ ]*%s[ ]*' % stringosa)
        return len(stack_expr) == 0

    def html_validator(self, expression: str) -> int:
        return self._parse(expression)
# ----------------------------------------------------------------------------------------------------------------------


examples = [
    #'<tag>I love coding <Component />!</tag>',
    '<DIV>  unmatched <  </DIV>'
]
sol = Solution()
for ex in examples:
    print('Ref.: %s -> %s ' % (str(ex), sol.html_validator(ex)))
    print()
# ----------------------------------------------------------------------------------------------------------------------
