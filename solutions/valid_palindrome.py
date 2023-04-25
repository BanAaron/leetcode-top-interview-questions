class Solution:
    def isPalindrome(self, s: str) -> bool:
        # join on "" so we don't have any spaces
        # filter(str.isalnum) removes any non-alphanumeric characters
        # finally lower() converts our string to lowercase
        s = ("".join(filter(str.isalnum, s))).lower()
        # [::-1] reverses our string
        # So we return the result of the expression s = s-in-reverse
        return s == s[::-1]
