# def words_order(text: str, words: list) -> bool:
#     sen_word_list = text.split(" ")
#     j = 0
#     if text.find(words[0]) != 1:
#         for i in range(text.find(words[0])):
#             if sen_word_list[i] != words[j]:
#                 return False
#         return True
#     else:
#         return False

def words_order(text: str, words: list) -> bool: #TODO text str -> arr
    orderArr = []
    hello_word = {'hello': ['привет', 'хай']}
    for word in words:
        wordIndex = text.find(word)
        if wordIndex != -1 and wordIndex not in orderArr:
            orderArr.append(wordIndex)
    if orderArr == sorted(orderArr) and len(words) == len(orderArr):
        return True
    else:
        return False


if __name__ == '__main__':
    print("Example:")
    print(words_order('hi world im here', ['world', 'here']))
    print(words_order('hi world im here', ['here', 'world']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert words_order('hi world im here', ['world', 'here']) == True
    assert words_order('hi world im here', ['here', 'world']) == False
    assert words_order('hi world im here', ['world']) == True
    assert words_order('hi world im here',
                       ['world', 'here', 'hi']) == False
    assert words_order('hi world im here',
                       ['world', 'im', 'here']) == True
    assert words_order('hi world im here',
                       ['world', 'hi', 'here']) == False
    assert words_order('hi world im here', ['world', 'world']) == False
    assert words_order('hi world im here',
                       ['country', 'world']) == False
    assert words_order('hi world im here', ['wo', 'rld']) == False
    assert words_order('', ['world', 'here']) == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
