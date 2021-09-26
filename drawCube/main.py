# Write a function that draws an ASCII art cube of given height x.
#
# Example:
#
# $ drawCube(1)
#   +--+
#  /  /|
# +--+ +
# |  |/
# +--+
#
# $ drawCube(2)
#   +----+
#  /    /|
# +----+ |
# |    | +
# |    |/
# +----+
#
# $ drawCube(3)
#   +------+
#  /      /|
# +------+ |
# |      | |
# |      | +
# |      |/
# +------+
#
# $ drawCube(4)
#    +--------+
#   /        /|
#  /        / |
# +--------+  |
# |        |  |
# |        |  +
# |        | /
# |        |/
# +--------+
# ----------------------------------------------------------------------------------------------------------------------


class Solution:
    def draw_cube_ref(self, size: int):
        init_spaces = max(2, size - 1)
        # draw upper border
        print((' ' * init_spaces) + '+' + ('-' * size * 2) + '+')
        # draw upper diagonals
        for i in range(0, init_spaces - 1):
            print((' ' * (init_spaces - 1 - i)) + '/' + (' ' * size * 2) + '/' + (' ' * i) + '|')
        init_spaces = i + 1
        # draw corner and first columns
        print('+' + ('-' * size * 2) + '+' + (' ' * init_spaces) + ('|' if size > 1 else '+'))
        if size == 2:
            print('|' + (' ' * size * 2) + '|' + (' ' * init_spaces) + '+')
        elif size > 2:
            print('|' + (' ' * size * 2) + '|' + (' ' * init_spaces) + '|')
            print('|' + (' ' * size * 2) + '|' + (' ' * init_spaces) + '+')
        # draw columns and lower diagonal
        for i in range(0, init_spaces):
            print('|' + (' ' * size * 2) + '|' + (' ' * (init_spaces - i - 1)) + '/')
        # draw lower border
        print('+' + ('-' * size * 2) + '+')
# ----------------------------------------------------------------------------------------------------------------------


examples = {
    1: '1',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    10: '10',
}

sol = Solution()
for ex in examples:
    print('Ref..: %s = %s:' % (ex, examples[ex]))
    sol.draw_cube_ref(ex)
    print()
# ----------------------------------------------------------------------------------------------------------------------
