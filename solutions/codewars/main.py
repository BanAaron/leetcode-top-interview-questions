def array_diff(a, b):
    # this list comprehension loops through a and only returns numbers that are not in b
    # this should be faster than a loop because we get to use a hash map instead
    return [num for num in a if num not in b]


if __name__ == "__main__":
    print(array_diff([1, 2, 3], [1, 2]))
