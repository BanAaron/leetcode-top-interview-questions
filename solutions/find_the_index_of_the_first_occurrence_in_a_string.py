class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        else:
            return haystack.find(needle)


if __name__ == "__main__":
    s = Solution()
    s.strStr(haystack="sadbutsad", needle="sad")
