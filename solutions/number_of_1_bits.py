class Solution:
    def hammingWeight(self, n: int) -> int:
        # convert to binary then use count() to find the sum of 1s
        return bin(n).count("1")

        # initial solution
        # return sum([int(x) for x in bin(n) if x == "1"])


if __name__ == "__main__":
    s = Solution()
    print(s.hammingWeight(11))
