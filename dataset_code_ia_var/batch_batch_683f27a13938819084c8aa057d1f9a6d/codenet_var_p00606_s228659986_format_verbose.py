while True:

    number_of_moves = int(input())

    if number_of_moves == 0:
        break

    start_cell, target_cell, forbidden_cell = input().split()

    ascii_base_for_cell = ord("A")
    forbidden_cell_index = ord(forbidden_cell) - ascii_base_for_cell

    transition_probability_matrix = [
        [0] * 9 for _ in range(number_of_moves + 1)
    ]

    transition_probability_matrix[0][ord(start_cell) - ascii_base_for_cell] = 1

    cell_neighbors = {
        0: (0, 0, 1, 3),
        1: (0, 1, 2, 4),
        2: (1, 2, 2, 5),
        3: (0, 3, 4, 6),
        4: (1, 3, 5, 7),
        5: (2, 4, 5, 8),
        6: (3, 6, 6, 7),
        7: (4, 6, 7, 8),
        8: (5, 7, 8, 8)
    }

    def apply_transition_update(current_cell, current_step):

        for next_cell in cell_neighbors[current_cell]:

            if next_cell == forbidden_cell_index:
                transition_probability_matrix[current_step][current_cell] += (
                    transition_probability_matrix[current_step - 1][current_cell] / 4
                )
            else:
                transition_probability_matrix[current_step][next_cell] += (
                    transition_probability_matrix[current_step - 1][current_cell] / 4
                )

    for move_number in range(1, number_of_moves + 1):

        for cell_index in range(9):

            apply_transition_update(cell_index, move_number)

    probability_reaching_target_cell = transition_probability_matrix[
        number_of_moves
    ][ord(target_cell) - ascii_base_for_cell]

    print(probability_reaching_target_cell)