from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        t = [amount] * (amount + 1)
        t[0] = 0

        for c in coins:
            for i in range(c, len(t)):
                t[i] = min(
                    t[i],
                    t[i - c] + 1
                )

        return t[-1]



sol = Solution()
#print(sol.change(5, [1, 2, 5]))
print(sol.change(11, [1, 2, 5]))

