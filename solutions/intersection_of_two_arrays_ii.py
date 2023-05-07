class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        from collections import Counter

        # create counters for each list
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)
        # store our results in result
        result: list[int] = []

        for key, value in counter1.items():
            if key in counter2:
                # get the minimum number of occurrences between counter1 and counter2 for the current value
                min_count = min(value, counter2[key])
                # extend result with they key * the number of occurrences
                result.extend([key] * min_count)

        return result


if __name__ == "__main__":
    s = Solution()
    print(s.intersect([1, 2, 2, 1], [2, 2]))  # [2, 2]
    print(s.intersect([4, 9, 5], [9, 4, 9, 8, 4]))  # [4 , 9]
    print(s.intersect([1, 2], [1, 1]))  # [1]
