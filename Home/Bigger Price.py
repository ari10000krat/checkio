def bigger_price(limit: int, data: list) -> list:
    """
        TOP most expensive goods
    """
    result = []
    for i in range(limit):
        index = 0
        max = data[index]['price']
        for j in range(len(data)):
            if data[j]['price'] > max:
                index = j
                max = data[j]['price']
        result.append(data[index])
        data.pop(index)
    return result


# def bigger_price(limit: int, data: list) -> list:
#     """
#         TOP most expensive goods
#     """
#     # your code here
#
#     return sorted(data, key=lambda item: item.get("price"), reverse=True)[:limit]

if __name__ == '__main__':
    from pprint import pprint

    print('Example:')
    print(bigger_price(2, [
        {"name": "bread", "price": 10},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 25}
    ]))

    # These "asserts" using for self-checking and not for auto-testing
    assert bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]) == [
               {"name": "wine", "price": 138},
               {"name": "bread", "price": 100}
           ], "First"

    assert bigger_price(1, [
        {"name": "pen", "price": 5},
        {"name": "whiteboard", "price": 170}
    ]) == [{"name": "whiteboard", "price": 170}], "Second"

    print('Done! Looks like it is fine. Go and check it')
