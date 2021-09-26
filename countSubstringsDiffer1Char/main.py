# Given two strings s and t, find the number of ways you can choose a non-empty substring of s and replace a single
# character by a different character such that the resulting substring is a substring of t. In other words,
# find the number of substrings in s that differ from some substring in t by exactly one character.
#
# For example, the underlined substrings in "computer" and "computation" only differ by the 'e'/'a', so this is a
# valid way.
#
# Return the number of substrings that satisfy the condition above.
#
# A substring is a contiguous sequence of characters within a string.
#
# Example 1:
#
# Input: s = "aba", t = "baba"
# Output: 6
# Explanation: The following are the pairs of substrings from s and t that differ by exactly 1 character:
# ("aba", "baba")
# ("aba", "baba")
# ("aba", "baba")
# ("aba", "baba")
# ("aba", "baba")
# ("aba", "baba")
# The underlined portions are the substrings that are chosen from s and t.
# Example 2:
# Input: s = "ab", t = "bb"
# Output: 3
# Explanation: The following are the pairs of substrings from s and t that differ by 1 character:
# ("ab", "bb")
# ("ab", "bb")
# ("ab", "bb")
# The underlined portions are the substrings that are chosen from s and t.
# Example 3:
# Input: s = "a", t = "a"
# Output: 0
# Example 4:
#
# Input: s = "abe", t = "bbc"
# Output: 10
#
# Constraints:
# 1 <= s.length, t.length <= 100
# s and t consist of lowercase English letters only.
# ----------------------------------------------------------------------------------------------------------------------


from collections import deque
from typing import List
# ----------------------------------------------------------------------------------------------------------------------


class Solution:
    def count_substrs_differ_1_char_naive(self, s: str, t: str) -> int:
        # Time complexity: S * S * T * T * S = S^3 * T^2
        # Space complexity: O(1)
        differ_one = 0

        def diff_strs(a: str, b: str):
            if len(a) != len(b):
                return -1
            idx, temp_diff = 0, 0
            while idx < len(a) and temp_diff < 2:
                if a[idx] != b[idx]:
                    temp_diff += 1
                idx += 1
            return temp_diff

        for i in range(len(s)):
            for j in range(i, len(s)):
                subs_s = s[i:j + 1]
                for m in range(len(t)):
                    for n in range(m, len(t)):
                        subs_t = t[m:n + 1]
                        if diff_strs(subs_s, subs_t) == 1:
                            differ_one += 1
        return differ_one

    def count_substrs_differ_1_char_cheaper(self, s: str, t: str) -> int:
        # Time complexity: S * T * MAX(S, T)
        # Space complexity: O(1)
        res = 0
        for i in range(len(s)):
            for j in range(len(t)):
                if s[i] != t[j]:
                    left, right = 1, 1
                    while i - left >= 0 and j - left >= 0 and s[i - left] == t[j - left]:
                        left += 1
                    while i + right < len(s) and j + right < len(t) and s[i + right] == t[j + right]:
                        right += 1
                    res += left * right
        return res

    def count_substrs_differ_1_char_dp(self, s: str, t: str) -> int:
        # Time complexity: O(S*T)
        # Space complexity: O(S*T)
        dpl = [[0 for _ in range(len(t) + 1)] for _ in range(len(s) + 1)]
        dpr = [[0 for _ in range(len(t) + 1)] for _ in range(len(s) + 1)]
        res = 0
        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                if s[i - 1] == t[j - 1]:
                    dpl[i][j] = 1 + dpl[i - 1][j - 1]
        for i in range(len(s), 0, -1):
            for j in range(len(t), 0, -1):
                if s[i - 1] == t[j - 1]:
                    dpr[i - 1][j - 1] = 1 + dpr[i][j]
        for i in range(len(s)):
            for j in range(len(t)):
                if s[i] != t[j]:
                    res += (dpl[i][j] + 1) * (dpr[i + 1][j + 1] + 1)
        return res
# ----------------------------------------------------------------------------------------------------------------------


examples = [
    {
        's': 'aba',
        't': 'baba',
        'ExpectedResult': 6
    },
    {
        's': 'ab',
        't': 'bb',
        'ExpectedResult': 3
    },
    {
        's': 'a',
        't': 'b',
        'ExpectedResult': 1
    },
    {
        's': 'a',
        't': 'a',
        'ExpectedResult': 0
    },
    {
        's': 'abe',
        't': 'bbc',
        'ExpectedResult': 10
    },
    {
        's': 'computer',
        't': 'computation',
        'ExpectedResult': 10
    },
]

sol = Solution()
for ex in examples:
    print('[%s, %s]' % (ex['s'], ex['t']))
    print(
        'Naive...: %s : %s' % (
            str(ex['ExpectedResult']),
            str(sol.count_substrs_differ_1_char_naive(ex['s'], ex['t']))
        )
    )
    print(
        'Cheaper.: %s : %s' % (
            str(ex['ExpectedResult']),
            str(sol.count_substrs_differ_1_char_cheaper(ex['s'], ex['t']))
        )
    )
    print(
        'DP......: %s : %s' % (
            str(ex['ExpectedResult']),
            str(sol.count_substrs_differ_1_char_dp(ex['s'], ex['t']))
        )
    )
    print()
# ----------------------------------------------------------------------------------------------------------------------
