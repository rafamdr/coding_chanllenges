from typing import List
# ----------------------------------------------------------------------------------------------------------------------


class Solution:
    def get_longest_subarray_sum_k_on2(self, array: List, k: int):
        temp_max = 0
        for i in range(len(array)):
            sum = 0
            count = 0
            for j in range(i, len(array)):
                sum += array[j]
                count += 1
                if sum == k:
                    temp_max = max(count, temp_max)

        return temp_max

    def get_longest_subarray_sum_k_on(self, array: List, k: int):
        temp_max = 0
        desc_array_sum = [0] * len(array)
        sum = 0
        for i in range(len(array)):
            sum += array[-i - 1]
            desc_array_sum[-i - 1] = sum
        sum = 0



        return temp_max
# ----------------------------------------------------------------------------------------------------------------------


examples = [
    {
        'array': [10, 5, 2, 7, 1, 9],
        'k': 15
    },
    {
        'array': [-5, 8, -14, 2, 4, 12],
        'k': -5
    },
]

sol = Solution()

for ex in examples:
    print('Quad: %d ' % sol.get_longest_subarray_sum_k_on2(ex['array'], ex['k']), end='')
    print('Lin: %d ' % sol.get_longest_subarray_sum_k_on(ex['array'], ex['k']), end='')
    print()
# ----------------------------------------------------------------------------------------------------------------------
