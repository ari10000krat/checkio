def is_all_upper(text: str) -> bool:
    text.replace(' ','')
    if text.upper() == text or not text.isalpha:
        return True
    return False

# def is_all_upper(text: str) -> bool:
#     # your code here
#     return text.upper() == text

if __name__ == '__main__':
    assert is_all_upper('123') == True
    assert is_all_upper('all lower') == False
    assert is_all_upper('mixed UPPER and lower') == False
    assert is_all_upper('') == True
    assert is_all_upper('     ') == True

    print("Coding complete? Click 'Check' to earn cool rewards!")
