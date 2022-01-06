# Given an array of strings, group the anagrams together in separate arrays. An anagram is a word or phrase formed by
# rearranging the letters of another word or phrase, using all the original letters exactly once.
#
# Example:
#
# $ groupAnagrams(["eat","tea","ten","poop","net","ate"])
# $ [["poop"],["net","ten"],["eat","tea","ate"]]
# ----------------------------------------------------------------------------------------------------------------------


from typing import List
from collections import Counter, defaultdict
# ----------------------------------------------------------------------------------------------------------------------


class Solution:
    def group_anagrams_v1(self, words: List[str]) -> List[List[str]]:
        result = {}
        for word in words:
            item = frozenset(Counter(word).items())
            result[item] = [word] if item not in result else result[item] + [word]
        return list(result.values())

    def group_anagrams_v2(self, words: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for word in words:
            result[frozenset(Counter(word).items())].append(word)
        return list(result.values())
# ----------------------------------------------------------------------------------------------------------------------


examples = {
    'ex1': {
        'array': ["eat", "tea", "ten", "poop", "net", "ate"],
        'expected': [["poop"], ["net", "ten"], ["eat", "tea", "ate"]]
    },

    'ex2': {
        'array': ["eat", "tea", "ten", "pop", "poop", "net", "ate"],
        'expected': [["pop"], ["poop"], ["net", "ten"], ["eat", "tea", "ate"]]
    },

    'ex3': {
        'array': [],
        'expected': []
    },
}

sol = Solution()
for ex in examples:
    examp = examples[ex]
    print('V1..:\t%s ->%s : %s' % (examp['array'], examp['expected'], sol.group_anagrams_v1(examp['array'].copy())))
    print('V2..:\t%s ->%s : %s' % (examp['array'], examp['expected'], sol.group_anagrams_v2(examp['array'].copy())))
# ----------------------------------------------------------------------------------------------------------------------
