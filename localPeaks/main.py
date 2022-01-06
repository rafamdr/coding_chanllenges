# Given an array of integers, return the index of each local peak in the array. A “peak” element is an element that
# is greater than its neighbors.
#
# Example:
#
# $ localPeaks([1,2,3,1])
# $ [2]
#
# $ localPeaks([1,3,2,3,5,6,4])
# $ [1, 5]
# ----------------------------------------------------------------------------------------------------------------------


from typing import List
# ----------------------------------------------------------------------------------------------------------------------


class Solution:
    def local_peaks_v1(self, array: List[int]) -> List[int]:
        peaks = []
        increasing = False
        for idx in range(1, len(array)):
            if array[idx] > array[idx - 1]:
                increasing = True
            elif increasing:
                peaks.append(idx - 1)
                increasing = False
        return peaks

    def local_peaks_v2(self, array: List[int]) -> List[int]:
        peaks = []
        for idx in range(1, len(array) - 1):
            if array[idx - 1] < array[idx] > array[idx + 1]:
                peaks.append(idx)
        return peaks

    def local_peaks_v3(self, arr: List[int]) -> List[int]:
        return list(filter(lambda i: arr[i - 1] < arr[i] > arr[i + 1], range(1, len(arr) - 1)))

    def local_peaks_v4(self, arr: List[int]) -> List[int]:
        return list(
            filter(
                lambda i: arr[i - 1] < arr[i] > arr[i + 1],
                range(1, len(arr) - 1)
            )
        )
# ----------------------------------------------------------------------------------------------------------------------


examples = {
    'ex1': {
        'array': [1, 2, 3, 1],
        'expected': [2]
    },

    'ex2': {
        'array': [1, 3, 2, 3, 5, 6, 4],
        'expected': [1, 5]
    },

    'ex3': {
        'array': [],
        'expected': []
    },

    'ex4': {
        'array': [1],
        'expected': []
    },

    'ex5': {
        'array': [2, 2],
        'expected': []
    },

    'ex6': {
        'array': [2, 3],
        'expected': []
    },

    'ex7': {
        'array': [45, 6],
        'expected': []
    },

    'ex8': {
        'array': [1, 45, 6],
        'expected': [1]
    },

    'ex9': {
        'array': [1, 4, 1],
        'expected': [1]
    },

    'ex10': {
        'array': [1, 1, 1],
        'expected': [1]
    },

    'ex11': {
        'array': [1, 1, 1, 2, 1, 0, -1, 2, 3, 4, 6, 5, 5, 5, 10, 1],
        'expected': [3, 10, 14]
    },
}

sol = Solution()
for ex in examples:
    examp = examples[ex]
    print('V1..:\t%s ->%s : %s' % (examp['array'], examp['expected'], sol.local_peaks_v1(examp['array'].copy())))
    print('V2..:\t%s ->%s : %s' % (examp['array'], examp['expected'], sol.local_peaks_v2(examp['array'].copy())))
    print('V3..:\t%s ->%s : %s' % (examp['array'], examp['expected'], sol.local_peaks_v3(examp['array'].copy())))
# ----------------------------------------------------------------------------------------------------------------------
