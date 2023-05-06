class Solution:
    def fizzBuzz(self, number: int) -> list[str]:
        # store the outcome in result
        result = []
        # a dictionary to store our values to match on
        rules = {
            5: "Buzz",
            3: "Fizz",
        }

        # loop through our number + 1 to make it inclusive
        for n in range(1, number + 1):
            answer = ""
            # loop through our rules
            for key, value in rules.items():
                # check if our number modulo the rule key is 0
                if n % key == 0:
                    # concatenate answer string with the value from the dictionary
                    answer += value
            # append the resulting answer to results OR n as a string if we haven't matched any cases and answer is
            # an empty string
            result.append(answer or str(n))

        return result


if __name__ == "__main__":
    s = Solution()
    print(s.fizzBuzz(101))
