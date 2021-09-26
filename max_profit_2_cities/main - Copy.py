from typing import List
# ----------------------------------------------------------------------------------------------------------------------


class Example:
    def __init__(self, pcity_a: List[int], pcity_b: List[int], fee: int):
        self.pcity_a = pcity_a
        self.pcity_b = pcity_b
        self.fee = fee
# ----------------------------------------------------------------------------------------------------------------------


class Solution:
    @staticmethod
    def max_profit_2cities_2d(pcity_a: List[int], pcity_b: List[int], fee: int) -> int:
        t = []
        for i in range(0, len(pcity_a) + 1):
            t.append([0] * (len(pcity_b) + 1))

        for i in range(0, len(pcity_a) + 1):
            for j in range(0, len(pcity_b) + 1):
                if i == 0 and j > 0:
                    t[i][j] = t[i][j - 1] + pcity_b[j - 1]
                elif j == 0 and i > 0:
                    t[i][j] = t[i - 1][j] + pcity_a[i - 1]
                elif i > 0 and i == j:
                    t[i][j] = max(t[i][j - 1], t[i - 1][j])
                elif i > j:
                    # print('lower left corner triangle coord: %d, %d' % (i, j))
                    last_pos = i - 1
                    if last_pos == j:
                        last_pos = i - 2
                    t[i][j] = max(
                        t[i][j - 1],
                        t[last_pos][j] - fee + pcity_a[i - 1]
                    )
                elif i < j:
                    # print('upper right corner triangle coord: %d, %d' % (i, j))
                    last_pos = j - 1
                    if last_pos == i:
                        last_pos = j - 2
                    t[i][j] = max(
                        t[i - 1][j],
                        t[i][last_pos] - fee + pcity_b[j - 1]
                    )
        return t[-1][-1]

    @staticmethod
    def max_profit_2cities_2arrays(pcity_a: List[int], pcity_b: List[int], fee: int) -> int:
        return 0
# ----------------------------------------------------------------------------------------------------------------------


sol = Solution()
examples = [
    Example([-10, 50, 20], [10, 20, 30], 10),
    Example([-10, 50, 20], [10, 20, 30], 20),
    Example([0, 1001, 0], [0, 20, 30], 1000),
]

for ex in examples:
    res2d = sol.max_profit_2cities_2d(ex.pcity_a, ex.pcity_b, ex.fee)
    res2Array = sol.max_profit_2cities_2arrays(ex.pcity_a, ex.pcity_b, ex.fee)
    print('Results -> 2D = %d \t 2Arrays = %d' % (res2d, res2Array))

# ----------------------------------------------------------------------------------------------------------------------
