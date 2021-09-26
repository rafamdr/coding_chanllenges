# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
# Example:
#
# $ formParens(1)
# $ ["()"]
#
# $ formParens(3)
# $ ["((()))","(()())","(())()","()(())","()()()"]

# ----------------------------------------------------------------------------------------------------------------------
from typing import List


def form_parens_ref(num_parens: int) -> List[str]:
    if num_parens <= 0:
        return []
    result = {"()"}
    for i in range(1, num_parens):
        temp_set = set()
        for elem in result:
            temp_set.update(['()' + elem, '(' + elem + ')', elem + '()'])
        result = temp_set
    return list(result)
# ----------------------------------------------------------------------------------------------------------------------


def form_parens_v1(num_parens: int) -> List[str]:
    result = {"()"}
    for i in range(1, num_parens):
        temp_set = set()
        for elem in result:
            temp_set.update(['()' + elem, '(' + elem + ')', elem + '()'])
        result = temp_set
    return list(result) if num_parens >= 1 else []
# ----------------------------------------------------------------------------------------------------------------------


examples = {
    0: [],
    1: ["()"],
    2: ["(())", "()()"],
    3: ["((()))", "(()())", "(())()", "()(())", "()()()"],
    4: ['()()(())', '(((())))', '(()()())', '()(()())', '()((()))', '((()()))', '(()(()))', '()()()()'],
}

for ex in examples:
    # print('Ref..: %d = %s -> %s' % (ex, examples[ex], form_parens_ref(ex)))
    print('v1...: %d = %s -> %s' % (ex, examples[ex], form_parens_v1(ex)))
# ----------------------------------------------------------------------------------------------------------------------
