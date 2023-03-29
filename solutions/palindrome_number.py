class Solution:
    def isPalindrome(self, x: int) -> bool:
        # returns result of condition: if x is the same as reversed x
        return str(x) == str(x)[::-1]


if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(5))
    print(s.isPalindrome(-101))
    print(s.isPalindrome(101))
