def order(sentence: str) -> str:
    # create a list of numbers between 1-9
    numbers = [x for x in range(1, 10)]
    # remove any whitespace around the string and split on the remaining spaces
    sentence = sentence.strip().split(" ")
    # we will store out values in a dictionary and later return it in order
    storage = dict()

    for word in sentence:
        for number in numbers:
            # once the number in our string matches to the number in our list we store it in the storage dict
            if str(number) in word:
                storage[number] = word

    # we create a list comprehension out of our dictionary in sorted() order.
    # then simply join() the list together with a space for the final output
    return " ".join([value for key, value in sorted(storage.items(), key=lambda x: x[0])])


if __name__ == "__main__":
    print(order("is2 Thi1s T4est 3a"))
