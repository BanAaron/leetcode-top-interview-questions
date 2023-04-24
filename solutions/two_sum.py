def two_sum(nums: list[int], target: int) -> list[int]:
    store = {}

    for index, number in enumerate(nums):
        if target - number in store:
            return [store[target - number], index]
        else:
            store[number] = index
