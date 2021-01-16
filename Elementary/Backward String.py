def backward_string(val: str) -> str:
    val = list(val)
    for i in range(len(val)//2):
        val[i], val[len(val)-i-1] = val[len(val)-i-1], val[i]
    return ''.join(val)


# def backward_string(val: str) -> str:
#     return val[::-1]

if __name__ == '__main__':
    print("Example:")
    print(backward_string('abc'))
    print(backward_string('123'))


    assert backward_string('val') == 'lav'
    assert backward_string('') == ''
    assert backward_string('ohho') == 'ohho'
    assert backward_string('123456789') == '987654321'
