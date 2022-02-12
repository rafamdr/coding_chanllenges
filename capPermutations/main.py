# Given a string s, you can transform every letter individually to be lowercase or uppercase. Return a list of all
# possible permutations you could create from s.
#
# Example:
#
# $ capPermutations("ab2")
# $ ["ab2","aB2","Ab2","AB2"]
#
# $ capPermutations("35p")
# $ ["35p","35P"]
# ----------------------------------------------------------------------------------------------------------------------


from typing import List
from collections import Counter, defaultdict
# ----------------------------------------------------------------------------------------------------------------------


class Solution:
    def cap_permutations_v1(self, text: str, sort_result=False) -> List[str]:
        if len(text) == 0:
            return []
        else:
            result = {text[0].lower() + text[1:], text[0].upper() + text[1:]}
        for idx in range(1, len(text)):
            result_bkp = list(result.copy()) + list(result.copy())
            for item in result_bkp:
                result.add(item[:idx] + item[idx].lower() + item[idx + 1:])
                result.add(item[:idx] + item[idx].upper() + item[idx + 1:])
        return sorted(list(result), reverse=True) if sort_result else list(result)

    def cap_permutations_v2(self, text: str, sort_result=False) -> List[str]:
        result = []
        if len(text) > 0:
            result = {text[0].lower() + text[1:], text[0].upper() + text[1:]}
        for idx in range(1, len(text)):
            result_bkp = list(result.copy()) * 2
            for item in result_bkp:
                result.add(item[:idx] + item[idx].lower() + item[idx + 1:])
                result.add(item[:idx] + item[idx].upper() + item[idx + 1:])
        return sorted(list(result), reverse=True) if sort_result else list(result)

    def cap_permutations_v3(self, text: str, sort_result=False) -> List[str]:
        result = []
        if len(text) > 0:
            result = {text[0].lower() + text[1:], text[0].upper() + text[1:]}
        for idx in range(1, len(text)):
            new_combinations = list(result.copy()) * 2
            for item in new_combinations:
                before, after, low, cap = item[:idx], item[idx + 1:], item[idx].lower(), item[idx].upper()
                result.update([before + low + after, before + cap + after])
        return sorted(list(result), reverse=True) if sort_result else list(result)
# ----------------------------------------------------------------------------------------------------------------------


examples = {
    'abc': ['abc', 'abC', 'aBc', 'aBC', 'Abc', 'AbC', 'ABc', 'ABC'],
    'ab2': ["ab2", "aB2", "Ab2", "AB2"],
    '35p': ["35p", "35P"],
    '': [],
    '123': ['123'],
    '123a': ['123a', '123A'],
}

sol = Solution()
for ex in examples:
    examp = examples[ex]
    print('V1..:\t%s -> %s : %s' % (ex, examp, sol.cap_permutations_v1(ex, True)))
    print('V2..:\t%s -> %s : %s' % (ex, examp, sol.cap_permutations_v2(ex, True)))
    print('V3..:\t%s -> %s : %s' % (ex, examp, sol.cap_permutations_v3(ex, True)))
    print()
# ----------------------------------------------------------------------------------------------------------------------
