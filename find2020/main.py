# This week’s question:
# You’re given a string of characters that are only 2s and 0s. Return the index of the first occurrence of “2020” 
# without using the indexOf (or similar) function, and -1 if it’s not found in the string.

# Example:
# $ find2020('2220000202220020200')
# $ 14
# ---------------------------------------------------------------------------------------------------------------------


class Solution:
    
    def find2020_ref(self, text: str) -> int:
        substr = '2020'
        substr_idx = 0
        for i in range(len(text)):
            if substr_idx < len(substr):
                if text[i] == substr[substr_idx]:
                    substr_idx += 1
                elif text[i] == substr[0]:
                    substr_idx = 1
                else:
                    substr_idx = 0
            else:
                return i - len(substr)

        return -1 if substr_idx < len(substr) else len(text) - len(substr)
# ---------------------------------------------------------------------------------------------------------------------


def main():
    examples = {
        '2220000202220020200': 14,
        '': -1,
        '2': -1,
        '20': -1,
        '202': -1,
        '2020': 0,
        '02020': 1,
        '0020202': 2,
        '0022020222222220': 3,
        '20220202220': 3,
        '202002022222': 0,
    }
    sol = Solution()
    for key in examples:
        print('Ref......: Exp = %s  ->  Res = %s for %s' % (examples[key], sol.find2020_ref(key), key))
        print()
# ---------------------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    main()
# ---------------------------------------------------------------------------------------------------------------------
