class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        while True:
            swapped = False
            for i, _ in enumerate(nums):
                if i < len(nums) - 1 and nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    swapped = True
            if not swapped:
                break
        print(nums)


if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 0]
    s.sortColors(nums)
    nums = [2, 0, 2, 1, 1, 0]
    s.sortColors(nums)
    nums = [2, 0, 1]
    s.sortColors(nums)
