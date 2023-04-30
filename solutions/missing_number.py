class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        # we know that if the array is [0] the only possible answer can be 1,  so we return early
        if nums == [0]:
            return 1
        # loop through from zero to the biggest number in our list
        for x in range(max(nums) + 1):
            # when we find a number that isn't in our list we know it is the missing one
            if x not in nums:
                return x
        # if we get all the way through our loop we know we must be missing max + 1
        return max(nums) + 1
