class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # we know anything zero or smaller cannot be a power of 3, so we can return false
        if n < 1:
            return False

        # loop while n modulo 3 is 0
        while n % 3 == 0:
            # n = n floor divided by 3
            n //= 3

        # if we end up with n == 1 it means the number is a power of three and can return True
        # else returns False
        return n == 1
