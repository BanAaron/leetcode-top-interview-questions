class Solution:
    def sum_digits(self, number):
        # list comprehension to loop through the number, square each number and store the sum
        total = sum([int(n) ** 2 for n in str(number)])

        # once we have narrowed down our answer to a single digit we know the result and can return
        if len(str(total)) == 1:
            return total
        else:
            # recursively call this function with the new total
            return self.sum_digits(total)

    def isHappy(self, n: int) -> bool:
        # we know that the only single digit happy numbers can be 1 or 7
        if self.sum_digits(n) in (1, 7):
            return True
        else:
            return False


if __name__ == "__main__":
    s = Solution()
    print(s.isHappy(19))
    print(s.isHappy(2))
    print(s.isHappy(1111111))
