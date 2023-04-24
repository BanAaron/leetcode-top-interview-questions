class Solution:
    def __init__(self):
        self.answer = 0

    def romanToInt(self, s: str) -> int:
        chars = s

        def add(number):
            self.answer += number

        # inelegantly replace all the edge special cases with simplified versions. IV (4) becomes IIII (1,1,1,1) etc
        chars = (
            chars.replace("IV", "IIII")
            .replace("IX", "VIIII")
            .replace("XL", "XXXX")
            .replace("XC", "LXXXX")
            .replace("CD", "CCCC")
            .replace("CM", "DCCCC")
        )

        # basically a switch statement to map each possible roam-nc numeral to an integer value and add it up
        for char in chars:
            match char:
                case "I":
                    add(1)
                case "V":
                    add(5)
                case "X":
                    add(10)
                case "L":
                    add(50)
                case "C":
                    add(100)
                case "D":
                    add(500)
                case "M":
                    add(1000)

        return self.answer
