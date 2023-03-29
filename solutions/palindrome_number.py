class Solution:
    def isPalindrome(self, x: int) -> bool:
        # returns true if x is the same as x reversed
        return str(x) == str(x)[::-1]


if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(5))
    print(s.isPalindrome(-101))
    print(s.isPalindrome(101))
