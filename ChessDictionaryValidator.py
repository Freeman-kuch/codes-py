#!  Python 3
# chess Dictionary Validator

def isValidChessBoard(board):
    #  Define the set of all chess  pieces
    colors = ['w', 'b']  # defines the two side of the board
    pieces = ['king', 'queen', 'knight', 'bishop', 'rook', 'pawn']  # defines all the names of possible pieces on the board
    all_pieces = list(color + piece for piece in pieces for color in colors)  # the syntax/ data type is to take not of!
    #  print(all_pieces)

    #  Define the valid count range  of pieces by type (low, high) tuples
    valid_counts = {'king': (1, 1),
                    'queen': (0, 1),
                    'rook': (0, 2),
                    'bishop': (0, 2),
                    'knight': (0, 2),
                    'pawn': (0, 8)}

    #  Count the pieces on the board
    piece_count = {}
    for v in board.values():  # this counts all the values in the board input
        if v in all_pieces:  # this checks if the values are in the defined variable 'all_pieces'
            piece_count.setdefault(v, 0)  # this sets the value to 0 on the first instance
            piece_count[v] += 1  # this then adds 1 to the value count

    #  Check pieces counts in a valid range
    for piece in all_pieces:
        count = piece_count.get(piece, 0)
        lo, hi = valid_counts[piece[1:]]  # this defines the low and high for each piece
        if not lo <= count <= hi:  # Count needs to be between lo and hi
            if lo != hi:
                print(f"There should between {lo} and {hi} {piece} but there are {count}")
            else:
                print(f"There should be {lo} {piece} but there are {count})")
            return False

    #  Check that positions are valid
    for location in board.keys():  # this iterates over all the keys(location on the chess board) in the board dictionary
        row = int(location[:1])  # defines row as the alphabet part of the key
        column = location[1:]  # defines column as the numeric part of the key
        if not ((1 <= row <= 8) and ('a' <= column <= "h")):  # checks if its within range of 1-8 and a-h
            print(f"Invalid to have {board[location]} at position {location}")
            return False

    #  Check that pieces names are valid
    for loc, piece in board.items():  # iterates over all the keys: values in the board dictionary
        if piece:  # if the value isn't among all_pieces variable
            if piece not in all_pieces:  # checks if the piece is not in a valid spot
                print(f"{piece} is not a valid chess piece at position {loc}")
                return False

    return True


board = {'1a': 'bking', '2a': 'bqueen', '3a': 'brook', '4a': 'brook',
         '5a': 'bknight', '6a': 'bknight', '7a': 'bbishop', '8a': 'bbishop',
         '1b': 'bpawn', '2b': 'bpawn', '3b': 'bpawn', '4b': 'bpawn',
         '5b': 'bpawn', '6b': 'bpawn', '7b': 'bpawn', '8b': 'bpawn',
         '1c': 'wking', '2c': 'wqueen', '3c': 'wrook', '4c': 'wrook',
         '5c': 'wbishop', '6c': 'wbishop', '7c': 'wknight', '8c': 'wknight',
         '1e': 'wpawn', '2e': 'wpawn', '3e': 'wpawn', '4e': 'wpawn',
         '5e': 'wpawn', '6e': 'wpawn', '7e': 'wpawn', '8e': 'wpawn',
         '1f': '', '2f': '', '3f': '', '4f': '', '5f': '', '6f': '', '7f': '', '8f': '',
         '1g': '', '2g': '', '3g': '', '4g': '', '5g': '', '6g': '', '7g': '', '8g': '',
         '1h': '', '2h': '', '3h': '', '4h': '', '5h': '', '6h': '', '7h': '', '8h': '', }

print(isValidChessBoard(board))
