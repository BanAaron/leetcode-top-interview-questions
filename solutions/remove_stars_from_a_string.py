class Solution:
    def removeStars(self, s: str) -> str:
        # we will store characters in a list
        answer = list()

        for char in s:
            if char == "*":
                # if the character is a star we remove the last item in our list
                answer.pop()
            else:
                # else we just add the character onto the end
                answer.append(char)

        return "".join(answer)


if __name__ == "__main__":
    sol = Solution()
    print(sol.removeStars("leet**cod*e"))
    print(sol.removeStars("erase*****"))
