# Given a 3x3, 2D array of integers, where every digit is between 0 and 9, except 7, find the minimum number of
# digits that must be replaced with 7s so that the sums of the numbers in each row and each column are the same.
#
# Example:
#
# $ missingSevens([[9,4,3],[3,4,9],[4,8,4]])
# $ 0
#
# $ missingSevens([[1,5,2],[5,9,5],[6,5,3]])
# $ 4
#
# $ missingSevens([[3,9,6],[8,5,5],[8,4,0]])
# $ 2
# ----------------------------------------------------------------------------------------------------------------------


from typing import List
# ----------------------------------------------------------------------------------------------------------------------


def missing_sevens_ref(mat: List[List[int]]) -> int:

    return 0
# ----------------------------------------------------------------------------------------------------------------------


examples = {
    'ex1': {
        'mat': [
            [9, 4, 3],
            [3, 4, 9],
            [4, 8, 4]
        ],
        'res': 0
    },
    'ex2': {
        'mat': [
            [1, 5, 2],
            [5, 9, 5],
            [6, 5, 3]
        ],
        'res': 4
    },
    'ex3': {
        'mat': [
            [3, 9, 6],
            [8, 5, 5],
            [8, 4, 0]
        ],
        'res': 2
    },
}

for ex in examples:
    print('Ref..: %s = %d -> %d' % (examples[ex]['mat'], examples[ex]['res'], missing_sevens_ref(examples[ex]['mat'])))
# ----------------------------------------------------------------------------------------------------------------------
