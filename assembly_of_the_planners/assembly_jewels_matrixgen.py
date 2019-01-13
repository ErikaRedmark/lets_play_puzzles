# Generates the incidence matrix needed for being solved by
# algorithm X.
# Assume a pentomino board of the following, using the trick of noticing that
# the entire left side can be solved indepedent of the right:
# |X|X|X|X|X|_|_|
# |X|X|X|_|_|_|_|
# |X|X|_|_|_|_|_|
# |X|_|_|_|_|_|_|
# |X|_|_|_|_|_|_|
# |_|_|_|_|_|_|_|
# |_|_|_|_|_|_|X|
# |_|_|_|_|_|_|X|
# |X|_|_|_|_|_|X|
# |X|_|_|_|_|_|X|
# |X|X|_|_|_|_|X|
# |X|X|X|_|_|_|X|
# |X|X|X|X|X|_|X|
#
import pprint
import itertools
from copy import deepcopy

# represents the 'legal' spaces of the above board. The extra padding is for
# ease of algorithm; translation stops at set points, and the extra 'no'
# spaces prevents index errors during computation.
LEGAL_SPACES = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# initial positions of pentominoes. For simplicity, each unique pentomino is
# given 4 versons of itself, starting at top of matrix in each rotation.
# One pentomio is completely duplicated, including reflection type, so the
# algorithm will simply add another duplicate set of rows for it.
f_std_0 = [(0, 1), (0, 2), (1, 0), (1, 1), (2, 1)]
f_std_1 = [(0, 1), (1, 0), (1, 1), (1, 2), (2, 2)]
f_std_2 = [(0, 1), (1, 1), (1, 2), (2, 0), (2, 1)]
f_std_3 = [(0, 0), (1, 0), (1, 1), (1, 2), (2, 1)]

f_ref_0 = [(0, 1), (1, 0), (1, 1), (2, 1), (2, 2)]
f_ref_1 = [(0, 1), (1, 0), (1, 1), (1, 2), (2, 0)]
f_ref_2 = [(0, 0), (0, 1), (1, 1), (1, 2), (2, 1)]
f_ref_3 = [(0, 2), (1, 0), (1, 1), (1, 2), (2, 1)]

p_0 = [(0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]
p_1 = [(0, 0), (0, 1), (1, 0), (1, 1), (1, 2)]
p_2 = [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0)]
p_3 = [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2)]
# only two unique rotations of z.
z_0 = [(0, 1), (0, 2), (1, 1), (2, 0), (2, 1)]
z_1 = [(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)]

v_0 = [(0, 0), (0, 1), (0, 2), (1, 0), (2, 0)]
v_1 = [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]
v_2 = [(0, 2), (1, 2), (2, 0), (2, 1), (2, 2)]
v_3 = [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]
# this piece is duplicated in output since there are 2 of it for puzzle.
n_std_0 = [(0, 0), (0, 1), (1, 1), (1, 2), (1, 3)]
n_std_1 = [(0, 1), (1, 0), (1, 1), (2, 0), (3, 0)]
n_std_2 = [(0, 0), (0, 1), (0, 2), (1, 2), (1, 3)]
n_std_3 = [(0, 1), (1, 1), (2, 0), (2, 1), (3, 0)]

n_ref_0 = [(0, 1), (0, 2), (0, 3), (1, 0), (1, 1)]
n_ref_1 = [(0, 0), (1, 0), (1, 1), (2, 1), (3, 1)]
n_ref_2 = [(0, 2), (0, 3), (1, 0), (1, 1), (1, 2)]
n_ref_3 = [(0, 0), (1, 0), (2, 0), (2, 1), (3, 1)]

l_0 = [(0, 0), (1, 0), (2, 0), (3, 0), (3, 1)]
l_1 = [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0)]
l_2 = [(0, 0), (0, 1), (1, 1), (2, 1), (3, 1)]
l_3 = [(0, 3), (1, 0), (1, 1), (1, 2), (1, 3)]

u_0 = [(0, 0), (0, 2), (1, 0), (1, 1), (1, 2)]
u_1 = [(0, 0), (0, 1), (1, 0), (2, 0), (2, 1)]
u_2 = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2)]
u_3 = [(0, 0), (0, 1), (1, 1), (2, 0), (2, 1)]

w_0 = [(0, 2), (1, 1), (1, 2), (2, 0), (2, 1)]
w_1 = [(0, 0), (1, 0), (1, 1), (2, 1), (2, 2)]
w_2 = [(0, 1), (0, 2), (1, 0), (1, 1), (2, 0)]
w_3 = [(0, 0), (0, 1), (1, 1), (1, 2), (2, 2)]

