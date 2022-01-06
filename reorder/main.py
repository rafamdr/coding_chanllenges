# Given an array of objects A, and an array of indexes B, reorder the objects in array A with the given indexes in
# array B.
# Example:
#
# let a = [C, D, E, F, G, H];
# let b = [3, 0, 4, 1, 2, 5];
#
# $ reorder(a, b) // a is now [D, F, G, C, E, H]
# ----------------------------------------------------------------------------------------------------------------------


from typing import List
# ----------------------------------------------------------------------------------------------------------------------


class Solution:
    def reorder_v1(self, items: List[str], indexes: List[int]) -> List[str]:
        return [i[1] for i in sorted(enumerate(items), key=lambda x: indexes[x[0]])]

    def reorder_v2(self, items: List[str], indexes: List[int]) -> List[str]:
        res = [''] * len(items)
        for i in range(0, len(indexes)):
            res[indexes[i]] = items[i]
        return res

    def reorder_v3(self, items: List, indexes: List[int]) -> List:  # doesn't work for all cases
        for i in range(0, len(indexes)):
            items[indexes[i]], items[i] = items[i], items[indexes[i]]
            indexes[indexes[i]], indexes[i] = indexes[i], indexes[indexes[i]]
        return items

    def reorder_v4(self, items: List, indexes: List[int]) -> List:
        for i in range(0, len(items)):
            while indexes[i] != i:
                temp_idx = indexes[indexes[i]]
                temp_item = items[indexes[i]]

                items[indexes[i]] = items[i]
                indexes[indexes[i]] = indexes[i]

                indexes[i] = temp_idx
                items[i] = temp_item
        return items
# ----------------------------------------------------------------------------------------------------------------------


examples = {
    'ex1': {
        'items': ["C", "D", "E", "F", "G", "H"],
        'indexes': [3, 0, 4, 1, 2, 5],
        'expected': ['D', 'F', 'G', 'C', 'E', 'H']
    },

    'ex2': {
        'items': ["C", "D", "E", "F", "G"],
        'indexes': [3, 0, 4, 1, 2],
        'expected': ['D', 'F', 'G', 'C', 'E']
    },

    'ex3': {
        'items': [24, 56, 74, -23, 87, 91],
        'indexes': [1, 2, 3, 0, 4, 5],
        'expected': [-23, 24, 56, 74, 87, 91]
    },

    'ex4': {
        'items': [10, 11, 12],
        'indexes': [1, 0, 2],
        'expected': [11, 10, 12]
    },
}

sol = Solution()
for ex in examples:
    examp = examples[ex]
    print('v1: ' + str(sol.reorder_v1(examp['items'].copy(), examp['indexes'].copy())))
    print('v2: ' + str(sol.reorder_v2(examp['items'].copy(), examp['indexes'].copy())))
    print('v3: ' + str(sol.reorder_v3(examp['items'].copy(), examp['indexes'].copy())))
    print('v4: ' + str(sol.reorder_v4(examp['items'].copy(), examp['indexes'].copy())))
# ----------------------------------------------------------------------------------------------------------------------
