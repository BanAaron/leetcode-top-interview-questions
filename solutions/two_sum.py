def two_sum(nums: list[int], target: int) -> list[int]:
    # we will store our values in a dictionary
    store = {}

    # loop through nums with an index using enumerate
    for index, number in enumerate(nums):
        # all we do is check if the target number - the current number is in our dictionary
        if target - number in store:
            # if it is we can just return the index from the store dictionary and the current index
            return [store[target - number], index]
        # if not we just store the value in the store dictionary for the next loop
        else:
            store[number] = index
