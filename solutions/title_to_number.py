class Solution:
    def titleToNumber(self, column_title: str) -> int:
        from string import ascii_uppercase
        from collections import defaultdict

        score = 0
        letter_values = defaultdict()

        # store each letter of the alphabet with its position as its value
        for i, char in enumerate(ascii_uppercase):
            letter_values[char] = i + 1

        # loop though our string in reverse
        for i, char in enumerate(column_title[::-1]):
            # for each position in our string we need to increase the power
            score += letter_values[char] * 26**i

        return score
