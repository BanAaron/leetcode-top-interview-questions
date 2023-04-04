class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        # store the length of the shorted word in our list
        length = min(len(i) for i in strs)

        # we will store values in a set so we only count 1 of each distinct character
        stack = set()
        result = ""

        # only bother looping through enough times to reach our shorted length
        for index in range(0, length):
            # loop through each string in our list
            for string in strs:
                # add the current character to our set()
                stack.add(string[index])
            # if the length of our stack is 1 it means that all characters were the same
            if len(stack) == 1:
                # so we store it in results and remove it using pop()
                result += stack.pop()

        # we then simply return our result. If there are no matches it will be an empty string as required
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.longestCommonPrefix(["flower", "flow", "flight"]))
    print(s.longestCommonPrefix(["dog", "racecar", "car"]))
    print(s.longestCommonPrefix(["a"]))
