class Solution:
    def leftRightDifference(self, nums: list[int]) -> list[int]:
        left = []
        right = []

        for i, num in enumerate(nums):
            if i == 0:
                left.append(0)
                right.append(sum(nums[i + 1 :]))
            elif i == len(nums) - 1:
                left.append(sum(nums[:i]))
                right.append(0)
            else:
                left.append(sum(nums[:i]))
                right.append(sum(nums[i + 1 :]))

        print(left)
        print(right)
        return [abs(x[0] - x[1]) for x in zip(left, right)]


if __name__ == "__main__":
    s = Solution()
    print(s.leftRightDifference([10, 4, 8, 3]))
