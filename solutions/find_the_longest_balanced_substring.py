class Solution:
    def findTheLongestBalancedSubstring(self, string: str) -> int:
        x = ""
        for i in range(25):
            x = "0" + x + "1"
            if x not in string:
                return i * 2
        return 50


if __name__ == "__main__":
    s = Solution()
    print(s.findTheLongestBalancedSubstring("01000111"))
    print(s.findTheLongestBalancedSubstring("00111"))
    print(s.findTheLongestBalancedSubstring("111"))