t_0 = [(0, 0), (0, 1), (0, 2), (1, 1), (2, 1)]
t_1 = [(0, 2), (1, 0), (1, 1), (1, 2), (2, 2)]
t_2 = [(0, 1), (1, 1), (2, 0), (2, 1), (2, 2)]
t_3 = [(0, 0), (1, 0), (1, 1), (1, 2), (2, 0)]

# collects all unique constraints into a sigle easily iterable list. Because
# the list is used in matrix gen the repeated pentomino is also repeated here.
ALL_PENTOMINOES = [
    f_std_0, f_std_1, f_std_2, f_std_3, f_ref_3, f_ref_2, f_ref_1, f_ref_0,
    p_0, p_1, p_2, p_3, z_0, z_1, v_0, v_1, v_2, v_3, n_std_0, n_std_1,
    n_std_2, n_std_3, n_ref_0, n_ref_1, n_ref_2, n_ref_3, l_0, l_1, l_2,
    l_3, u_0, u_1, u_2, u_3, w_0, w_1, w_2, w_3, t_0, t_1, t_2, t_3,
    n_std_0, n_std_1, n_std_2, n_std_3
]

# generates all moves for the legal board using the given pentomino. The
# returned list is a list of tuples for each place the pentomino can go.
def generate_all_moves(pent):
    # board is 7x13
    all_moves = []
    for i_translate in range(0, 14):
        for j_translate in range(0, 9):
            pent_copy = translate(pent, i_translate, j_translate)
            if (check_placement(pent_copy)):
                # the padding on the left and top sides with 0s means that
                # the actual board placement is offset.
                all_moves.append(translate(pent_copy, -1, -1))
    return all_moves

# translates the given pentomino the given amount.
def translate(pent, i, j):
    new_pent = []
    for coord in pent:
        new_pent.append((coord[0] + i, coord[1] + j))
    return new_pent

# checks if the pentomino can be placed, AND that it does not create
# fail areas; that is, areas of non-multiple of 5 sections that are completely
# segregated from the rest of the board.
def check_placement(pent):
    even_legal = (LEGAL_SPACES[pent[0][0]][pent[0][1]] == 1 and
        LEGAL_SPACES[pent[1][0]][pent[1][1]] == 1 and
        LEGAL_SPACES[pent[2][0]][pent[2][1]] == 1 and
        LEGAL_SPACES[pent[3][0]][pent[3][1]] == 1 and
        LEGAL_SPACES[pent[4][0]][pent[4][1]] == 1)

    if not even_legal:
        return False

    # 2D; using list constructor won't copy the lists within the lists.
    board = deepcopy(LEGAL_SPACES)

    for coord in pent:
        board[coord[0]][coord[1]] = 0

    # choose from one of two dummy locations
    i, j = (1, 6) if board[1][6] == 1 else (6, 6)
    searched_nodes = [(i, j)]
    search_remaining = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
    valid_count = 1
    while len(search_remaining) != 0:
        next_coord = search_remaining.pop()
        searched_nodes.append(next_coord)
        if (board[next_coord[0]][next_coord[1]] == 1):
            # print("Searched valid: {0}".format(next_coord))
            valid_count += 1
            expand_up = (next_coord[0] + 1, next_coord[1])
            expand_right = (next_coord[0], next_coord[1] + 1)
            expand_down = (next_coord[0] - 1, next_coord[1])
            expand_left = (next_coord[0], next_coord[1] - 1)
            if (board[expand_up[0]][expand_up[1]] == 1 and
                    expand_up not in searched_nodes and
                    expand_up not in search_remaining):
                search_remaining.append(expand_up)
            if (board[expand_right[0]][expand_right[1]] == 1 and
                    expand_right not in searched_nodes and
                    expand_right not in search_remaining):
                search_remaining.append(expand_right)
            if (board[expand_down[0]][expand_down[1]] == 1 and
                    expand_down not in searched_nodes and
                    expand_down not in search_remaining):
                search_remaining.append(expand_down)
            if (board[expand_left[0]][expand_left[1]] == 1 and
                    expand_left not in searched_nodes and
                    expand_left not in search_remaining):
                search_remaining.append(expand_left)

    #if (valid_count % 5 == 0):
    #    print(searched_nodes)
    return valid_count % 5 == 0


