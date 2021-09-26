# In this problem, we are given two string one text of size n and other a pattern of size m. Our task is to create a
# program for Anagram substring search.
#
# Here, we have to find all the occurrence of pattern and all its permutations (anagrams) in the text.
#
# Let’s take an example to understand the problem,
#
# Input
# text = "cbabadcbbabbcbabaabccbabc" pattern = "abbc"
# ----------------------------------------------------------------------------------------------------------------------


from typing import List
import collections
# ----------------------------------------------------------------------------------------------------------------------


class Solution:
    def anagram_substr_search_ref(self, t: str, p: str) -> List[int]:
        result = []
        POSSIBLE_CHARS = 256
        t_arr = [0] * POSSIBLE_CHARS
        p_arr = [0] * POSSIBLE_CHARS
        for i in range(len(p)):
            p_arr[ord(p[i])] += 1
            t_arr[ord(t[i])] += 1

        for i in range(len(p), len(t)):
            if p_arr == t_arr:
                result.append(i - len(p))
            t_arr[ord(t[i])] += 1
            t_arr[ord(t[i - len(p)])] -= 1

        if collections.Counter(p_arr) == collections.Counter(t_arr):
            result.append(len(t) - len(p))

        return result
# ----------------------------------------------------------------------------------------------------------------------


examples = [
    {
        't': 'cbabadcbbabbcbabaabccbabc',
        'p': 'abbc',
        'resp': 0,
    },
]

sol = Solution()
for ex in examples:
    print('Ref...: %s -> %s : %s' % (str(ex), sol.anagram_substr_search_ref(ex['t'], ex['p']), ex['resp']))
    print()
# ----------------------------------------------------------------------------------------------------------------------
