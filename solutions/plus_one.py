class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        # if the last element is 9
        if digits[-1] == 9:
            # and if list only has 1 element, and it is 9 we know the only valid result is [1, 0]
            if len(digits) == 1:
                return [1, 0]
            # otherwise call plusOne() without the last element and then append [0] onto the end
            return self.plusOne(digits[:-1]) + [0]
        # if the last element isn't a 9 we can just +1
        else:
            digits[-1] += 1
        return digits
