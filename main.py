def fizz_buzz(start: int = 1, end: int = 100, factors: tuple = (3, 5)):
    factors_len = len(factors)
    factor0 = False
    factor1 = False
    result = []

    if factors_len != 2:
        raise Exception(
            f"factors length is {factors_len}. factors must be a length of 2."
        )
    if end <= start:
        raise Exception(f"end must be greater than start. start.")
    else:
        for x in range(start, end + 1):
            for y, factor in enumerate(factors):
                if x % factor == 0 and y == 0:
                    factor0 = True
                if x % factor == 0 and y == 1:
                    factor1 = True
            if factor0 and factor1:
                result.append("Fizz Buzz")
            elif factor0:
                result.append("Fizz")
            elif factor1:
                result.append("Buzz")
            else:
                result.append(str(x))
            # finally
            factor0 = False
            factor1 = False

    return result


fizz_buzz()
