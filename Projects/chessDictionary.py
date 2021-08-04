# Chess Dictionary Validator

goodBoard = {'3e':'wking', '1h':'bking'}

badBoardPosition = {'3m':'wking', '1h':'bking'}

badBoardNumberPawns = {'3e': 'wking', '1h': 'bking', '3a': 'wpawn','3b': 'wpawn',
                        '3c': 'wpawn','3d': 'wpawn','4e': 'wpawn','3f': 'wpawn',
                        '3g': 'wpawn','3h': 'wpawn','4a': 'wpawn'}

badBoardNumberPieces = {'3e':'wking', '1h':'bking', '3a':'wpawn','3b':'wpawn',
                        '3c':'wpawn','3d':'wpawn','4e':'wpawn','3f':'wpawn',
                        '3g':'wpawn','3h':'wpawn','4a':'wrook', '4d':'wrook',
                        '4f':'wrook','5a':'wqueen','5b':'wqueen','5c':'wqueen',
                        '5d':'wqueen','5e':'wqueen','5f':'wqueen','5g':'wqueen'}

# Main program
def isValidChessBoard(board):

    # Variables
    pieces = ('wking','wqueen','wrook','wknight','wbishop','wpawn',
              'bking','bqueen','brook','bknight','bbishop','bpawn')
    location = ('a','b','c','d','e','f','g','h')
    wKing = 0
    bKing = 0
    wPieces = 0
    bPieces = 0
    wPawns = 0
    bPawns = 0

    # Check for only one king of each color.
    for v in board.values():
        if v == 'wking':
            wKing += 1
        if v == 'bking':
            bKing += 1
    if wKing != 1:
            print('Error: Need only 1 white king.')
            return False
    if bKing != 1:
            print('Error: Need only 1 black king.')
            return False

    # Check for only 16 pieces max on each color.
    for k in board.values():
        if k[0] == 'w':
            wPieces += 1
        if wPieces >= 16:
            print('Too many white pieces.')
            return False
        if k[0] == 'b':
            bPieces += 1
        if bPieces >= 16:
            print('Too many black pieces.')
            return False

    # Check for only 8 pawns max on each color.
    for v in board.values():
        if v == 'wpawn':
            wPawns += 1
        if wPawns >= 9:
            print('Too many white pawns.')
            return False
        if v == 'bpawn':
            bPawns += 1
        if bPawns >= 9:
            print('Too many black pawns.')
            return False

    # Check for only valid spaces.
    for k in board.keys():
        if int(k[0]) >= 9:
            print('Invalid piece location')
            return False
        if k[1] not in location:
            print('Invalid piece location')
            return False

    # If nothing is False, then board checks out.
    if True:
        print('This is a valid chess board.')

print(isValidChessBoard(badBoardNumberPieces))
