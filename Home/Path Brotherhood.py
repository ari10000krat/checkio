def safe_pawns(pawns: set) -> int:
    countOfSafe = 0
    coordArr = [];
    for i in pawns:
        coordArr.append([ ord(i[0]), int(i[1])+1])

    for c in coordArr:
        if c[1] == 1 or \
                [c[0] - 1, c[1] - 1] in coordArr or \
                [c[0] + 1, c[1] - 1] in coordArr:
            countOfSafe += 1

    return countOfSafe


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    print(safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}))
    print(safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}))
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    assert safe_pawns(["a1", "b2", "c3", "d4", "e5", "f6", "g7", "h8"]) == 7
    assert safe_pawns(["a8", "b7", "c6", "d5", "e4", "f3", "g2", "h1"]) == 7

    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
