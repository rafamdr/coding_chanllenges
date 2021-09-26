# Given an unsorted array of integers and a number n, find the number of continuous subarrays having sum exactly
# equal n. Return -1 if none exist.
#
# Example:
#
# $ subarraySum([10 , 2, -2, -20, 10], -10)
# $ 3 // arr[0...3], arr[1...4], arr[3...4]
# ----------------------------------------------------------------------------------------------------------------------
from typing import List


def subarray_sum_ref(array: List[int], desired_sum: int) -> int:
    results = []
    for i in range(0, len(array)):
        sum = array[i]
        if sum == desired_sum:
            results.append([i, i])
        for j in range(i + 1, len(array)):
            sum += array[j]
            if sum == desired_sum:
                results.append([i, j])
    return len(results)


def subarray_sum(array: List[int], desired_sum: int) -> int:
    dict = {0: {0}}
    sum = 0
    results = []
    for i in range(0, len(array)):
        temp = (sum + array[i] - desired_sum)
        if temp in dict:
            results.extend([[idx, i] for idx in dict[temp]])
        if sum not in dict:
            dict[sum] = set()
        dict[sum].add(i)
        sum += array[i]
    return len(results)


def num_subarrays_sum(array: List[int], desired_sum: int) -> int:
    dict = {0: 0}
    sum = 0
    result = 0
    for i in range(0, len(array)):
        sum += array[i]
        result += int(sum == desired_sum)
        if sum - desired_sum in dict:
            result += dict[sum - desired_sum]
        if sum not in dict:
            dict[sum] = 0
        dict[sum] += 1
    return result
# ----------------------------------------------------------------------------------------------------------------------


examples = {
    'ex0': {
        'array': [],
        'desired_sum': -10,
        'expected_res': []
    },
    'ex1': {
        'array': [10],
        'desired_sum': -10,
        'expected_res': []
    },
    'ex2': {
        'array': [-10],
        'desired_sum': -10,
        'expected_res': [[0, 0]]
    },
    'ex3': {
        'array': [10, 2, -2, -20, 10],
        'desired_sum': -10,
        'expected_res': [[0, 3], [1, 4], [3, 4]]
    },
    'ex4': {
        'array': [34, 5, -5, -5, 3, 0],
        'desired_sum': -10,
        'expected_res': [[2, 3]]
    },
    'ex5': {
        'array': [-10, 0],
        'desired_sum': -10,
        'expected_res': [[0, 0], [0, 1]]
    },
}

for ex in examples:
    it = examples[ex]
    print('%s: %s, %d -> %s' % (ex, it['array'], it['desired_sum'], str(it['expected_res'])))
    print('Ref.: %s' % str(subarray_sum_ref(it['array'], it['desired_sum'])))
    print('Opt1: %s' % str(subarray_sum(it['array'], it['desired_sum'])))
    print('Num.: %s' % str(num_subarrays_sum(it['array'], it['desired_sum'])))
    print()
# ----------------------------------------------------------------------------------------------------------------------
