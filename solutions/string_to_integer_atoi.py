from string import digits


class Solution:
    def myAtoi(self, string: str) -> int:
        string = string.strip()
        prefix: str = ""
        number_string = ""
        found = False

        if string[0] in ("-", "+"):
            prefix = string[0]
            string = string[1:]

        for char in string:
            if char in digits and not found:
                found = True
            if char not in digits and found:
                return int(prefix + number_string)
            elif found:
                number_string += char

        return int(prefix + number_string)
