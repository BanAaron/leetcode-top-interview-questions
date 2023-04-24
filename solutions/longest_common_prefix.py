class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        # store the shortest string from strs
        length = min(len(i) for i in strs)
        stack = set()
        result = ""

        # we loop through length, so we only loop the minimum amount of times required
        # also prevents us getting an out-of-bounds error
        for index in range(0, length):
            for string in strs:
                # because stack is a set() it can only contain unique values
                stack.add(string[index])
            # if the length of the stack is 1 we all characters must have been the same
            if len(stack) == 1:
                # store the character in our result to return later
                result += stack.pop()
        return result
