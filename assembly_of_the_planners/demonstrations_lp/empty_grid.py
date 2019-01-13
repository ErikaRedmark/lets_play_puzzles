# Intended to be used with draw_solution.
# Takes a list of piece tuples normally intended for draw_solution,
# assumes a board that is for Assembly of the
# Planers, and returns a list containing the original piece tuples, plus
# one more that simply grays out all the other pieces, as well as address
# pitch black for the 'covered' parts to make the generated board look more
# visually understandable as being from the game.
# This is intended also for partial solutions, so the rest of the board can
# be shown even if not fully covered.

BOARD_LOCATIONS = [
                                            (0, 5), (0, 6),
                            (1, 3), (1, 4), (1, 5), (1, 6),
                    (2, 2), (2, 3), (2, 4), (2, 5), (2, 6),
            (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6),
            (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6),
    (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6),
    (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5),
    (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5),
            (8, 1), (8, 2), (8, 3), (8, 4), (8, 5),
            (9, 1), (9, 2), (9, 3), (9, 4), (9, 5),
                    (10, 2), (10, 3), (10, 4), (10, 5),
                             (11, 3), (11, 4), (11, 5),
                                               (12, 5)
]

GRAY_BOXES = ("wall", [(0, 4), (4, 0), (8, 0), (12, 4), (6, 6)])

# Expecting a single list, with multiple piece tuple, each piece tuple
# containing the piece name, and a list of 5 locations the piece is placed.
# the passed solution is not modified; new list returned
def invert_solution(solution):
    board_loc_copy = list(BOARD_LOCATIONS)
    for piece in solution:
        piece_locations = piece[1]
        for piece_loc in piece_locations:
            if piece_loc in board_loc_copy:
                board_loc_copy.remove(piece_loc)
    return solution + [(("empty", board_loc_copy))]


# Adds "pentomino" piece values for the gray boxes from the game. Intended
# ONLY for drawing.
# the passed solution is not modified; new list returned
def add_gray_boxes(solution):
    return solution + [GRAY_BOXES]


# identical to performing both invert_solution and add_gray_boxes
def pretty(solution):
    return add_gray_boxes(invert_solution(solution))
