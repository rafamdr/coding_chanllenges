# This week’s question is brought to you by Stytch!
# Given two strings n and m, return true if they are equal when both are entered into text editors. But: a # means a
# backspace character (deleting backwards), and a % means a delete character (deleting forwards).
#
# Example:
#
# > equalWithDeletions("a##x", "#a#x")
# > true      // both strings become "x"
#
# > equalWithDeletions("fi##f%%%th %%year #time###", "fifth year time")
# > false     // the first string becomes "fart"
# ----------------------------------------------------------------------------------------------------------------------

from typing import List, Dict
# ----------------------------------------------------------------------------------------------------------------------


class Solution:

    def equal_with_deletions(self, n: str, m: str) -> bool:
        def process_dels(text: str) -> []:
            forward, result = 0, []
            for ch in text:
                if forward > 0:
                    forward -= 1
                elif ch == '%':
                    forward += 1
                elif ch == '#':
                    if len(result) > 0:
                        result.pop()
                else:
                    result += ch
            return result
        return process_dels(n) == process_dels(m)

    def equal_with_deletions_v2(self, n: str, m: str) -> bool:
        def process_dels(text: str) -> []:
            forward, result = 0, []
            for ch in text:
                if forward > 0:
                    forward -= 1
                elif ch == '%':
                    forward += 1
                elif ch == '#':
                    if len(result) > 0:
                        result.pop()
                else:
                    result += ch
            return result


        processed_word = process_dels(n)

        forward, equals, different = 0, 0
        for ch in m:
            if forward > 0:
                forward -= 1
            elif ch == '%':
                forward += 1
            elif ch == '#':
                equals = equals - 1 if 0 < equals < len(processed_word) else equals
            elif equals < len(processed_word):
                if processed_word[equals] == ch:
                    equals += 1
                else:
                    equals = 0

        return equals > 0
# ----------------------------------------------------------------------------------------------------------------------


examples = {
    # ("", ""): True,
    # ("", "###"): True,
    # ("###", "###"): True,
    # ("a##x", "#a#x"): True,
    # ("a##xb#bz", "#a#xbzz#"): True,
    # ("abcd", "abcd"): True,
    ("abcd", "abcc#d"): True,
    ("fi##f%%%th %%year #time###", "fifth year time"): False
}

sol = Solution()
for ex in examples:
    input_n, input_m = ex
    print('Ref..: %s <-> %s == %s' % (ex, examples[ex], sol.equal_with_deletions(input_n, input_m)))
    print('V2...: %s <-> %s == %s' % (ex, examples[ex], sol.equal_with_deletions_v2(input_n, input_m)))
    print()
# ----------------------------------------------------------------------------------------------------------------------
