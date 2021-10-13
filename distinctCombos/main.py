# Given an integer array, find all distinct combinations of a given length x (with repetition allowed).
#
# Example:
#
# $ distinctCombos([1,1,2], 2)
# $ [1, 1], [1, 2], [2, 2]
#
# $ distinctCombos([1,2,3,4], 2)
# $ [1, 1], [1, 2], [1, 3], [1, 4], [2, 2], [2, 3], [2, 4], [3, 3], [3, 4], [4, 4]
# ----------------------------------------------------------------------------------------------------------------------


from typing import List, Tuple
import copy as cp
# ----------------------------------------------------------------------------------------------------------------------


class Solution:
    def distinct_combos (
            self,
            array: List[int],
            length: int, allow_rep: bool = False
    ) -> List[List[int]]:

        result = [tuple([_]) for _ in array]
        if length <= 0:
            return []
        elif length == 1:
            result = set(result)
        else:
            for i in range(1, length):
                temp = []
                for _ in range(0, len(array)):
                    temp.extend(cp.deepcopy(result))
                result = set()
                for idx in range(0, len(temp)):
                    array_item = array[(idx // len(array)) % len(array)]
                    if allow_rep or (array_item, *temp[idx]) not in result:
                        result.add((*temp[idx], array_item))
        return sorted([
            (
                sorted(list(item)) if allow_rep is False else list(item)
            ) for item in result
        ])
# ----------------------------------------------------------------------------------------------------------------------


examples = {
    'ex3.0': {
        'array': [1, 1, 2],
        'length': 0,
        'expected': []
    },

    'ex0.3': {
        'array': [],
        'length': 3,
        'expected': []
    },

    'ex3.2': {
        'array': [1, 1, 2],
        'length': 2,
        'expected': [[1, 1], [1, 2], [2, 2]]
    },

    'ex3.3': {
        'array': [1, 1, 2],
        'length': 3,
        'expected': [[1, 1, 1], [1, 1, 2], [1, 2, 2], [2, 2, 2]]
    },

    'ex4.2': {
        'array': [1, 2, 3, 4],
        'length': 2,
        'expected': [[1, 1], [1, 2], [1, 3], [1, 4], [2, 2], [2, 3], [2, 4], [3, 3], [3, 4], [4, 4]]
    }
}

sol = Solution()
for ex in examples:
    item = examples[ex]
    print(
        'Ref..: %s : %d -> \n\tExp: %s \n\tRes: %s ' % (
            item['array'],
            item['length'],
            item['expected'],
            str(sol.distinct_combos(item['array'], item['length']))
        )
    )
    print()
# ----------------------------------------------------------------------------------------------------------------------

# [1, 1], [1, 2], [2, 2]
# [1, 1, 1], [1, 2, 1], [2, 2, 1], [1, 1, 2], [1, 2, 2], [2, 2, 2]


