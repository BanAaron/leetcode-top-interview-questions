class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # [:] gives a copy of the whole string in place
        s[:] = reversed(s)
