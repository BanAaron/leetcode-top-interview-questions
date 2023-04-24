from itertools import pairwise


def first_non_consecutive(arr):
    for x, y in pairwise(arr):
        if y != x + 1:
            return y


if __name__ == "__main__":
    print(first_non_consecutive([1, 2, 3, 4, 6]))
    print(first_non_consecutive([100, 101, 205]))
