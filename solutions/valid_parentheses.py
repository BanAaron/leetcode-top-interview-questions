class Solution:
    def isValid(self, s: str) -> bool:
        stack = ""
        valid_brackets = ("()", "[]", "{}")

        for char in s:
            # add the current char onto the end of the stack
            stack += char
            # whenever we hit a closing bracket
            if char in ")]}":
                # we check if the final two characters make a valid set of brackets
                if stack[len(stack) - 2 :] in valid_brackets:
                    # if it is we cut off the last two characters from the stack
                    stack = stack[:-2]
        # if the length of our stack by the end is 0 it means all brackets were closed properly and we can return True
        return len(stack) == 0
