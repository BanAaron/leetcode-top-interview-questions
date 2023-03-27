class Solution:
    def isValid(self, s: str) -> bool:
        stack = ""
        valid_brackets = ("()", "[]", "{}")

        for char in s:
            if char in "([{":
                stack += char
            elif char in ")]}":
                stack += char
                if stack[len(stack) - 2:] in valid_brackets:
                    stack = stack[:-2]

        return len(stack) == 0


if __name__ == "__main__":
    s = Solution()
    print(s.isValid("()[]{}"))
    print(s.isValid("{[]}"))
    print(s.isValid("{]"))
