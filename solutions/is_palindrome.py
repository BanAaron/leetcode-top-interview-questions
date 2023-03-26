class Solution:
    def isPalindrome(self, x: int) -> bool:
        store = zip(str(x), reversed(str(x)))
        for i in store:
            if i[0] != i[1]:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(5))
    print(s.isPalindrome(-101))
    print(s.isPalindrome(101))
