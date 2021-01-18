def checkio(arr: list) -> int:
    """
        sums even-indexes elements and multiply at the last
    """
    sum = 0
    for i in range(0, len(arr), 2):
        sum += arr[i]
    return arr[-1] * sum if len(arr) > 0 else 0


# def checkio(array):
#     if not array:
#         return 0
#     return sum(array[::2]) * array[-1]
#
#
# def checkio(array: list) -> int:
#     """
#         sums even-indexes elements and multiply at the last
#     """
#     return sum(array[i] for i in range(len(array)) if i % 2 == 0) * array[-1] if array else 0



if __name__ == '__main__':
    print('Example:')
    print(checkio([0, 1, 2, 3, 4, 5]))

    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
