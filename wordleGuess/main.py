# Using the rules of Wordle, given a guessWord and a solutionWord, return a set of emojis returned from the guessWord.
#
# Example:
#
# let solutionWord = "fudge"
#
# $ wordleGuess("reads", solutionWord)
# $ "⬛🟨⬛🟨⬛"
#
# $ wordleGuess("lodge", solutionWord)
# $ "⬛⬛🟩🟩🟩"
# ----------------------------------------------------------------------------------------------------------------------


from typing import List
from collections import Counter, defaultdict
# ----------------------------------------------------------------------------------------------------------------------


class Wordle:
    def __init__(self, solution_word):
        self.solution_dict = defaultdict(set)
        for idx, letter in enumerate(solution_word):
            self.solution_dict[letter].add(idx)

    def guess(self, word: str) -> str:
        result = ['⬛'] * len(word)
        found = set()
        for idx, ch in enumerate(word):
            if (ch not in found) and (ch in self.solution_dict):
                result[idx] = '🟩' if (idx in self.solution_dict[ch]) else '🟨'
                found.add(ch)
        return ''.join(result)
# ----------------------------------------------------------------------------------------------------------------------


examples = {
    "fudge": {
        'reads': '⬛🟨⬛🟨⬛',
        'lodge': '⬛⬛🟩🟩🟩',
        '': ''
    },
    "knoll": {
        'known': '🟩🟩🟩⬛⬛',
        'lodge': '🟨🟨⬛⬛⬛',
        '': ''
    }
}

for ex in examples:
    sol = Wordle(ex)
    for word in examples[ex]:
        print('V1..:\t[%s] %s -> %s : %s' % (ex, word, examples[ex][word], sol.guess(word)))
    print()
# ----------------------------------------------------------------------------------------------------------------------
