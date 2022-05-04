# Given a string that represents items as asterisks (*) and compartment walls as pipes (|), a start index, and an end
# index, return the number of items in a closed compartment.
#
# Example:
#
# let str = '|**|*|*'
#
# > containedItems(str, 0, 5)
# > 2
#
# > containedItems(str, 0, 6)
# > 3
#
# > containedItems(str, 1, 7)
# > 1
# ----------------------------------------------------------------------------------------------------------------------

from typing import List, Dict
# ----------------------------------------------------------------------------------------------------------------------


class Solution:
    def contained_items(self, text: str, indices: List[tuple[int, int]]) -> Dict[tuple[int, int], int]:
        COUNT, LOCAL_COUNT, STATE = 0, 1, 2
        indices_dict, result_dict = {}, {}
        for (start, end) in indices:
            result_dict[(start, end)] = 0
            if start not in indices_dict:
                indices_dict[start] = {}
            indices_dict[start][end] = [0, 0, 0]

        for i, ch in enumerate(text):
            for start in indices_dict:
                if i >= start:
                    for end in indices_dict[start]:
                        if i < end:
                            if ch == '|':
                                indices_dict[start][end][COUNT] += indices_dict[start][end][LOCAL_COUNT]
                                indices_dict[start][end][LOCAL_COUNT] = 0
                                indices_dict[start][end][STATE] = 1
                            else:
                                if indices_dict[start][end][STATE] == 1:
                                    indices_dict[start][end][LOCAL_COUNT] += 1

        for start in indices_dict:
            for end in indices_dict[start]:
                result_dict[(start, end)] = indices_dict[start][end][COUNT]

        return result_dict

    def contained_items_v2(self, text: str, indices: List[tuple[int, int]]) -> Dict[tuple[int, int], int]:
        COUNT, LOCAL_COUNT, STATE = 0, 1, 2
        indices_dict, result_dict = {}, {}
        for (start, end) in indices:
            if start not in indices_dict:
                indices_dict[start] = {}
            indices_dict[start][end] = [0, 0, 0]

        for i, ch in enumerate(text):
            for start in indices_dict:
                if i >= start:
                    for end in indices_dict[start]:
                        if i < end:
                            if ch == '|':
                                indices_dict[start][end][COUNT] += indices_dict[start][end][LOCAL_COUNT]
                                indices_dict[start][end][LOCAL_COUNT] = 0
                                indices_dict[start][end][STATE] = 1
                            else:
                                indices_dict[start][end][LOCAL_COUNT] += indices_dict[start][end][STATE]

        for start in indices_dict:
            for end in indices_dict[start]:
                result_dict[(start, end)] = indices_dict[start][end][COUNT]

        return result_dict

    def contained_items_v3(self, text: str, indices: List[tuple[int, int]]) -> Dict[tuple[int, int], int]:
        COUNT, LOCAL_COUNT, STATE = 0, 1, 2
        indices_dict = {(start, end): [0, 0, 0] for (start, end) in indices}
        for i, ch in enumerate(text):
            for (start, end) in indices_dict:
                if start <= i < end:
                    if ch == '|':
                        indices_dict[(start, end)][COUNT] += indices_dict[(start, end)][LOCAL_COUNT]
                        indices_dict[(start, end)][LOCAL_COUNT] = 0
                        indices_dict[(start, end)][STATE] = 1
                    else:
                        indices_dict[(start, end)][LOCAL_COUNT] += indices_dict[(start, end)][STATE]

        for (start, end) in indices_dict:
            indices_dict[(start, end)] = indices_dict[(start, end)][COUNT]

        return indices_dict

    def contained_items_v4(self, text: str, indices: List[tuple[int, int]]) -> Dict[tuple[int, int], int]:
        local_count, state = 0, 1
        indices_dict, result_dict = {}, {}
        for (start, end) in indices:
            indices_dict[(start, end)], result_dict[(start, end)] = [0, 0], 0
        for i, ch in enumerate(text):
            for (start, end) in indices_dict:
                if start <= i < end:
                    if ch == '|':
                        result_dict[(start, end)] += indices_dict[(start, end)][local_count]
                        indices_dict[(start, end)] = [0, 1]  # local_count = 0, state = 1
                    else:
                        indices_dict[(start, end)][local_count] += indices_dict[(start, end)][state]
        return result_dict

    def contained_items_v5(self, text: str, indices: List[tuple[int, int]]) -> Dict[tuple[int, int], int]:  # O(n)
        count, local_count, state = 0, 0, 0
        local_values = [0 for _ in range(len(text))]
        count_values = [0 for _ in range(len(text))]
        last_pipe = -1
        result_dict = {(start, end): 0 for (start, end) in indices}
        for i, ch in enumerate(text):
            if ch == '|':
                count += local_count
                local_count, state = 0, 1
                if last_pipe != -1:
                    local_values[last_pipe + 1] = count
                last_pipe = i
            else:
                local_count += state
            count_values[i] = count

        for i in range(1, len(local_values)):
            local_values[i] = max(local_values[i], local_values[i - 1])

        for (start, end) in indices:
            if start < end - 1 < len(local_values):
                result_dict[(start, end)] = count_values[end - 1] - local_values[start]

        return result_dict

    def contained_items_v6(self, text: str, indices: List[tuple[int, int]]) -> Dict[tuple[int, int], int]:  # O(n)
        count, local_count, state, last_pipe = 0, 0, 0, -1
        local_values = [[0, 0] for _ in range(len(text))]
        result_dict = {(start, end): 0 for (start, end) in indices}
        for i, ch in enumerate(text):
            if ch == '|':
                count += local_count
                local_count, state = 0, 1
                if last_pipe != -1:
                    local_values[last_pipe + 1][1] = count
                last_pipe = i
            else:
                local_count += state
            local_values[i][0] = count

        for i in range(1, len(local_values)):
            local_values[i][1] = max(local_values[i][1], local_values[i - 1][1])

        for (start, end) in indices:
            if start < end - 1 < len(local_values):
                result_dict[(start, end)] = local_values[end - 1][0] - local_values[start][1]

        return result_dict
