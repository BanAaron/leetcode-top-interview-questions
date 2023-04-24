class Solution:
    def minMaxDifference(self, num: int) -> int:
        # store out number as a maximum
        maximum = num
        # cast out number to a string
        num = str(num)

        # loop through each character in our string from left to right
        for n in num:
            # on the first character that is not 9
            if n != "9":
                # replace the character with 9, then cast it to an int and store it as maximum
                maximum = int(num.replace(n, "9"))
                # we then break to not repeat this process again
                break

        # simply return the maximum - minimum
        # we always know minimum will be whatever the frst character in our string is replaced with 0 so we do not need
        # to loop through and check anything
        return maximum - int(num.replace(num[0], "0"))


if __name__ == "__main__":
    s = Solution()
    s.minMaxDifference(11891)
