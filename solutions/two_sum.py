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


def two_sum(nums: list[int], target: int) -> list[int]:
    store = {}
    for index, number in enumerate(nums):
        if target - number in store:
            return [store[target - number], index]
        else:
            store[number] = index


if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))
    print(two_sum([3, 2, 4], 6))
    print(two_sum([3, 3], 6))