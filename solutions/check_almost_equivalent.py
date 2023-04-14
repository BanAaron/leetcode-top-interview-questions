class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        characters = set(word1 + word2)
        for character in characters:
            if abs(word1.count(character) - word2.count(character)) > 3:
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.checkAlmostEquivalent("aaaa", "bccb"))
    print(s.checkAlmostEquivalent("aaron", "baron"))
