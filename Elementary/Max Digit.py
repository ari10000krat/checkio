def max_digit(number: int) -> int:
    max_dijit = 0
    while number >= 1:
        guess = number % 10
        number //= 10
        if guess > max_dijit:
            max_dijit = guess

    return max_dijit

# def max_digit(number: int) -> int:
#     return max([int(d) for d in str(number)])

if __name__ == '__main__':
    assert max_digit(52) == 5
    assert max_digit(0) == 0
    assert max_digit(634) == 6
    assert max_digit(1) == 1
    assert max_digit(10000) == 1
    print("Coding complete? Click 'Check' to earn cool rewards!")
