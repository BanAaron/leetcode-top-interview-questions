class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        # we will store our answer in result
        result = []
        # dictionary containing our conditions
        rules = {3: "Fizz", 5: "Buzz"}

        for x in range(1, n + 1):
            # we will store each answer in this string
            answer = ""
            # loop through our dictionary
            for key, value in rules.items():
                # if our number modulo key (6 % 3 for example) is equal to zero
                if x % key == 0:
                    # we can add the value from the dictionary to the answer
                    # 3 = "Fizz" for example
                    answer += value
            # after we are done checking against the dictionary we append the answer to our results
            # (answer or str(x)) will append answer if it is not an empty string or append x as a string if answer is
            # empty
            result.append(answer or str(x))

        return result


if __name__ == "__main__":
    s = Solution()
    print(s.fizzBuzz(100))
