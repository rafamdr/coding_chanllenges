# Write a function that converts a sentence into Pig Latin.
# ----------------------------------------------------------------------------------------------------------------------
import re
import string
# ----------------------------------------------------------------------------------------------------------------------


class Solution:
    def __init__(self):
        self._vowels_s = 'aeiou'
        self._vowels = set(self._vowels_s)
        self._consonants = set(string.ascii_lowercase).difference(self._vowels)
        self._consonants_s = ''.join(list(set(string.ascii_lowercase).difference(self._vowels)))
        self._actions = {
            r'^([%s]+)[%s]*.*$' % (self._consonants_s, self._vowels_s): self.consonant_sound_start_action,
            r'^([%s]+)[%s]*.*$' % (self._vowels_s, self._consonants_s): self.vowel_sound_start_action
        }

    def consonant_sound_start_action(self, word: str, res):
        pos = len(res.groups()[0])
        if pos == len(word):
            pos -= 1
        return word[pos:] + word[:pos] + 'ay'

    def vowel_sound_start_action(self, word: str, res):
        return word + 'yay'

    def _convert_word(self, word: str):
        first_letter_cap = word[0].isupper()
        word = word.lower()
        for pat in self._actions:
            res = re.match(pat, word.lower())
            if res and len(res.groups()) > 0:
                word = self._actions[pat](word, res)
                break
        if first_letter_cap:
            word = word[0].upper() + word[1:]
        return word

    def pig_latin_converter_ref(self, text: str):
        pos_begin = 0
        word_found = False
        i = 0
        while i < len(text):
            c = text[i].lower()
            if word_found is False:
                if (c in self._consonants_s) or (c in self._vowels_s):
                    word_found = True
                    pos_begin = i
            else:
                if (c not in self._consonants_s) and (c not in self._vowels_s):
                    new_word = self._convert_word(text[pos_begin: i])
                    text = text[:pos_begin] + new_word + text[i:]
                    word_found = False
                    i = len(new_word) + pos_begin
            i += 1
        if word_found:
            new_word = self._convert_word(text[pos_begin: i])
            text = text[:pos_begin] + new_word + text[i:]
        return text
# ----------------------------------------------------------------------------------------------------------------------


examples = {
    ' a': ' ayay',
    'a ': 'ayay ',
    ' ': ' ',
    '': '',
    'try': 'ytray',
    'flyby': 'yflybay',
    'synth': 'hsyntay',

    # # For words that begin with consonant sounds, all letters before the initial vowel are placed at the end of the
    # # word sequence. Then, "ay" is added, as in the following examples:
    "pig": "igpay",
    "latin": "atinlay",
    "banana": "ananabay",
    "will": "illway",
    "butler": "utlerbay",
    "happy": "appyhay",
    "duck": "uckday",
    "me": "emay",

    # # When words begin with consonant clusters (multiple consonants that form one sound), the whole sound is added to
    # # the end when speaking or writing:
    "smile": "ilesmay",
    "string": "ingstray",
    "stupid": "upidstay",
    "glove": "oveglay",
    "trash": "ashtray",
    "floor": "oorflay",
    "store": "orestay",

    # For words that begin with vowel sounds, the vowel is left alone, and most commonly 'yay' is added to the end.
    # But in different parts of the world, there are different 'dialects' of sorts. Some people may add 'way' or
    # 'hay' or other endings. Examples are:
    "eat": "eatyay",
    "omelet": "omeletyay",
    "are": "areyay",
    "egg": "eggyay",
    "explain": "explainyay",
    "always": "alwaysyay",
    "ends": "endsyay",
    "honest": "onesthay",
    "I": "Iyay",

    'This is how you speak in Pig Latin!': 'Isthay isyay owhay ouyay eakspay inyay Igpay Atinlay!'
}

sol = Solution()

for ex in examples:
    res = sol.pig_latin_converter_ref(ex)
    print('Ref..: %s -> (%s : %s) \t %s' % (ex, examples[ex], res, (examples[ex] == res)))
    print()
# ----------------------------------------------------------------------------------------------------------------------
