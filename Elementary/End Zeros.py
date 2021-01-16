def end_zeros(num: int) -> int:
    return len(str(num)) - len(str(num).rstrip('0'))

# def end_zeros(number):
#     if not number:
#        return 1
#     if not number % 10:
#        return 1 + end_zeros(number // 10)
#     return 0


# def end_zeros(number):
#     result = not number
#     while number and not number % 10:
#         number /= 10
#         result += 1
#     return result


if __name__ == '__main__':
    print("Example:")
    print(end_zeros(0))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert end_zeros(0) == 1
    assert end_zeros(1) == 0
    assert end_zeros(10) == 1
    assert end_zeros(101) == 0
    assert end_zeros(245) == 0
    assert end_zeros(100100) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")
