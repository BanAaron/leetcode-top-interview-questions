class Solution:
    @staticmethod
    def findTheDifference(s: str, t: str) -> str:
        for char in t:
            if char not in s:
                return char
            s = s.replace(char, "", 1)


if __name__ == "__main__":
    s = Solution
    print(s.findTheDifference("abcd", "abcde"))
    print(s.findTheDifference("", "y"))
