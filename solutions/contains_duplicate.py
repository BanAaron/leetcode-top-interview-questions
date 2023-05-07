class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # create we will store nums in seen as we go along
        seen = set()
        for number in nums:
            # if we have seen the number we can return true
            if number in seen:
                return True
            # add each number to seen as we go through
            seen.add(number)
        # if we get all the way through our list it means there are no duplicates and can return false
        return False


if __name__ == "__main__":
    s = Solution()
    print(s.containsDuplicate([1, 2, 3, 1]))
    print(s.containsDuplicate([1, 2, 3, 4]))
    print(s.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
