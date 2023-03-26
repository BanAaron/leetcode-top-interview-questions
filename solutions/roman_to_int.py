class Solution:
    def romanToInt(self, s: str) -> int:
        ints = []
        chars = s

        def add(number):
            ints.append(number)

        for index, char in enumerate(chars):
            if char == "I" and index + 1 < len(chars):
                if chars[index + 1] in ("V", "X"):
                    add(-1)
                else:
                    add(1)
            elif char == "X" and index + 1 < len(chars):
                if chars[index + 1] in ("L", "C"):
                    add(-10)
                else:
                    add(10)
            elif char == "C" and index + 1 < len(chars):
                if chars[index + 1] in ("D", "M"):
                    add(-100)
                else:
                    add(100)
            elif char == "I":
                add(1)
            elif char == "V":
                add(5)
            elif char == "X":
                add(10)
            elif char == "L":
                add(50)
            elif char == "C":
                add(100)
            elif char == "D":
                add(500)
            elif char == "M":
                add(1000)
        return sum(ints)


if __name__ == "__main__":
    s = Solution()
    print(s.romanToInt("III"))
    print(s.romanToInt("LVIII"))
    print(s.romanToInt("MCMXCIV"))
