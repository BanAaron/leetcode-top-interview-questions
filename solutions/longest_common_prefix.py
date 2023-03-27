class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        length = min(len(i) for i in strs)
        store = set()
        result = ""

        for index in range(0, length):
            for string in strs:
                store.add(string[index])
            if len(store) == 1:
                a = store.pop()
                result += a
            else:
                break

        return result


if __name__ == "__main__":
    s = Solution()
    print(s.longestCommonPrefix(["flower", "flow", "flight"]))
    print(s.longestCommonPrefix(["dog", "racecar", "car"]))
    print(s.longestCommonPrefix(["a"]))
