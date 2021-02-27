from pprint import pprint


def exclusive_elem(arr: list):
    """
        Returns exclusive elements in array
    """
    arr_result = []
    for x in arr:
        if x not in arr_result:
            arr_result.append(x)
    return arr_result


def sort_dict(d: dict):
    """
    sorts the dictionary by values reversed
    :return: Sorted dict
    """
    list_d = list(d.items())
    list_d.sort(key=lambda i: i[1], reverse=True)
    return dict(list_d)


def frequency_sort(arr: list):
    d = dict.fromkeys(exclusive_elem(arr), 0)
    res_arr = []
    for dijit in arr:
        d[dijit] += 1
    d = sort_dict(d)
    for i in d:
        for j in range(d[i]):
            res_arr.append(i)
    return res_arr


    # resArr = []
    # for i in range(len(arr)):
    #     if arr[i] not in resArr:
    #         for n in range(arr.count(arr[i])):
    #             resArr.append(arr[i])
    # return resArr
#
# def frequency_sort(items):
#     return sum(sorted([v for v in {i:[i]*items.count(i) for i in items}.values()], key=len, reverse=True), [])
#
# def frequency_sort(items):
#     lst = []
#     for x in items:
#         if x not in lst:
#             lst += [x] * items.count(x)
#     return sorted(lst, key=lambda x: lst.count(x), reverse=True)

if __name__ == '__main__':
    # print("Example:")
    print([4, 6, 2, 2, 2, 6, 4, 4, 4], 'WAS')
    print(frequency_sort([4, 6, 2, 2, 2, 6, 4, 4, 4]), 'my result')
    print([4, 4, 4, 4, 2, 2, 2, 6, 6], 'right result')
    print(frequency_sort([4, 6, 2, 2, 2, 6, 4, 4, 4])==[4, 4, 4, 4, 2, 2, 2, 6, 6])
    # # These "asserts" are used for self-checking and not for an auto-testing
    # assert list(frequency_sort([4, 6, 2, 2, 2, 6, 4, 4, 4])) == [
    #     4, 4, 4, 4, 2, 2, 2, 6, 6]
    # assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == [
    #     'bob', 'bob', 'bob', 'carl', 'alex']
    # assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    # assert list(frequency_sort([])) == []
    # assert list(frequency_sort([1])) == [1]
    # print("Coding complete? Click 'Check' to earn cool rewards!")
