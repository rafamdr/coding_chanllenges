# You went on a vacation with friends. Each of you paid for certain meals on the trip for the group. Write a function
# that determines who owes money to whom so that everyone pays equally.
#
# Example:
#
# let receipts = [
#   { name: 'Ximena', paid: 45 },
#   { name: 'Clara', paid: 130 },
#   { name: 'Ximena', paid: 100 },
#   { name: 'Cassidy', paid: 140 },
#   { name: 'Cassidy', paid: 76 },
#   { name: 'Clara', paid: 29 },
#   { name: 'Ximena', paid: 20 },
# ]
#
# $ whoOwes(receipts)
# $ 'Clara owes Cassidy $19, Ximena owes Cassidy $17'
# ----------------------------------------------------------------------------------------------------------------------

import heapq
from typing import List


# ----------------------------------------------------------------------------------------------------------------------
class PaymentReceipt:
    def __init__(self, name: str, paid: float):
        self.name = name
        self.paid = paid
# ----------------------------------------------------------------------------------------------------------------------


class Solution:
    def who_owes(self, receipts: List[PaymentReceipt]) -> str:
        dct = {}
        total = 0
        for rec in receipts:
            if rec.name not in dct:
                dct[rec.name] = 0
            dct[rec.name] += rec.paid
            total += rec.paid
        part = (total / len(dct.keys()))
        for name in dct:
            dct[name] -= part

        a = 0

        return ''

# ----------------------------------------------------------------------------------------------------------------------


examples = {
    'ex1': {
        'input': [
          {'name': 'Ximena', 'paid': 45},
          {'name': 'Clara', 'paid': 130},
          {'name': 'Ximena', 'paid': 100},
          {'name': 'Cassidy', 'paid': 140},
          {'name': 'Cassidy', 'paid': 76},
          {'name': 'Clara', 'paid': 29},
          {'name': 'Ximena', 'paid': 20},
        ],
        'expected': 'Clara owes Cassidy $19, Ximena owes Cassidy $17'
    }
}

sol = Solution()
for ex in examples:
    input_ex, expected = examples[ex]['input'], examples[ex]['expected']
    print(
        'Ref..: %s:\n\tExp: %s\n\tRes: %s' % (
            input_ex,
            expected,
            sol.who_owes(
                list(map(lambda x: PaymentReceipt(x['name'], x['paid']), input_ex))
            )
        )
    )
    print()
# ----------------------------------------------------------------------------------------------------------------------
