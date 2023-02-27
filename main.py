def fizz_buzz(start: int = 1, end: int = 100, divisors: tuple = (3, 5)) -> list:
    """
    a function that returns the answer to the fizz buzz game
    :param start: start counting from here
    :param end: stop count here
    :param divisors: the numbers to divide against
    :return: List of strings
    """
    divisors_len = len(divisors)
    divisor0 = False
    divisor1 = False
    result = []

    if divisors_len != 2:
        raise Exception(
            f"factors length is {divisors_len}. factors must be a length of 2."
        )
    if end <= start:
        raise Exception(f"end must be greater than start. start.")
    else:
        for x in range(start, end + 1):
            for y, divisor in enumerate(divisors):
                if x % divisor == 0 and y == 0:
                    divisor0 = True
                if x % divisor == 0 and y == 1:
                    divisor1 = True
            if divisor0 and divisor1:
                result.append("Fizz Buzz")
            elif divisor0:
                result.append("Fizz")
            elif divisor1:
                result.append("Buzz")
            else:
                result.append(str(x))
            # finally
            divisor0 = False
            divisor1 = False

    return result


print(fizz_buzz())
