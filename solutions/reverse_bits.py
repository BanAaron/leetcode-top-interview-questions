class Solution:
    def reverseBits(self, n: int) -> int:
        # convert out number to a binary
        n = bin(n)[2:]
        # convert it to a string with a zfill(32) to convert to 32-bit integer binary format
        n = str(n).zfill(32)
        # reverse the string
        n = n[::-1]
        # convert back to an integer with base 2 format
        return int(n, 2)