# ----------------------------------------------------------------------------------------------------------------------


examples = {
    # "|**|*|*********": {(0, 5): 2, (0, 6): 3, (1, 7): 1},
    # "|**|*|********": {(0, 5): 2, (0, 6): 3, (3, 7): 1},
    # "|**|*|**********": {(0, 5): 2, (0, 6): 3, (4, 7): 0},
    # "|**|*|*": {(0, 5): 2, (0, 6): 3, (1, 7): 1},
    # "": {(0, 5): 0, (0, 6): 0, (1, 7): 0},
    # "|***|*|*": {(0, 5): 3, (0, 6): 3, (1, 7): 1},
    # "|***|*|*|": {(0, 5): 3, (0, 6): 3, (1, 9): 2},
    "|***|*|**|******": {(0, 5): 3, (0, 6): 3, (1, 9): 1, (1, 10): 3},
    "|***|": {(0, 5): 3},
    "|***": {(0, 5): 0},
    "***|": {(0, 5): 0},
    "|": {(0, 5): 0},
    "||*|": {(0, 2): 0, (1, 4): 1},
    "********||": {(0, 2): 0, (1, 4): 0},
    "********|*|": {(0, 2): 0, (4, 11): 1},
}

sol = Solution()
for ex in examples:
    print(
        'Ref..: %s <-> %s == %s' % (
            ex, examples[ex], examples[ex] == sol.contained_items(ex, list(examples[ex].keys()))
        )
    )
    # print(
    #     'V2...: %s <-> %s == %s' % (
    #         ex, examples[ex], examples[ex] == sol.contained_items_v2(ex, list(examples[ex].keys()))
    #     )
    # )
    # print(
    #     'V3...: %s <-> %s == %s' % (
    #         ex, examples[ex], examples[ex] == sol.contained_items_v3(ex, list(examples[ex].keys()))
    #     )
    # )
    # print(
    #     'V4...: %s <-> %s == %s' % (
    #         ex, examples[ex], examples[ex] == sol.contained_items_v4(ex, list(examples[ex].keys()))
    #     )
    # )
    print(
        'V5...: %s <-> %s == %s' % (
            ex, examples[ex], examples[ex] == sol.contained_items_v5(ex, list(examples[ex].keys()))
        )
    )
    print()
# ----------------------------------------------------------------------------------------------------------------------
