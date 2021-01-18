def count_digits(text: str) -> int:
    result = 0
    for char in text:
        if char.isdigit():
            result += 1

    return result

# def count_digits(text: str) -> int:
#     return sum(c.isdigit() for c in text)
#
# def count_digits(text: str) -> int:
#     return sum(1 for _ in (filter(str.isdigit, text)))



if __name__ == '__main__':
    print("Example:")
    print(count_digits('hi'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert count_digits('hi') == 0
    assert count_digits('who is 1st here') == 1
    assert count_digits('my numbers is 2') == 1
    assert count_digits('This picture is an oil on canvas '
                        'painting by Danish artist Anna '
                        'Petersen between 1845 and 1910 year') == 8
    assert count_digits('5 plus 6 is') == 2
    assert count_digits('') == 0
