def nearest_value(values: set, one: int) -> int:
    values = list(values)

    return None

def nearest_value(values: set, one: int) -> int:
    return min(values, key=lambda n: (abs(one - n), n))
def nearest_value(values: set, one: int) -> int:
    return sorted([(x, abs(one - x)) for x in values], key=lambda x: (x[1], x[0]))[0][0]


def nearest_value(values: set, one: int) -> int:
    # your code here
    if one in values: return one
    lowest_subt = ''
    temp = 0
    number_lowest = 0

    for number in sorted(list(values)):
        temp = abs(number - one)
        if lowest_subt == '':
            lowest_subt = temp
            number_lowest = number
        elif lowest_subt > temp:
            lowest_subt = temp
            number_lowest = number
    return number_lowest


def nearest_value(values: set, one: int) -> int:
    if one in values:
        return (one)

    else:
        values.add(one)
        values = sorted(list(values))
        if values.index(one) == 0:
            return (values[1])
        elif values.index(one) == len(values) - 1:
            return (values[(len(values) - 2)])
        else:
            if one - values[values.index(one) - 1] <= values[values.index(one) + 1] - one:
                return values[values.index(one) - 1]
            else:
                return values[values.index(one) + 1]
def nearest_value(values: set, one: int) -> int:
    solution = 999
    num = 0
    if values.issubset({one}):
        return one
    else:
        for i in values:
            if abs(one - i) < solution:
                solution = abs(one - i)
                num = i
            elif abs(one - i) == solution:
                solution = abs(one - i)
                if i > num:
                    pass
                else:
                    num = i
            else:
                pass
        return num



if __name__ == '__main__':
    nearest_value({4, 7, 10, 11, 12, 17}, 9)
    # print("Example:")
    # print(nearest_value({4, 7, 10, 11, 12, 17}, 9))
    #
    # # These "asserts" are used for self-checking and not for an auto-testing
    # assert nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
    # assert nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
    # assert nearest_value({4, 8, 10, 11, 12, 17}, 9) == 8
    # assert nearest_value({4, 9, 10, 11, 12, 17}, 9) == 9
    # assert nearest_value({4, 7, 10, 11, 12, 17}, 0) == 4
    # assert nearest_value({4, 7, 10, 11, 12, 17}, 100) == 17
    # assert nearest_value({5, 10, 8, 12, 89, 100}, 7) == 8
    # assert nearest_value({-1, 2, 3}, 0) == -1
    # print("Coding complete? Click 'Check' to earn cool rewards!")
