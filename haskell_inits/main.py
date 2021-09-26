# Given a list, return a list of all its prefixes in ascending order of their length. You’re essentially implementing
# the inits function in Haskell!
#
# Example:
#
# $ inits([4, 3, 2, 1])
# $ [[], [4], [4,3], [4,3,2], [4,3,2,1]]
#
# $ inits([144])
# $ [[], [144]]
# ----------------------------------------------------------------------------------------------------------------------


from functools import reduce
from typing import List
# ----------------------------------------------------------------------------------------------------------------------


class Solution:
    def inits(self, arr: List) -> List[List]:
        return reduce(lambda res, item: res + [res[-1] + [item]], arr, [[]])
# ----------------------------------------------------------------------------------------------------------------------


examples = {
    tuple([4, 3, 2, 1]): [[], [4], [4, 3], [4, 3, 2], [4, 3, 2, 1]],
    tuple([144]): [[], [144]],
}

sol = Solution()
for ex in examples:
    print('Ref.: \n%s->\n%s\n%s\n' % (ex, examples[ex], sol.inits(list(ex))))
# ----------------------------------------------------------------------------------------------------------------------
