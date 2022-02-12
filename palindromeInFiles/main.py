# You are given three files named first_page.txt, second_page.txt, and third_page.txt with the occurrence of at least
# one palindrome in each of them. Write a script to find the following:
#
# The exact number of palindromes in each file.
# The line numbers of the palindromes in each file.
# ----------------------------------------------------------------------------------------------------------------------


from typing import List
from collections import Counter, defaultdict
# ----------------------------------------------------------------------------------------------------------------------


class Palindrome:
    def _hasPalindromeSubstring(self, word: str, min_size: int) -> bool:
        for i in range(1, len(word)):
            left = i - 1
            right = i
            while (left >= 0) and (right < len(word)) and (word[left] == word[right]):
                left -= 1
                right += 1
            left += 1
            right -= 1
            if (word[left] == word[right]) and (right - left + 1 > min_size):
                return True
            left = i - 1
            right = i + 1
            while (left >= 0) and (right < len(word)) and (word[left] == word[right]):
                left -= 1
                right += 1
            left += 1
            right -= 1
            if word[left] == word[right] and right - left + 1 > min_size:
                return True
        return False

    def searchPalindromeLines(self, filename: str, min_size: int = 2) -> List:
        result = []
        with open(filename, 'r') as file:
            lines_count = 0
            while line := file.readline():
                for word in line.split(' '):
                    if self._hasPalindromeSubstring(word, min_size):
                        result.append(lines_count)
                        break
                lines_count += 1
        return result


sol = Palindrome()
filenames = ['first_page.txt', 'second_page.txt', 'third_page.txt']
for page_filename in filenames:
    res = sol.searchPalindromeLines(page_filename)
    print('File: %s - Number of palindromes: %d - Palindromes in lines: %s' % (page_filename, len(res), res))

import wolframalpha
import ssl

APP_ID = 'U4REU5-Y94KJTUTYE'
ssl._create_default_https_context = ssl._create_unverified_context

def get_factorial(num: int) -> int:
    client = wolframalpha.Client(APP_ID)
    res = client.query('%d!' % num)
    return int(next(res.results).text)


print(get_factorial(5))
# ----------------------------------------------------------------------------------------------------------------------
