def parse_words(text: str) -> list:
    """
    Parse text
    :return: arr with reversed words
    """
    words_arr = text.split()
    for i in range(len(words_arr)):
        words_arr[i] = words_arr[i][::-1]
    return words_arr


def parse_separators(text: str) -> list:
    """
    Parse text
    :return: arr with separators between words
    """
    separators_arr = []
    separator_str = ''
    for char in text:
        if char.isspace():
            separator_str += char
        elif len(separator_str) > 0:
            separators_arr.append(separator_str)
            separator_str = ''
    return separators_arr


def combine_string(words_arr, separators_arr, text) -> str:
    """
    Join arr of words and separators to create a string
    :return:
    """
    result_str = ''
    words_index = 0
    sep_index = 0
    while len(result_str) < len(text):
        try:
            result_str += words_arr[words_index]
            words_index += 1

            result_str += separators_arr[sep_index]
            sep_index += 1
        except:
            break
    return result_str


def backward_string_by_word(text: str) -> str:
    words_arr = parse_words(text)
    separators_arr = parse_separators(text)
    result_str = combine_string(words_arr,separators_arr,text)

    return result_str

def backward_string_by_word(text: str) -> str:
    return ' '.join([x[::-1] for x in text.split(' ')])


if __name__ == '__main__':
    assert backward_string_by_word('hello world') == 'olleh dlrow'
    print("Example:")
    print(backward_string_by_word(''))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string_by_word('') == ''
    assert backward_string_by_word('world') == 'dlrow'
    assert backward_string_by_word('hello world') == 'olleh dlrow'
    assert backward_string_by_word('hello   world') == 'olleh   dlrow'
    assert backward_string_by_word('welcome to a game') == 'emoclew ot a emag'
    print("Coding complete? Click 'Check' to earn cool rewards!")
