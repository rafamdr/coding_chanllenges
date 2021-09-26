# Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's
# in their binary representation and return them as an array.
#
# Example 1:
#
# Input: 2
# Output: [0,1,1]
# Example 2:
#
# Input: 5
# Output: [0,1,1,2,1,2]
# Follow up:
#
# It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(
# n) /possibly in a single pass? Space complexity should be O(n). Can you do it like a boss? Do it without using any
# builtin function like __builtin_popcount in c++ or in any other language.
# ----------------------------------------------------------------------------------------------------------------------


from typing import List
# ----------------------------------------------------------------------------------------------------------------------


class Solution:
    def count_bits_ref(self, num: int):
        array = []
        for i in range(0, num + 1):
            bit_cnt = 0
            num_temp = i
            while num_temp > 0:
                bit_cnt += (num_temp & 1)
                num_temp = num_temp >> 1
            array.append(bit_cnt)
        return array

    def count_bits_fast1(self, num: int):
        array = [0]
        for i in range(1, num + 1):
            if i & (i - 1) == 0:
                array.append(1)
            elif i & 1 == 0:
                array.append(array[i // 2])
            else:
                array.append(array[i // 2] + 1)
        return array

    def count_bits_fast2(self, num: int):
        array = [0]
        for i in range(1, num + 1):
            if i & 1 == 0:
                array.append(array[i // 2])
            else:
                array.append(array[i // 2] + 1)
        return array

    def count_bits_fast3(self, num: int):
        array = [0]
        for i in range(1, num + 1):
            array.append(array[i // 2] + (i & 1))
        return array
# ----------------------------------------------------------------------------------------------------------------------


examples = [
    8, 10, 32, 366, 77
]

sol = Solution()

for ex in examples:
    print('Ref..: %s' % str(sol.count_bits_ref(ex)))
    print('Fast1: %s' % str(sol.count_bits_fast1(ex)))
    print('Fast2: %s' % str(sol.count_bits_fast2(ex)))
    print('Fast3: %s' % str(sol.count_bits_fast3(ex)))
    print()
# ----------------------------------------------------------------------------------------------------------------------
