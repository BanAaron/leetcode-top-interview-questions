class Solution:
    def isValid(self, s: str) -> bool:
        stack = ""
        valid_brackets = ("()", "[]", "{}")

        for char in s:
            stack += char
            if char in ")]}":
                if stack[len(stack) - 2 :] in valid_brackets:
                    stack = stack[:-2]

        return len(stack) == 0
