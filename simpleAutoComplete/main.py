# Implement a simple version of autocomplete, where given an input string s and a dictionary of words dict,
# return the word(s) in dict that partially match s (or an empty string if nothing matches).
#
# Example:
#
# let dict = ['apple', 'banana', 'cranberry', 'strawberry']
#
# $ simpleAutocomplete('app')
# $ ['apple']
#
# $ simpleAutocomplete('berry')
# $ ['cranberry', 'strawberry']
#
# $ simpleAutocomplete('fart')
# $ []
# ----------------------------------------------------------------------------------------------------------------------

import heapq
from typing import List
# ----------------------------------------------------------------------------------------------------------------------


class SuffixArray:
    MARK_SYMBOL = '$'
    ALPHABET_SIZE = 256  # ASCII

    def __init__(self, words: List[str]):
        self.words = words
        arrays = []
        for i, word in enumerate(self.words):
            arrays.append([(i, o) for o in self._build_array_for_word(word)])
        self._merge_arrays(arrays)

    def _sort_characters(self, word: str) -> List[int]:
        order = [0 for _ in range(0, len(word))]
        count = [0 for _ in range(0, SuffixArray.ALPHABET_SIZE)]
        for char in word:
            count[ord(char)] += 1
        for i in range(1, len(count)):
            count[i] += count[i - 1]
        for i in reversed(range(0, len(word))):
            char = word[i]
            count[ord(char)] -= 1
            order[count[ord(char)]] = i
        return order

    def _get_char_classes(self, word: str, order: List[int]) -> List[int]:
        classes = [0 for _ in range(0, len(word))]
        for i in range(1, len(order)):
            if word[order[i]] != word[order[i - 1]]:
                classes[order[i]] = classes[order[i - 1]] + 1
            else:
                classes[order[i]] = classes[order[i - 1]]
        return classes

    def _sort_doubled(self, word: str, current_length: int, order: List[int], classes: List[int]) -> List[int]:
        count = [0 for _ in range(0, len(word))]
        new_order = [0 for _ in range(0, len(word))]
        for i in range(0, len(word)):
            count[classes[i]] += 1
        for i in range(1, len(word)):
            count[i] += count[i - 1]
        for i in reversed(range(0, len(word))):
            start_idx = (order[i] - current_length + len(word)) % len(word)
            clazz = classes[start_idx]
            count[clazz] -= 1
            new_order[count[clazz]] = start_idx
        return new_order

    def _update_classes(self, new_order: List[int], classes: List[int], current_length: int) -> List[int]:
        new_classes = [0 for _ in range(0, len(new_order))]
        for i in range(1, len(new_order)):
            curr, prev = new_order[i], new_order[i - 1]
            mid, mid_prev = (curr + current_length) % len(new_order), ((prev + current_length) % len(new_order))
            if(
                classes[curr] != new_classes[prev] or
                classes[mid] != new_classes[mid_prev]
            ):
                new_classes[curr] = new_classes[prev] + 1
            else:
                new_classes[curr] = new_classes[prev]
        return new_classes

    def _build_array_for_word(self, word: str) -> List[int]:
        word += SuffixArray.MARK_SYMBOL
        order = self._sort_characters(word)
        classes = self._get_char_classes(word, order)
        length = 1
        while length < len(word):
            order = self._sort_doubled(word, length, order, classes)
            classes = self._update_classes(order, classes, length)
            length *= 2
        return order

    def _merge_arrays(self, arrays: list[list[tuple[int, int]]]):
        self.array = []
        for i, _ in enumerate(arrays):
            self.words[i] += SuffixArray.MARK_SYMBOL

        def key_func(index):
            word_idx, order = index
            return self.words[word_idx][order:]

        self.array = list(heapq.merge(*arrays, key=key_func))

    def get_suffixes(self):
        result = []
        for (word_idx, order) in self.array:
            result.append(self.words[word_idx][order:])
        return result

    def _get_close_results(self, sub_word: str, pos: int) -> List[str]:
        result = set()

        for i in reversed(range(0, pos)):
            (word_idx, order) = self.array[i]
            suffix = self.words[word_idx][order:]
            min_len = min(len(sub_word), len(suffix))
            trunc_suffix = suffix[:min_len]
            if trunc_suffix != sub_word:
                break
            result.add(word_idx)

        for i in range(pos, len(self.array)):
            (word_idx, order) = self.array[i]
            suffix = self.words[word_idx][order:]
            min_len = min(len(sub_word), len(suffix))
            trunc_suffix = suffix[:min_len]
            if trunc_suffix != sub_word:
                break
            result.add(word_idx)

        return [self.words[word_idx][:-1] for word_idx in result]

    def auto_complete(self, sub_word: str) -> List[str]:
        if len(sub_word) == 0:
            return [word[:-1] for word in self.words]
        left, right = 0, len(self.array) - 1
        while left <= right:
            mid = left + (right - left) // 2
            (word_idx, order) = self.array[mid]
            suffix = self.words[word_idx][order:]
            min_len = min(len(sub_word), len(suffix))
            trunc_suffix = suffix[:min_len]

            if sub_word < trunc_suffix:
                right = mid - 1
            elif sub_word > trunc_suffix:
                left = mid + 1
            else:
                return self._get_close_results(sub_word, mid)

        return []

# ----------------------------------------------------------------------------------------------------------------------


examples = {
    'app': ['apple'],
    'pp': ['apple'],
    'a': ['apple', 'banana', 'cranberry', 'strawberry'],
    'berry': ['cranberry', 'strawberry'],
    'erry': ['cranberry', 'strawberry'],
    'strawberry': ['strawberry'],
    'strawberry12': [],
    'err': ['cranberry', 'strawberry'],
    'y': ['cranberry', 'strawberry'],
    '': ['apple', 'banana', 'cranberry', 'strawberry'],
    'fart': [],
}

sol = SuffixArray(['apple', 'banana', 'cranberry', 'strawberry'])
suffixes = sol.get_suffixes()
for ex in examples:
    input_ex, expected = ex, examples[ex]
    print('Ref..: %s:\n\tExp: %s\n\tRes: %s' % (input_ex, expected, sol.auto_complete(input_ex)))
    print()
# ----------------------------------------------------------------------------------------------------------------------
