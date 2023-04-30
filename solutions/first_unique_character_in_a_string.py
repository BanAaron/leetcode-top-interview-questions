class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i, char in enumerate(s):
            # if there is exactly 1 occurrence of our character in the string we can return its index
            if s.count(char) == 1:
                return i
        return -1
