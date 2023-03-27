class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        length = min(len(i) for i in strs)
        stack = set()
        result = ""

        for index in range(0, length):
            for string in strs:
                stack.add(string[index])
            if len(stack) == 1:
                result += stack.pop()
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.longestCommonPrefix(["flower", "flow", "flight"]))
    print(s.longestCommonPrefix(["dog", "racecar", "car"]))
    print(s.longestCommonPrefix(["a"]))
