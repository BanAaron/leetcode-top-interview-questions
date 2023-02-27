def fizz_buzz(start: int = 1, end: int = 100, divisors: tuple = (3, 5)) -> list[str]:
    """
    a function that returns the answer to the fizz buzz game
    :param start: start counting from here
    :param end: stop count here
    :param divisors: the numbers to divide against
    :return: List of strings
    """
    divisors_len = len(divisors)
    result = []

    divisors0 = divisors[0]
    divisors1 = divisors[1]

    if divisors_len != 2:
        raise Exception(f"factors can only contain 2 items.")
    if end <= start:
        raise Exception(f"end must be greater than start.")
    else:
        for x in range(start, end + 1):
            if x % divisors0 == 0 and x % divisors1 == 0:
                result.append("Fizz Buzz")
            elif x % divisors0 == 0:
                result.append("Fizz")
            elif x % divisors1 == 0:
                result.append("Buzz")
            else:
                result.append(str(x))
    return result


print(fizz_buzz())
