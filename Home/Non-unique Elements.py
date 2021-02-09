
\

from collections import Counter
from operator import itemgetter

def checkio(data: list) -> list:
    x = Counter(data).most_common()

    if list(dict.fromkeys(data)) == data:
        return []

    if min(x, key=itemgetter(1)) == max(x, key=itemgetter(1)):
        return data

    for key, value in x:
        if value == 1:
            data.remove(key)

    return data

def checkio(data: list) -> list:
    # Your code here
    # It's main function. Don't remove this function
    # It's used for auto-testing and must return a result for check.
    return list(map(lambda i: data[i],
                    filter(lambda x: data[x] in data[x + 1::] or data[x] in data[0:x], range(len(data)))))

def checkio(data: list) -> list:
    return [dijit for dijit in data if data.count(dijit) != 1]


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
    print("It is all good. Let's check it now")
