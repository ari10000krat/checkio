# from timeit import timeit as t

def first_word(text):
    index = text.find(" ")
    return text[:index] if index != -1 else text


# print(t('first_word(x)', setup='x = "asdf we"*10', number=10000, globals=globals()))       #  ~11.7 ms
# print(t('first_word(x)', setup='x = "asdfawe"*10', number=10000, globals=globals()))       #  ~6.1 ms
# print(t('first_word(x)', setup='x = "asdf we"*100000', number=10000, globals=globals()))   #  ~90928.2 ms
# print(t('first_word(x)', setup='x = "asdfawe"*100000', number=10000, globals=globals()))   #  ~5562.9 ms

############################################################
# first_word = lambda txt: txt[:(txt+' ').index(' ')]


############################################################
# My Code
# def first_word(text: str) -> str:
#     """
#         returns the first word in a given text.
#     """
#     stringArr = text.split()
#     return stringArr[0]

if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello world"))

    assert first_word("Hello world") == "Hello"
    assert first_word("a word") == "a"
    assert first_word("hi") == "hi"
