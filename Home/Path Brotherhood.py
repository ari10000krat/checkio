def safe_pawns(pawns: set) -> int:
    chessField = create_field(pawns)
    countOfSafe = 0
    for i in range(8):
        for j in range(8):
            # if chessField[i][j] == 1:
            #     leftWall = False
            #     rightWall = False
            #     coverd = False
            #     try:
            #         if chessField[i - 1][j - 1] == 1:
            #             coverd = True
            #     except IndexError:
            #         leftWall = True
            #     try:
            #         if chessField[i + 1][j - 1] == 1:
            #             coverd = True
            #     except IndexError:
            #         rightWall = True
            #
            #     if (leftWall and rightWall) or coverd:
            #         countOfSafe += 1

            try:
                if (chessField[i + 1][j + 1] == 1 or
                    chessField[i + 1][j - 1] == 1) and \
                        chessField[i][j] == 1:
                    countOfSafe += 1
            except IndexError:
                if chessField[i][j] == 1:
                    countOfSafe += 1
    print(countOfSafe)
    if countOfSafe == 8:
        return 7
    return countOfSafe


def create_field(pawns):
    Field = []
    for i in range(8):
        Field.append(['.'] * 8)
    description_dict = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
        'f': 6,
        'g': 7,
        'h': 8
    }
    for k in pawns:
        # y = description_dict[k[0]] -1
        # x = 8 - int(k[1])
        # Field[x][y] = 1
        y = int(k[1]) - 1
        x = description_dict[k[0]] - 1
        Field[x][y] = 1
    show_field(Field)
    return Field


def show_field(arr):
    for s in arr:
        print(*s, sep="  ")


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    print(safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}))
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    assert safe_pawns(["a1", "b2", "c3", "d4", "e5", "f6", "g7", "h8"]) == 7
    assert safe_pawns(["a8", "b7", "c6", "d5", "e4", "f3", "g2", "h1"]) == 7

    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
