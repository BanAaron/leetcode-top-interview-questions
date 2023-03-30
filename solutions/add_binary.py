class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # convert the strings to base 2 integer, add them together, then convert back to binary
        # [2:] removed the first 2 characters "0b" which is not needed
        return bin(int(a, 2) + int(b, 2))[2:]


if __name__ == "__main__":
    s = Solution()
    s.addBinary("11", "1")
