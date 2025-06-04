# Dictionnaire qui mappe chaque lettre à une position (ligne, colonne) sur une grille 3x3
grid_position_mapping = {
    "A": (0, 0), "B": (0, 1), "C": (0, 2),
    "D": (1, 0), "E": (1, 1), "F": (1, 2),
    "G": (2, 0), "H": (2, 1), "I": (2, 2)
}

while True:

    user_input_iterations = input()
    
    if user_input_iterations == 0:
        break

    # Initialisation du tableau dynamique 3D (pas, ligne, colonne)
    number_of_steps = user_input_iterations
    probability_table = [
        [
            [0] * 3 for _ in range(3)
        ]
        for _ in range(number_of_steps + 1)
    ]

    start_label, target_label, blocked_label = raw_input().split()

    start_row, start_col = grid_position_mapping[start_label]
    target_row, target_col = grid_position_mapping[target_label]
    blocked_row, blocked_col = grid_position_mapping[blocked_label]

    # Position de départ
    probability_table[0][start_row][start_col] = 1

    for current_step in range(number_of_steps):
        for current_row in range(3):
            for current_col in range(3):
                possible_directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
                for delta_row, delta_col in possible_directions:
                    next_row = current_row + delta_row
                    next_col = current_col + delta_col

                    blocked_position = (blocked_row, blocked_col)
                    next_position = (next_row, next_col)

                    # Si la position suivante est hors de la grille ou bloquée
                    if not (0 <= next_row < 3 and 0 <= next_col < 3) or next_position == blocked_position:
                        probability_table[current_step + 1][current_row][current_col] += probability_table[current_step][current_row][current_col]
                    else:
                        probability_table[current_step + 1][next_row][next_col] += probability_table[current_step][current_row][current_col]

    number_of_paths = probability_table[number_of_steps][target_row][target_col]
    total_number_of_possible_paths = 4.0 ** number_of_steps
    probability = float(number_of_paths) / total_number_of_possible_paths

    print("{:.8f}".format(probability))