# For testing purposes, print out all of them to visually inspect
# coordinates to check for errors.
def print_pentomino(pent):
    for i in range(0, 4):
        print("     ", end="")
        for j in range(0, 4):
            if (i, j) in pent:
                print('#', end="")
            else:
                print('O', end="")
        print("")

# prints a list of lists such that each sublist is on a separate line.
def pretty_print(moves):
    for move in moves:
        print(move)

# Collect all moves (duplicate the ones for the n_std_0) and write out to
# file.
def create_moves_matrix():
    all_moves = []

    f_std_moves = []
    f_std_moves.append(generate_all_moves(f_std_0))
    f_std_moves.append(generate_all_moves(f_std_1))
    f_std_moves.append(generate_all_moves(f_std_2))
    f_std_moves.append(generate_all_moves(f_std_3))
    all_moves.append(('F_std',
        list(itertools.chain.from_iterable(f_std_moves))))

    f_ref_moves = []
    f_ref_moves.append(generate_all_moves(f_ref_0))
    f_ref_moves.append(generate_all_moves(f_ref_1))
    f_ref_moves.append(generate_all_moves(f_ref_2))
    f_ref_moves.append(generate_all_moves(f_ref_3))
    all_moves.append(('F_ref',
        list(itertools.chain.from_iterable(f_ref_moves))))

    p_moves = []
    p_moves.append(generate_all_moves(p_0))
    p_moves.append(generate_all_moves(p_1))
    p_moves.append(generate_all_moves(p_2))
    p_moves.append(generate_all_moves(p_3))
    all_moves.append(('P', list(itertools.chain.from_iterable(p_moves))))

    z_moves = []
    z_moves.append(generate_all_moves(z_0))
    z_moves.append(generate_all_moves(z_1))
    all_moves.append(('Z', list(itertools.chain.from_iterable(z_moves))))

    v_moves = []
    v_moves.append(generate_all_moves(v_0))
    v_moves.append(generate_all_moves(v_1))
    v_moves.append(generate_all_moves(v_2))
    v_moves.append(generate_all_moves(v_3))
    all_moves.append(('V', list(itertools.chain.from_iterable(v_moves))))

    n_std_moves = []
    n_std_moves.append(generate_all_moves(n_std_0))
    n_std_moves.append(generate_all_moves(n_std_1))
    n_std_moves.append(generate_all_moves(n_std_2))
    n_std_moves.append(generate_all_moves(n_std_3))
    # we have two pieces.
    all_moves.append(('N_std_1',
        list(itertools.chain.from_iterable(n_std_moves))))
    all_moves.append(('N_std_2',
        list(itertools.chain.from_iterable(n_std_moves))))

    n_ref_moves = []
    n_ref_moves.append(generate_all_moves(n_ref_0))
    n_ref_moves.append(generate_all_moves(n_ref_1))
    n_ref_moves.append(generate_all_moves(n_ref_2))
    n_ref_moves.append(generate_all_moves(n_ref_3))
    all_moves.append(('N_ref',
        list(itertools.chain.from_iterable(n_ref_moves))))

    l_moves = []
    l_moves.append(generate_all_moves(l_0))
    l_moves.append(generate_all_moves(l_1))
    l_moves.append(generate_all_moves(l_2))
    l_moves.append(generate_all_moves(l_3))
    all_moves.append(('L',
        list(itertools.chain.from_iterable(l_moves))))

    u_moves = []
    u_moves.append(generate_all_moves(u_0))
    u_moves.append(generate_all_moves(u_1))
    u_moves.append(generate_all_moves(u_2))
    u_moves.append(generate_all_moves(u_3))
    all_moves.append(('U', list(itertools.chain.from_iterable(u_moves))))

    w_moves = []
    w_moves.append(generate_all_moves(w_0))
    w_moves.append(generate_all_moves(w_1))
    w_moves.append(generate_all_moves(w_2))
    w_moves.append(generate_all_moves(w_3))
    all_moves.append(('W', list(itertools.chain.from_iterable(w_moves))))

    t_moves = []
    t_moves.append(generate_all_moves(t_0))
    t_moves.append(generate_all_moves(t_1))
    t_moves.append(generate_all_moves(t_2))
    t_moves.append(generate_all_moves(t_3))
    all_moves.append(('T', list(itertools.chain.from_iterable(t_moves))))

    return all_moves


def write_matrix(filename):
    data_printer = pprint.PrettyPrinter(indent=4)
    data = data_printer.pformat(create_moves_matrix())

    with open(filename, 'w') as file:
        file.write(data)


if (__name__ == "__main__"):
    write_matrix("incidence_matrix_assembly.json")
