class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # strip() removes any leading/trailing spaces
        # spit(" ") then creates a list splitting each element by each space
        s = s.strip().split(" ")

        # then simply return the length of the last element
        return len(s[len(s) - 1])


if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLastWord("Hello World"))
    print(s.lengthOfLastWord("   fly me   to   the moon  "))
    print(s.lengthOfLastWord("luffy is still joyboy"))
