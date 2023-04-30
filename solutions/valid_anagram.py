class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # I have testing a solution with Counters. But it seems to be slower unless your words are extremely long.
        if sorted(s) == sorted(t):
            return True
        else:
            return False
