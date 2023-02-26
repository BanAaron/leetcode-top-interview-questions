def fizz_buzz(number):
    for x in range(number):
        y = x + 1
        if y % 3 == 0 and y % 5 == 0:
            print(f"fizz buzz")
        elif y % 5 == 0:
            print(f"buzz")
        elif y % 3 == 0:
            print(f"fizz")
        else:
            print(x + 1)


fizz_buzz(100)
