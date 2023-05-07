class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # Counter takes an input and creates a dictionary with the elements of our array as the key and the number of
        # occurrences as the value
        from collections import Counter

        count = Counter(nums)

        # we then return the value where the counter[x] value is greater than len(nums) / 2
        return [x for x in count if count[x] > len(nums) / 2][0]
