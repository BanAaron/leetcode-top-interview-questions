class Solution:
    def removeDuplicates(self, nums):
        # sets can only contain unique values. So we can just convert to a set and sort it to maintain the order
        # [:] gives a copy of the string in place
        nums[:] = sorted(set(nums))
        return len(nums)
