import re

def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    result = ''
    status = False  # Status: WE FIND THE WORD!
    for char in text:
        if char.isalpha() or char == "'":
            status = True
            result += char
        elif status:
            return result
    return result


# def first_word(text: str) -> str:
#     regex = re.compile(r"\w+'?\w*")
#     words = regex.findall(text)
#     return words[0]
#
#
# def first_word(text: str) -> str:
#     """
#         returns the first word in a given text.
#     """
#     # your code here
#     return text.replace('.',' ').replace(',',' ').split()[0]




if __name__ == '__main__':
    assert first_word("greetings, friends") == "greetings"

    print("Example:")
    print(first_word("Hello world"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    assert first_word("Hello.World") == "Hello"
    print("Coding complete? Click 'Check' to earn cool rewards!")
