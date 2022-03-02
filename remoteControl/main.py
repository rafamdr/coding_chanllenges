# Given a QWERTY keyboard grid and a remote control with arrows and a “select” button, write a function that returns
# the buttons you have to press to type a certain word. The cursor will always start in the upper left at the letter Q.
#
# Example:
#
# $ remoteControl('car')
# $ 'down, down, right, right, select, left, left, up, select, up, right, right, right, select'
# ----------------------------------------------------------------------------------------------------------------------
import enum


# ----------------------------------------------------------------------------------------------------------------------


class Direction(enum.Enum):
    left = (0, -1)
    up = (-1, 0)
    right = (0, 1)
    down = (1, 0)
# ----------------------------------------------------------------------------------------------------------------------


class RemoteControl:
    def __init__(self):
        self.qwerty_kb = [
            ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
            ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', '.'],
            ['z', 'x', 'c', 'v', 'b', 'n', 'm', '.', '.', '.']
        ]
        self.rows, self.cols = len(self.qwerty_kb), len(self.qwerty_kb[0])
        self.qwerty_kb_reverse_idx = {
            self.qwerty_kb[pos[0]][pos[1]]: pos
            for pos in [(i, j) for j in range(0, self.cols) for i in range(0, self.rows)]
        }

    def _get_distance(self, p1: tuple[int, int], p2: tuple[int, int]):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    def get_sequence(self, word: str) -> str:
        stack = [[0, 0, 0, []]]
        while len(stack) > 0:
            i, j, idx, path = stack.pop()
            if word[idx] == self.qwerty_kb[i][j]:
                path.append('select')
                idx += 1
            if idx == len(word) or word[idx] not in self.qwerty_kb_reverse_idx:
                break
            dst_pos = self.qwerty_kb_reverse_idx[word[idx]]
            for direction_item in Direction:
                ni, nj = i + direction_item.value[0], j + direction_item.value[1]
                if (
                    (0 <= ni < self.rows) and (0 <= nj < self.cols) and self.qwerty_kb[ni][nj] != '.' and
                    self._get_distance((ni, nj), dst_pos) < self._get_distance((i, j), dst_pos)
                ):
                    stack.append([ni, nj, idx, path + [str(direction_item.name)]])
        return '' if path is None else path
# ----------------------------------------------------------------------------------------------------------------------


examples = {
    'car': 'down, down, right, right, select, left, left, up, select, up, right, right, right, select',
    '3453': ''
}

sol = RemoteControl()
for ex in examples:
    print('Ref..: %s ->\t%s \n%s ' % (ex, examples[ex], str(sol.get_sequence(ex))))
    print()
# ----------------------------------------------------------------------------------------------------------------------
