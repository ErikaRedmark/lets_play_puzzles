# Use %paste in IPython. Use invert_solution and add_gray_boxes in empty_grid.py
# for nicer output. Make sure to wrap everything in a list of lists for
# draw_solution.

# ------------ DEMONSTRATION ONE
# Fast hueristics to determine you're on your way to no solution

# Ready to place a 'P' block into the slot
demonstration_1_1 = [
("L", [(0, 5), (0, 6), (1, 6), (2, 6), (3, 6)]),
("V", [(1, 3), (1, 4), (1, 5), (2, 5), (3, 5)]),
("F_std", [(2, 2), (2, 3), (3, 1), (3, 2), (4, 2)])
]

# Show that the only piece that could fill the area to the right is another P block
demonstration_1_2 = [
("L", [(0, 5), (0, 6), (1, 6), (2, 6), (3, 6)]),
("V", [(1, 3), (1, 4), (1, 5), (2, 5), (3, 5)]),
("F_std", [(2, 2), (2, 3), (3, 1), (3, 2), (4, 2)]),
("P", [(2, 4), (3, 3), (3, 4), (4, 3), (4, 4)])
]

# colouring in the single block
demonstration_1_3 = [
("L", [(0, 5), (0, 6), (1, 6), (2, 6), (3, 6)]),
("V", [(1, 3), (1, 4), (1, 5), (2, 5), (3, 5)]),
("F_std", [(2, 2), (2, 3), (3, 1), (3, 2), (4, 2)]),
("P", [(2, 4), (3, 3), (3, 4), (4, 3), (4, 4)]),
("W", [(5, 5)])
]

demonstration_1_3 = empty_grid.pretty(demonstration_1_3)
draw_solution.draw_solution([demonstration_1_3], "demo1_3.svg", size=35)

# colouring in the four blocks

demonstration_1_4 = [
("L", [(0, 5), (0, 6), (1, 6), (2, 6), (3, 6)]),
("V", [(1, 3), (1, 4), (1, 5), (2, 5), (3, 5)]),
("F_std", [(2, 2), (2, 3), (3, 1), (3, 2), (4, 2)]),
("P", [(2, 4), (3, 3), (3, 4), (4, 3), (4, 4)]),
("W", [(5, 5), (5, 6), (4, 5), (4, 6)])
]

demonstration_1_4 = empty_grid.pretty(demonstration_1_4)
draw_solution.draw_solution([demonstration_1_4], "demo1_4.svg", size=35)

# colouring in two different places for the P to go
demonstration_1_5 = [
("L", [(0, 5), (0, 6), (1, 6), (2, 6), (3, 6)]),
("V", [(1, 3), (1, 4), (1, 5), (2, 5), (3, 5)]),
("F_std", [(2, 2), (2, 3), (3, 1), (3, 2), (4, 2)]),
("P", [(2, 4), (3, 3), (3, 4), (4, 3), (4, 4)]),
("W", [(5, 5), (5, 6), (4, 5), (4, 6)]),
("F_ref", [(5, 4), (6, 5)])
]

demonstration_1_5 = empty_grid.pretty(demonstration_1_5)
draw_solution.draw_solution([demonstration_1_5], "demo1_5.svg", size=35)

# -------------- DEMONSTRATION TWO
# The rotation. Just builds an empty thing with a single piece to show how the rotation will work.
demonstration_2_1 = [
("W", [(2, 4), (3, 3), (3, 4), (4, 2), (4, 3)])
]

demonstration_2_1 = empty_grid.pretty(demonstration_2_1)
draw_solution.draw_solution([demonstration_2_1], "demo2_1.svg", size=35)

# A completely empty board
demonstration_2_2 = []

demonstration_2_2 = empty_grid.pretty(demonstration_2_2)
draw_solution.draw_solution([demonstration_2_2], "demo2_2.svg", size=35)

# --------------- DEMONSTRATION THREE
# If we end up splitting the board into two unconnected subsections, we MUST
# make sure that at least one subsection is a multiple of 5. We only need to
# check one, because if it is, and since the pieces already covered must be
# a multiple of 5, then the other section MUST be a multiple of 5 because...
# ... math. A multiple of 5 (in this case 60) minus a multiple of 5
# (the pieces covering right now) minus another multiple of 5 (the size of
# the section we calculated) will be a multiple of 5, the remainder over there
demonstration_3_1 = [
("V", [(5, 0), (5, 1), (5, 2), (6, 0), (7, 0)]),
("F_ref", [(5, 3), (5, 4), (6, 4), (6, 5), (7, 4)]),
]

demonstration_3_1 = empty_grid.pretty(demonstration_3_1)
draw_solution.draw_solution([demonstration_3_1], "demo3_1.svg", size=35)

# Here, the split does not result in two sides with multiples of 5.
demonstration_3_2 = [
("N_ref", [(6, 1), (6, 2), (6, 3), (7, 1), (7, 0)]),
("F_ref", [(5, 3), (5, 4), (6, 4), (6, 5), (7, 4)]),
]

demonstration_3_2 = empty_grid.pretty(demonstration_3_2)
draw_solution.draw_solution([demonstration_3_2], "demo3_2.svg", size=35)

# --------------- DEMONSTRATION FOUR
# When almost done, take the most annoying piece and try and fit it somewhere.
# Hey, if there is a solution it's gotta go SOMEWHERE. Then take a look and
# see if you can fit the remaining pieces around it.
demonstration_4_1 = [
("F_std", [(10, 4), (11, 3), (11, 4), (11, 5), (12, 5)]),
("U", [(9, 3), (9, 4), (9, 5), (10, 3), (10, 5)]),
("N_ref", [(7, 1), (8, 1), (9, 1), (9, 2), (10, 2)]),
("V", [(5, 0), (5, 1), (5, 2), (6, 0), (7, 0)]),
("P", [(6, 1), (6, 2), (6, 3), (7, 2), (7, 3)]),
("L", [(8, 2), (8, 3), (8, 4), (8, 5), (7, 5)]),
("F_ref", [(5, 3), (5, 4), (6, 4), (6, 5), (7, 4)]),
("Z", [(1, 3), (2, 3), (2, 4), (2, 5), (3, 5)]),
# out of play
("N_std_1", [(0, 8), (1, 8), (2, 8), (2, 7), (3, 7)]),
("W", [(3, 9), (3, 8), (4, 8), (4, 7), (5, 7)]),
("T", [(5, 9), (6, 9), (7, 9), (7, 8), (7, 10)]),
("N_std_2", [(9, 9), (10, 9), (11, 9), (11, 8), (12, 8)])
]

demonstration_4_1 = empty_grid.pretty(demonstration_4_1)
draw_solution.draw_solution([demonstration_4_1], "demo4_1.svg", size=35)
# End
