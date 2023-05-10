class Solution:
    def longestPalindrome(self, string: str) -> str:
        length = len(string)
        # if our string is already a palindrome, we know we cannot have the longest substring
        if string == string[::-1] or length <= 1:
            return string

        # create our window pointers
        left = 0
        right = 1
        longest = ""

        while left + 1 < length:
            # crete a window view using slices
            current = string[left:right]
            # if the window is a palindrome
            if current == current[::-1]:
                if len(current) > len(longest):
                    longest = current
            # once the right pointer is at the end of the string
            # increment the left pointer by 1
            # and set the right pointer to the left pointer position + 1
            if right == length:
                left += 1
                right = left + 1
            else:
                right += 1

        return longest
