class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        positives, negatives = 0, 0
        for num in nums:
            if num > 0:
                positives += 1
            elif num < 0:
                negatives += 1

        return max(positives, negatives)

    # list comprehension solution, sadly slower!
    # def maximumCount(self, nums: list[int]) -> int:
    #     positives = len([num for num in nums if num > 0])
    #     negatives = len([num for num in nums if num < 0])
    #
    #     return max(positives, negatives)


if __name__ == "__main__":
    s = Solution()
    s.maximumCount([-2, -1, -1, 1, 2, 3])
    s.maximumCount([-3, -2, -1, 0, 0, 1, 2])
    s.maximumCount([5, 20, 66, 1314])
