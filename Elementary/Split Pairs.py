def split_pairs(a):
    result = []
    if len(a) % 2 == 1:
        a += '_'
    for i in range(0,len(a),2):
        result.append(a[i:i+2])
    return result

# def split_pairs(a):
#     if len(a) % 2 != 0:
#         a = a + "_"
#     return [a[i:i + 2] for i in range(0, len(a), 2)]



if __name__ == '__main__':

    assert list(split_pairs('abcd')) == ['ab', 'cd']
    assert list(split_pairs('abc')) == ['ab', 'c_']
    assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
    assert list(split_pairs('a')) == ['a_']
    assert list(split_pairs('')) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")


    # arr = list(a)
    # for i in range(len(arr)):
    #     if i % 2 == 0 and i != 0:
    #         result +=