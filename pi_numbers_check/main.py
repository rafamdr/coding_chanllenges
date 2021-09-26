from collections import deque
from typing import List
# ----------------------------------------------------------------------------------------------------------------------


class Solution:
    def __init__(self):
        pass

    def get_min_spaces(self, digits: str, numbers: List) -> int:
        numbers_set = set(numbers)
        graph = {}
        d_len = len(digits)
        left = right = 0
        results = {}

        while left < d_len:
            possible_num = digits[left:right]
            if len(possible_num) !=0 and possible_num in numbers_set:
                if left not in graph:
                    graph[left] = {possible_num: right}
                else:
                    graph[left][possible_num] = right

            if right < d_len:
                right += 1
            else:
                left += 1
                right = left

        queue = deque()
        for gidx in graph:
            temp_visited = []
            queue.append(gidx)
            while len(queue) > 0:
                idx = queue.pop()
                temp_visited.append(idx)
                for adj_idx in graph[idx]:
                    if graph[idx][adj_idx] in graph:
                        queue.append(graph[idx][adj_idx])

            results[gidx] = temp_visited

        num_spaces = 0
        for path in results:
            if len(results[path]) > num_spaces:
                num_spaces = len(results[path])

        if num_spaces:
            return num_spaces - 1

        return -1

    def _check(self, pos):
        return 0

    def get_min_spaces2(self, digits: str, numbers: List) -> int:
        

# ----------------------------------------------------------------------------------------------------------------------


sol = Solution()

pi_digits = '3141592653589793238462643383279'
numbers = ['314', '49', '9001', '15926535897', '14', '9323', '8462643383279', '4', '793']
# Expected result = 314 15926535897 9323 8462643383279      ->   3 spaces
res = sol.get_min_spaces(pi_digits, numbers)
print(res)

pi_digits = '3141592653589793238462643383279'
numbers = ['314', '897', '159', '14', '9323', '8462643383279', '4', '926']
# Expected result = 897 9323 8462643383279      ->   2 spaces
res = sol.get_min_spaces(pi_digits, numbers)
print(res)

pi_digits = '3141592653589793238462643383279'
numbers = []
# Expected result = -1
res = sol.get_min_spaces(pi_digits, numbers)
print(res)

pi_digits = '3141592653589793238462643383279'
numbers = ['555']
# Expected result = -1
res = sol.get_min_spaces(pi_digits, numbers)
print(res)

pi_digits = '3141592653589793238462643383279'
numbers = ['3141592653589793238462643383279']
# Expected result = 0
res = sol.get_min_spaces(pi_digits, numbers)
print(res)

pi_digits = '3141592653589793238462643383279'
numbers = ['']
# Expected result = -1
res = sol.get_min_spaces(pi_digits, numbers)
print(res)

pi_digits = '12345'
numbers = ['1', '2', '3', '4', '5']
# Expected result = 4
res = sol.get_min_spaces(pi_digits, numbers)
print(res)

pi_digits = '112345'
numbers = ['1', '2', '3', '4', '5']
# Expected result = 5
res = sol.get_min_spaces(pi_digits, numbers)
print(res)
# ----------------------------------------------------------------------------------------------------------------------
