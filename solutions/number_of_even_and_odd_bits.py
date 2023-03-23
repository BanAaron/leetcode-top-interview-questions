def even_odd_bit(n: int) -> list[int]:
    answer = [0, 0]
    for index, bit in enumerate(bin(n)[2:][::-1]):
        if index % 2 == 0 and bit == "1":
            answer[0] += 1
        elif index % 2 == 1 and bit == "1":
            answer[1] += 1

    return answer


if __name__ == "__main__":
    print(even_odd_bit(17))
    print(even_odd_bit(2))
    print(even_odd_bit(1605))