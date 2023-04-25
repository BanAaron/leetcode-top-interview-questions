class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        from collections import Counter

        # Counter is basically a dictionary that only counts occurrences in a string/list
        # we create a counter using our list of numbers
        count = Counter(nums)
        # then simply return whichever number that hasn't been counted exactly twice
        return [int(x) for x in count if count[x] != 2][0]
