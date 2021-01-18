def sum_numbers(text: str) -> int:
    arr = text.split()
    result = 0
    for guess in arr:
        try:
            num = int(guess)
            result += num
        except ValueError:
            pass
    return result

# def sum_numbers(text: str) -> int:
#     text_list = text.split()
#     summ = 0
#     for item in text_list:
#         if item.isdigit():
#             summ += int(item)
#     return summ
#
# def sum_numbers(text: str) -> int:
#     # your code here
#     return sum([int(i) for i in text.split() if i.isdigit()])


if __name__ == '__main__':
    print("Example:")
    print(sum_numbers('hi'))

    assert sum_numbers('hi') == 0
    assert sum_numbers('who is 1st here') == 0
    assert sum_numbers('my numbers is 2') == 2
    assert sum_numbers('This picture is an oil on canvas '
                       'painting by Danish artist Anna '
                       'Petersen between 1845 and 1910 year') == 3755
    assert sum_numbers('5 plus 6 is') == 11
    assert sum_numbers('') == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")
