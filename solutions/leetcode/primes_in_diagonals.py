def is_prime(n: int) -> bool:
    """
    Returns True if number is prime. Returns False if not
    :param n: a positive integer
    :return: Bool
    """
    for i in range(2, n):
        # if our number % index return False
        if (n % i) == 0:
            return False
    # if there are no divisors return True
    return True


class Solution:
    def diagonalPrime(self, nums: list[list[int]]) -> int:
        length = len(nums)
        # we want to return 0 if there are no primes found
        max_prime = 0

        # loop through our array using the index
        for x in range(length):
            # only check if the number is prime if it is less than our current max_prime
            if max_prime < nums[x][x]:
                if is_prime(nums[x][x]):
                    max_prime = max(nums[x][x], max_prime)
            # same log as above but for the opposite diagonal
            if max_prime < nums[length - x - 1][x]:
                if is_prime(nums[length - x - 1][x]):
                    max_prime = max(nums[length - x - 1][x], max_prime)

        # 1 is not considered prime number so we should return 0 in this edge case
        if max_prime == 1:
            return 0
        else:
            return max_prime


if __name__ == "__main__":
    s = Solution()
    print(s.diagonalPrime([[1, 2, 3], [5, 6, 7], [9, 10, 11]]))
    print(s.diagonalPrime([[1, 2, 3], [5, 17, 7], [9, 11, 10]]))
