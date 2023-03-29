class Solution:
    def vowelStrings(self, words: list[str], left: int, right: int) -> int:
        vowels = ["a", "e", "i", "o", "u"]
        answer = 0

        for word in words[left : right + 1]:
            # words[-1] gives us the last character of the string regardless of the length
            if word[0] in vowels and word[-1] in vowels:
                answer += 1

        return answer


if __name__ == "__main__":
    s = Solution()
    # s.vowelStrings(words=["are", "amy", "u"], left=0, right=2)
    s.vowelStrings(words=["hey", "aeo", "mu", "ooo", "artro"], left=1, right=4)
