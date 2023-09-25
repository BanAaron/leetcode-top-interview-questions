class Solution:
    @staticmethod
    def longestCommonPrefix(strings: list[str]) -> str:
        shortest_element_length = min(len(i) for i in strings)
        stack = set()
        result = ""

        for index in range(0, shortest_element_length):
            for string in strings:
                string_index = string[index]
                stack.add(string_index)
            if len(stack) == 1:
                result += stack.pop()
        return result
