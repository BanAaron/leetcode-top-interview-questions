class Solution:
    def evenOddBit(self, n: int) -> list[int]:
        evens, odds = 0, 0

        # bin(n)[2:][::-1] convert the n integer to a binary and reverses it
        for index, bit in enumerate(bin(n)[2:][::-1]):
            # then if the index is even and the bit is 1 we increment our evens counter
            if index % 2 == 0 and bit == "1":
                evens += 1
            # same logic again for odd bits
            elif index % 2 == 1 and bit == "1":
                odds += 1

        return [evens, odds]


if __name__ == '__main__':
    s = Solution()
    s.evenOddBit(17)
    s.evenOddBit(2)
