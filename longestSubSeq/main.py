# Given an array of integers, find the length of the longest sub-sequence such that elements in the sub-sequence are
# consecutive integers, the consecutive numbers can be in any order.
#
# Example:
#
# $ longestSubSeq([1, 9, 87, 3, 10, 4, 20, 2, 45])
# $ 4 // 1, 3, 4, 2
#
# $ longestSubSeq([36, 41, 56, 35, 91, 33, 34, 92, 43, 37, 42])
# $ 5 // 36, 35, 33, 34, 37
# ----------------------------------------------------------------------------------------------------------------------


from typing import List


# ----------------------------------------------------------------------------------------------------------------------


class Solution:
    def longest_sub_seq(self, array: List[int]) -> int:
        sorted_array = sorted(array)
        longest = 1 if len(array) == 1 else 0
        count = 1
        for i in range(1, len(sorted_array)):
            if longest >= (len(sorted_array) // 2) + (len(sorted_array) & 1):
                break
            elif sorted_array[i] - sorted_array[i - 1] == 1:
                count += 1
            else:
                longest = max(count, longest)
                count = 1
        return longest

    def longest_sub_seq_v1(self, array: List[int]) -> int:
        result = set(array)
        longest = 0
        for num in array:
            count = 1
            temp_num = num
            while (temp_num := temp_num - 1) in result:
                result.remove(temp_num)
                count += 1
            temp_num = num
            while (temp_num := temp_num + 1) in result:
                result.remove(temp_num)
                count += 1
            longest = count if count > longest else longest
            if num in result:
                result.remove(num)
        return longest

    def longest_sub_seq_v2(self, array: List[int]) -> int:
        result = set(array)
        longest = 0
        for num in array:
            if num - 1 not in result:
                count = 1
                while (num := num + 1) in result:
                    count += 1
                longest = max(count, longest)
        return longest

    def longest_sub_seq_v3(self, array: List[int]) -> int:
        temp_set = set(array)
        longest = 0
        while len(temp_set) > 0 and longest < len(temp_set):
            num = temp_set.pop()
            if num - 1 not in temp_set:
                count = 1
                while (num := num + 1) in temp_set:
                    count += 1
                    temp_set.remove(num)
                longest = max(count, longest)
        return longest
# ----------------------------------------------------------------------------------------------------------------------


examples = {
    0: [],
    1: [1],
    # 1: [2, 2],
    4: [9, 87, 3, 10, 4, 20, 2, 45, 1],
    5: [36, 41, 56, 35, 91, 33, 34, 92, 43, 37, 42],
    6: [100, 9, 87, 3, 10, 4, 20, 2, 45, 1, 5, 6],
}

sol = Solution()
for ex in examples:
    print('Ref..: %s <-> %d == %d' % (examples[ex], ex, sol.longest_sub_seq(examples[ex])))
    print('v1...: %s <-> %d == %d' % (examples[ex], ex, sol.longest_sub_seq_v1(examples[ex])))
    print('v2...: %s <-> %d == %d' % (examples[ex], ex, sol.longest_sub_seq_v2(examples[ex])))
    print('v3...: %s <-> %d == %d' % (examples[ex], ex, sol.longest_sub_seq_v3(examples[ex])))
    print()
# ----------------------------------------------------------------------------------------------------------------------
