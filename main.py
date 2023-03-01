def fizz_buzz(start: int = 1, end: int = 100, divisors: tuple = (3, 5)) -> list:
    """
    a function that returns the answer to the fizz buzz game.
    :param start: start counting from here.
    :param end: stop count here.
    :param divisors: the numbers to divide against.
    :return: List of strings.
    """
    divisors_len = len(divisors)
    divisor1 = divisors[0]
    divisor2 = divisors[1]
    result = []

    if divisors_len != 2:
        raise Exception(f"factors can only contain 2 items.")
    elif type(start) != int or type(end) != int:
        raise Exception(f"start and end must be int")
    elif end <= start:
        raise Exception(f"end must be greater than start.")

    for x in range(start, end + 1):
        if x % divisor1 == 0 and x % divisor2 == 0:
            result.append("Fizz Buzz")
        elif x % divisor1 == 0:
            result.append("Fizz")
        elif x % divisor2 == 0:
            result.append("Buzz")
        else:
            result.append(str(x))
    return result


print(fizz_buzz(1, 20, (3, 5)))
