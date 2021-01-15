def is_acceptable_password(password: str) -> bool:
    return len(password)>6


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('short'))

    assert is_acceptable_password('short') == False
    assert is_acceptable_password('muchlonger') == True
    assert is_acceptable_password('ashort') == False


#is_acceptable_password = lambda password: len(password) > 6