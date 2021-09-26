# Given a direction and a number of columns, write a function that outputs an arrow of asterisks (see the pattern in
# the examples below)!
#
# Example:
#
# $ printArrow('right', 3)
# Output:
# *
#  *
#   *
#  *
# *
#
# $ printArrow('left', 5)
# Output:
#     *
#    *
#   *
#  *
# *
#  *
#   *
#    *
#     *
# ----------------------------------------------------------------------------------------------------------------------


from collections import Counter
# ----------------------------------------------------------------------------------------------------------------------


class Solution:
    def print_arrow_ref(self, dir: str, size: int):
        if dir == 'right':
            for i in range(0, size):
                print(i * ' ' + '*')
            for i in range(size - 2, -1, -1):
                print(i * ' ' + '*')
        else:
            for i in range(size - 1, -1, -1):
                print(i * ' ' + '*')
            for i in range(1, size):
                print(i * ' ' + '*')

    def print_arrow_op1(self, dir: str, size: int):
        incr = 0 if dir == 'right' else size - 1
        for i in range(0, size):
            print(abs(incr - i) * ' ' + '*')
        incr = size - 1 if dir == 'right' else 0
        for i in range(1, size):
            print(abs(incr - i) * ' ' + '*')

    def print_arrow_op2(self, dir: str, size: int):
        def print_out(start, a, s):
            print(*(abs(a - i) * ' ' + '*' for i in range(start, s)), sep='\n')
        print_out(0, (0 if dir == 'right' else size - 1), size)
        print_out(1, (size - 1 if dir == 'right' else 0), size)

    def print_arrow_op3(self, dir: str, size: int):
        size -= 1
        adj = size if dir == 'right' else 0
        for i in range(0, (size * 2) + 1):
            print(abs(adj - abs(i % (size*2) - size)) * ' ' + '*')
# ----------------------------------------------------------------------------------------------------------------------


examples = {
    'ex1': ['right', 3],
    'ex2': ['left', 5],
    'ex3': ['right', 4],
    'ex4': ['left', 8],
}

sol = Solution()
for ex in examples:
    print('Ref..: %s = %s:' % (ex, examples[ex]))
    sol.print_arrow_op3(examples[ex][0], examples[ex][1])
    print()
# ----------------------------------------------------------------------------------------------------------------------
