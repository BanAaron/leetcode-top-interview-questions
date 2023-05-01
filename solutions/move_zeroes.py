class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # store the numbers of zeros in our array
        number_of_zeroes = nums.count(0)
        # then we only need to loop for each zero
        for x in range(number_of_zeroes):
            # remove and append for each zero
            nums.remove(0)
            nums.append(0)
