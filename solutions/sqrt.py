class Solution:
    def mySqrt(self, x: int) -> int:
        # we cannot divide by 0, so we need to deal with this case manually
        if x == 0:
            return 0
        last_guess = x / 2.0
        while True:
            guess = (last_guess + x / last_guess) / 2
            if abs(guess - last_guess) < 0.000001:
                return int(guess)
            last_guess = guess


# I honestly don't understand how this works. All credit goes to tzot on stack overflow:
# https://stackoverflow.com/a/3047531/4698121
# It appears to be Babylonian Method https://www.wikiwand.com/en/Methods_of_computing_square_roots#Babylonian_method
