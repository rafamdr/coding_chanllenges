# Given a string containing digits from 2-9, return all possible letter combinations that the number could represent
# based on phone numbers/letters. For example, 2 could be a, b, or c, 3 could be d, e, or f, and so on.
#
# Example:
#
# $ phoneLetter('9')
# $ ['w', 'x', 'y', 'z']
#
# $ phoneLetter('23')
# $ ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
# ----------------------------------------------------------------------------------------------------------------------


from typing import List
import re
from collections import Counter, defaultdict


# ----------------------------------------------------------------------------------------------------------------------


class PhoneLetter:
    def __init__(self):
        self._map = {
                         '2': 'abc', '3': 'def',
            '4': 'ghi',  '5': 'jkl', '6': 'mno',
            '7': 'pqrs', '8': 'tuv', '9': 'wxyz',
        }

    def get_combinations(self, str_number: str, sort_result=False) -> List[str]:
        result = [] if len(str_number) == 0 else list(self._map[str_number[0]])
        for digit in str_number[1:]:
            result_bkp = result.copy()
            result = [
                combination + letter
                for combination in result_bkp
                for letter in self._map[digit]
            ]
        return sorted(result) if sort_result else result


# ----------------------------------------------------------------------------------------------------------------------


examples = {
    '': [],
    '9': ['w', 'x', 'y', 'z'],
    '23': ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf'],
    '235': ['adj', 'aej', 'afj', 'bdj', 'bej', 'bfj', 'cdj', 'cej', 'cfj',
            'adk', 'aek', 'afk', 'bdk', 'bek', 'bfk', 'cdk', 'cek', 'cfk',
            'adl', 'ael', 'afl', 'bdl', 'bel', 'bfl', 'cdl', 'cel', 'cfl'
            ],
}

sol = PhoneLetter()
for ex in examples:
    examp = examples[ex]
    res = sol.get_combinations(ex, True)
    print('V1..:\t%s ->%s : %s' % (ex, examp, sorted(examp) == res))
# ----------------------------------------------------------------------------------------------------------------------
