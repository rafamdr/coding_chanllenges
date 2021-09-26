# Given a string of brackets, return a rotation of those brackets that is balanced. The numbers of opening and
# closing brackets will always be equal, so [ or ][] won’t be given as inputs.
#
# Example:
# $ rotateBrackets(‘]][][[‘)
# $ ‘[[]][]’ // First rotation yields ‘[]][][‘. Second one yields ‘[[]][]’.
# []          ->  []
# ]][[        ->  [[]]
# [][]][      ->  [[][]]
# ][][[]      ->  [[]][] OR [][[]]
# [[[][][]]]  ->  [[[][][]]]
# ]]][][][[[  ->  [[[]]][][] OR [][[[]]][] OR [][][[[]]]
# ----------------------------------------------------------------------------------------------------------------------


class Solution:
    def _check_brackets(self, text):
        stack = []
        for i, ch in enumerate(text):
            if ch == '[':
                stack.append(ch)
            elif len(stack) > 0:
                stack.pop()
            else:
                return False
        return len(stack) == 0

    def rotate_brackets_ref(self, text: str) -> str:
        count_rot = 0
        text_temp = text
        test_rot = self._check_brackets(text_temp)
        while count_rot < len(text) and test_rot is False:
            text_temp = text_temp[-1] + text_temp[:-1]
            test_rot = self._check_brackets(text_temp)
            count_rot += 1
        return text_temp

    def rotate_brackets_faster(self, text: str) -> str:
        stack = []
        count_wrong = 0
        for ch in text:
            if ch == '[':
                stack.append(ch)
            elif len(stack) > 0:
                stack.pop()
            else:
                count_wrong += 1
        count_wrong = -count_wrong if text[-1] == '[' else count_wrong
        return text[count_wrong:] + text[:count_wrong]

# ----------------------------------------------------------------------------------------------------------------------


examples = {
    ']][][[': {'[[]][]'},
    '][]][[': {'[[][]]'},
    '[]': {'[]'},
    ']][[': {'[[]]'},
    '[][]][': {'[[][]]'},
    '][][[]': {'[[]][]', '[][[]]'},
    '[[[][][]]]': {'[[[][][]]]'},
    ']]][][][[[': {'[[[]]][][]', '[][[[]]][]', '[][][[[]]]'},
}

sol = Solution()
for ex in examples:
    res = sol.rotate_brackets_ref(ex)
    if res in examples[ex]:
        exp = res
    else:
        exp = 'None'
    print('Ref...: %s -> %s : %s' % (ex, exp, res))

    res = sol.rotate_brackets_faster(ex)
    if res in examples[ex]:
        exp = res
    else:
        exp = 'None'
    print('Opt1..: %s -> %s : %s' % (ex, exp, res))
# ----------------------------------------------------------------------------------------------------------------------
