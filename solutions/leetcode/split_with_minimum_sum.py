class Solution:
    def splitNum(self, numbers: int) -> int:
        # convert out number into a list of strings in ascending order
        numbers = sorted(list(str(numbers)))

        # store num1, num2 as strings
        num1, num2 = "", ""

        # ::2 means loop through the list starting at 0 and ending at the last index in increments of 2
        for number in numbers[::2]:
            num1 += number

        # 1::2 does the same as above but starts at the index of 1 of the list
        for number in numbers[1::2]:
            num2 += number

        # simply return the sum of num1 + num2 as integers
        return int(num1) + int(num2)


if __name__ == "__main__":
    s = Solution()
    print(s.splitNum(4325))
    print(s.splitNum(687))
