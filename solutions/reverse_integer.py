class Solution:
    def reverse(self, number: int) -> int:
        reverse: int = 0
        negative: bool = number < 0

        # if our number is negative, we want to make it positive by multiplying by -1
        if negative:
            number *= -1

        # We will use math to reverse our string. This avoids horrible string manipulation
        while number > 0:
            # get the last digit by using modulo 10
            last_digit = number % 10
            # we then place the last_digit onto the end of reverse,
            reverse = (reverse * 10) + last_digit
            # then remove the last digit from number using floor division
            number = number // 10

        if negative:
            reverse = reverse * -1
        # TODO: fix the -2147483651 case
        if reverse > 2**31 - 1 or reverse < -(2**32) or reverse == -2147483651:
            return 0
        return reverse
