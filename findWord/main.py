# Implement a word search. Given a 2D array of letters and a word to find, return the 2D array with the found word’s
# letters replaced with an asterisk (*).
#
# Example:
#
# let grid = [['a','a','q','t'],
#             ['x','c','w','e'],
#             ['r','l','e','p']]
#
# $ findWord(grid, 'ace')
# $ [['*','a','q','t'],
#    ['x','*','w','e'],
#    ['r','l','*','p']]
# ----------------------------------------------------------------------------------------------------------------------


from copy import deepcopy
from typing import List, Tuple, Optional
import enum
# ----------------------------------------------------------------------------------------------------------------------


class Direction(enum.Enum):
    WEST = (0, -1)
    NORTHWEST = (-1, -1)
    NORTH = (-1, 0)
    NORTHEAST = (-1, 1)
    EAST = (0, 1)
    SOUTHEAST = (1, 1)
    SOUTH = (1, 0)
    SOUTHWEST = (1, -1)
# ----------------------------------------------------------------------------------------------------------------------


class WordGrid:
    def _check_direction(
            self, grid: List[List[str]], word: str, ni: int, nj: int, direction: Tuple[int]
    ) -> Optional[List[Tuple[int]]]:
        rows, cols = len(grid), len(grid[0])
        result = []
        while (0 <= ni < rows) and (0 <= nj < cols) and (word[len(result)] == grid[ni][nj]):
            result.append((ni, nj))
            ni, nj = ni + direction[0], nj + direction[1]
        return result if len(result) == len(word) else None

    def find_word(self, grid: List[List[str]], word: str) -> List[List[str]]:
        rows, cols = len(grid), len(grid[0])
        for i in range(0, rows):
            for j in range(0, cols):
                for direction_item in Direction:
                    if res := self._check_direction(grid, word, i, j, direction_item.value):
                        for (rx, ry) in res:
                            grid[rx][ry] = '*'
                        break
        return grid
# ----------------------------------------------------------------------------------------------------------------------


examples = {
    'ace': {
        'input': [
            ['a', 'a', 'q', 't'],
            ['x', 'c', 'w', 'e'],
            ['r', 'l', 'e', 'p']
        ],
        'output': [
            ['*', 'a', 'q', 't'],
            ['x', '*', 'w', 'e'],
            ['r', 'l', '*', 'p']
        ]
    },
    'aco': {
        'input': [
            ['d', 'a', 'q', 't'],
            ['x', 'c', 'w', 'e'],
            ['r', 'o', 'e', 'p']
        ],
        'output': [
            ['d', '*', 'q', 't'],
            ['x', '*', 'w', 'e'],
            ['r', '*', 'e', 'p']
        ]
    },
    'oca': {
        'input': [
            ['d', 'a', 'q', 't'],
            ['x', 'c', 'w', 'e'],
            ['r', 'o', 'e', 'p']
        ],
        'output': [
            ['d', '*', 'q', 't'],
            ['x', '*', 'w', 'e'],
            ['r', '*', 'e', 'p']
        ]
    },
    'peor': {
        'input': [
            ['d', 'a', 'q', 't'],
            ['x', 'c', 'w', 'e'],
            ['r', 'o', 'e', 'p']
        ],
        'output': [
            ['d', 'a', 'q', 't'],
            ['x', 'c', 'w', 'e'],
            ['*', '*', '*', '*']
        ]
    },
}


def print_horizontal_matrixes(mat_list: List[List[List[str]]]):
    rows_size = len(mat_list[0])
    for row in range(0, rows_size):
        for mat in mat_list:
            print('[%s]' % (', '.join(mat[row])), end='\t\t')
        print()


sol = WordGrid()
for ex in examples:
    input_grid, output_grid = examples[ex]['input'], examples[ex]['output']
    print('Ref..: %s' % ex)
    print_horizontal_matrixes([input_grid, output_grid, sol.find_word(deepcopy(input_grid), ex)])
    print()
# ----------------------------------------------------------------------------------------------------------------------
