import random

SOLVE_ORDER = [0, 9, 16, 17, 15, 19, 18, 4, 10,
    8, 14, 1, 2, 3, 5, 11, 7, 13, 6, 12]

# minor optimisation: No need to validate a step of solving if that step
# placed a tile that is in a 'guess' position and didn't generate a full
# value somewhere that needs verification.
VALIDATE_BOARD_FOR_STEP = [True, False, True, True, False, True, True,
    False, True, False, True, False, False, True, False, True, False,
    True, True, True]

# index refers to numerical value of tile. Array value refers to how many left
tiles = [2] * 10
# drawing of board in validate functions
board = ["."] * 20

backtracking_cnt = 0

def solve_board(board, tiles, step):
    """Recursive function that solves the next step of the board. Each
    step of the board will try to place a tile into one particular place, which
    will either solve one row/column to a multiple of 7, or end up just being
    a guess. When the piece is placed, this function is called again for the
    next step. If a total solution is found (which will happen at step 19)
    this function returns with the board state changed."""
    # boolean return is just for early stopping of recursion once the
    # first solution is found.
    current_space = SOLVE_ORDER[step]

    for i in randomly(range(0, 10)):
    # for i in range(0, 10):
        # sanity check: we can't place a tile if we used them all up
        if (tiles[i] == 0):
            continue

        board[current_space] = i
        # validation is skipped for certain spaces.
        if (VALIDATE_BOARD_FOR_STEP[step] and not (is_valid_board(board))):
            board[current_space] = "."
            continue

        if (step == 19):
            # at the moment, just find first solution
            return True
        else:
            tiles[i] -= 1
            # hit the recursion here. The tile is valid and placed, and we
            # are not at a solution yet. Place the next one.

            # pretty_print(board)

            if (solve_board(board, tiles, step + 1)):
                return True
            # print("Backtracking...")
            global backtracking_cnt
            backtracking_cnt += 1
            # we returned from the solution branches, if any, from the previous
            # call. If we hit here, it means a backtrack. The tile is now
            # available again, so add it back
            tiles[i] += 1

        # moving out of method means a backtrack, so we undo the move we did.
        board[current_space] = "."

    return False

# TODO (Optimisation) possibly call is_valid_row for the known rows created for
# each solution step to minimize checking?
def is_valid_board(board):
    # there are 13 row/column combinations that all must have a number
    # divisible by seven. These checks are hardcoded and represent a board
    # of the following form where numbers are read from left-right and
    # top-bottom:
    #            | 0|
    #         | 1| 2| 3|
    #      | 4| 5| 6| 7| 8|
    #   | 9|10|11|12|13|14|15|
    #   |16|17|        |18|19|
    return (is_valid_row(0, 0, 0, 0, 0, 0, board[0]) and
        is_valid_row(0, 0, 0, 0, board[1], board[2], board[3]) and
        is_valid_row(0, 0, board[4], board[5], board[6],
            board[7], board[8]) and
        is_valid_row(board[9], board[10], board[11], board[12], board[13],
            board[14], board[15]) and
        is_valid_row(0, 0, 0, 0, 0, board[16], board[17]) and
        is_valid_row(0, 0, 0, 0, 0, board[18], board[19]) and
        # columns
        is_valid_row(0, 0, 0, 0, 0, board[9], board[16]) and
        is_valid_row(0, 0, 0, 0, 0, board[15], board[19]) and
        is_valid_row(0, 0, 0, 0, board[4], board[10], board[17]) and
        is_valid_row(0, 0, 0, 0, board[8], board[14], board[18]) and
        is_valid_row(0, 0, 0, 0, board[1], board[5], board[11]) and
        is_valid_row(0, 0, 0, 0, board[3], board[7], board[13]) and
        is_valid_row(0, 0, 0, board[0], board[2], board[6], board[12]))


def randomly(seq):
    """Iterator for random iteration over a sequence"""
    shuffled = list(seq)
    random.shuffle(shuffled)
    return iter(shuffled)

def is_valid_row(mil, hund_thousands, ten_thousands, thousands, hundreds,
        tens, ones):
    """Checks the validity of a number as divisible by 7 with each digit
    passed in according to it's place in the board. For example, the
    column for board locations 9 and 16 are passed with 9 in the tens place
    and 16 in the ones place. If any of the 'places' are ".", that represents
    no value yet, or an incomplete number. Those are considered 'valid' for
    the time being."""
    if (mil == "." or hund_thousands == "." or ten_thousands == "." or
            thousands == "." or hundreds == "." or tens == "." or ones == "."):
        return True

    number = (1000000 * mil +
              100000 * hund_thousands +
              10000 * ten_thousands +
              1000 * thousands +
              100 * hundreds +
              10 * tens +
              ones)

    return number % 7 == 0

def pretty_print(board):
    print("""
           |{0}|
         |{1}|{2}|{3}|
       |{4}|{5}|{6}|{7}|{8}|
     |{9}|{10}|{11}|{12}|{13}|{14}|{15}|
     |{16}|{17}|     |{18}|{19}|""".
   format(board[0], board[1], board[2], board[3], board[4], board[5], board[6],
        board[7], board[8], board[9], board[10], board[11], board[12],
        board[13], board[14], board[15], board[16], board[17], board[18],
        board[19]))

# Main Script

# first tile is obvious. We choose 0 over 7, because a clever human
# could consider 0 as limiting the number of digits they need to think
# about for the middle column value.
board[0] = 0

solve_board(board, tiles, 1)
pretty_print(board)
print("Number of backtrackings required: {0}".format(backtracking_cnt))
