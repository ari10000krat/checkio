from typing import List, Any


# def all_the_same(elements: List[Any]) -> bool:
#     if elements:
#         for k in elements:
#             if k == elements[0]:
#                 continue
#             else:
#                 return False
#         return False
#     else:
#         return True

def all_the_same(elements: List[Any]) -> bool:
    for k in elements:
        if k != elements[0]:
            return False
    return True

if __name__ == '__main__':
    print("Example:")
    print(all_the_same([1, 1, 1]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert all_the_same([1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False
    assert all_the_same(['a', 'a', 'a']) == True
    assert all_the_same([]) == True
    assert all_the_same([1]) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
