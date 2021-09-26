from typing import List
# ----------------------------------------------------------------------------------------------------------------------


class Solution:
    def move_zeros_v1(self, array: List):
        # Using a temporary array to store non-zeros elements
        # After that, it extends this temporary array with found zeros
        # Time: O(n); Space: O(n)
        count = 0
        temp_array = []
        while count < len(array):
            if array[count] != 0:
                temp_array.append(array[count])
            count += 1
        temp_array.extend([0] * (len(array) - len(temp_array)))
        return temp_array

    def move_zeros_v2(self, array: List):
        # swapping zeros with non-zeros elements in the end of array
        # Time: O(n); Space: O(1)
        start = 0
        end = len(array)
        while start < end:
            if array[start] == 0:
                array[start], array[end - 1] = array[end - 1], array[start]
                end -= 1
            else:
                start += 1
        return array

    def move_zeros_v3(self, array: List):
        # swapping non-zeros elements in the beginning of array
        # Time: O(n); Space: O(1)
        pos_to_swap = 0
        for i in range(len(array)):
            if array[i] != 0:
                array[pos_to_swap], array[i] = array[i], array[pos_to_swap]
                pos_to_swap += 1
        return array
# ----------------------------------------------------------------------------------------------------------------------


examples = [
    [0, 0, 0, 0, 4, 0],
    [6, 5, 4, 0],
    [0, 0, 0],
    [0, 0],
    [0],
    [1, 0],
    [0, 1],
    [],
    [1, 2, 0, 1, 0, 0, 3, 6],
    [0, 1, 2, 0, 1, 0, 0, 3, 6],
    [0,0,0,0,0,0,1111,1,1,1,1],
    [0,1,2,3,4],
    [1,2,3,4],
    [0,0,0,0,0,0,0,0,0,0,0,0,1,2,3,4],
    [0,0,0,0,0,0,0,0,0,0,0,0,1,2,3,4,0],
]

sol = Solution()
for ex in examples:
    print('V1: %s' % sol.move_zeros_v1(ex))
    print('V2: %s' % sol.move_zeros_v2(ex))
    print('V3: %s' % sol.move_zeros_v3(ex))
    print('-------------------------------------------------')
# ----------------------------------------------------------------------------------------------------------------------
