class Solution:
    def minNumber(self, nums1: list[int], nums2: list[int]) -> int:
        result: list[str] = []

        # loop through all the numbers we have
        for x in set(nums1 + nums2):
            # if num1 and nums2 contains this number then we know it is the smallest possible number
            if x in nums1 and x in nums2:
                return x

        # else we store the smallest number from each list into a list
        result.append(str(min(nums1)))
        result.append(str(min(nums2)))

        # sort the list in sending order
        result = sorted(result)

        # concatenate them together as a string, then cast to int and return
        return int("".join([str(x) for x in result]))


if __name__ == "__main__":
    s = Solution()
    print(s.minNumber(nums1=[7, 5, 6], nums2=[1, 4]))
