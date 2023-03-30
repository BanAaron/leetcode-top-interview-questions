class Solution:
    def isValid(self, s: str) -> bool:
        stack = ""
        valid_brackets = ("()", "[]", "{}")

        for char in s:
            stack += char
            if char in ")]}":
                # if the final two characters are a valid pair of brackets
                if stack[len(stack) - 2:] in valid_brackets:
                    # remove final two characters
                    stack = stack[:-2]

        return len(stack) == 0


if __name__ == "__main__":
    s = Solution()
    print(s.isValid("()[]{}"))
    print(s.isValid("{[]}"))
    print(s.isValid("{]"))
