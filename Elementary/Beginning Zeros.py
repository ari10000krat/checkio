def beginning_zeros(number: str) -> int:
    result = 0
    for i in range(len(number)):
        if number[i] == '0':
            result += 1
        else:
            break
    return result

# def beginning_zeros(number: str) -> int:
#     # your code her
#     zero = len(number)-len(number.lstrip('0'))
#     return zero
#
# def beginning_zeros(number: str) -> int:
#     return reduce(lambda a,_: a + 1, takewhile(lambda x: x == '0', number), 0)



if __name__ == '__main__':
    print("Example:")
    print(beginning_zeros('100'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert beginning_zeros('100') == 0
    assert beginning_zeros('001') == 2
    assert beginning_zeros('100100') == 0
    assert beginning_zeros('001001') == 2
    assert beginning_zeros('012345679') == 1
    print(beginning_zeros('0000'))
    assert beginning_zeros('0000') == 4
    print("Coding complete? Click 'Check' to earn cool rewards!")
