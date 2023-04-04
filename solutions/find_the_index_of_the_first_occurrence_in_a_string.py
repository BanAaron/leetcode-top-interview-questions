class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # ,find() does all the work for us by returning the index of needle if it exists. If it does not it returns -1
        return haystack.find(needle)


if __name__ == "__main__":
    s = Solution()
    print(s.strStr(haystack="sadbutsad", needle=""))
