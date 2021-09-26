from typing import List


# class Solution:
#     def change(self, amount: int, coins: List[int]) -> int:
#         t = []
#         for i in range(0, len(coins) + 1):
#             t.append([0] * (amount + 1))
#
#         for i in range(0, len(coins) + 1):
#             for j in range(0, amount + 1):
#                 if j == 0:
#                     t[i][j] = 1
#                 elif i == 0:
#                     t[i][j] = 0
#                 else:
#                     t[i][j] = t[i - 1][j]
#                     if j - coins[i - 1] >= 0:
#                         t[i][j] += t[i][j - coins[i - 1]]
#
#         return t[-1][-1]

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        t = [0] * (amount + 1)
        t[0] = 1

        for c in coins:
            for i in range(c, len(t)):
                t[i] += t[i - c]

        return t[-1]


sol = Solution()
print(sol.change(5, [1, 2, 5]))

