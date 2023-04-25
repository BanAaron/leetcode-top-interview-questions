class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        answer = []
        for x in range(1, n + 1):
            # if our number modulo 3 and 5 is 0 we can return "FizzBuzz"
            if x % 3 == 0 and x % 5 == 0:
                answer.append("FizzBuzz")
            # the same logic for only 5
            elif x % 5 == 0:
                answer.append("Buzz")
            # again for 3
            elif x % 3 == 0:
                answer.append("Fizz")
            # if we don't match any cases we can just append the number as a string
            else:
                answer.append(str(x))
        return answer
