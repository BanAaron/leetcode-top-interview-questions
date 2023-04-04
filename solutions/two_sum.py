# def two_sum(nums: list[int], target: int) -> list[int]:
#     answer = []
#     for x, number in enumerate(nums):
#         for y, num in enumerate(nums):
#             if number == num and x == y:
#                 pass
#             elif number + num == target:
#                 answer = [x, y]
#                 break
#     return answer


class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        store = {}

        # leep through nums
        for index, number in enumerate(nums):
            # if our target - the current number exists in our store then we can just return the the result
            if target - number in store:
                return [store[target - number], index]
            # otherwise store the value and move on
            else:
                store[number] = index


if __name__ == "__main__":
    s = Solution()
    print(s.two_sum([2, 7, 11, 15], 9))
    print(s.two_sum([3, 2, 4], 6))
    print(s.two_sum([3, 3], 6))
