# Définition des mouvements possibles selon la direction courante et la commande
movement_functions = [
    {
        'F': lambda current_row, current_col, number_of_steps: (
            current_row,
            min(number_of_columns, current_col + number_of_steps)
        ),
        'B': lambda current_row, current_col, number_of_steps: (
            current_row,
            max(1, current_col - number_of_steps)
        )
    },
    {
        'F': lambda current_row, current_col, number_of_steps: (
            min(number_of_rows, current_row + number_of_steps),
            current_col
        ),
        'B': lambda current_row, current_col, number_of_steps: (
            max(1, current_row - number_of_steps),
            current_col
        )
    },
    {
        'F': lambda current_row, current_col, number_of_steps: (
            current_row,
            max(1, current_col - number_of_steps)
        ),
        'B': lambda current_row, current_col, number_of_steps: (
            current_row,
            min(number_of_columns, current_col + number_of_steps)
        )
    },
    {
        'F': lambda current_row, current_col, number_of_steps: (
            max(1, current_row - number_of_steps),
            current_col
        ),
        'B': lambda current_row, current_col, number_of_steps: (
            min(number_of_rows, current_row + number_of_steps),
            current_col
        )
    }
]

# Instruction pour tourner à droite ou gauche selon l'indice de direction courant
direction_change = {
    'R': lambda current_direction_index: (current_direction_index + 1) % 4,
    'L': lambda current_direction_index: (current_direction_index - 1) % 4
}

while True:

    number_of_rows, number_of_columns = map(int, input().split())

    if number_of_rows == 0:
        break

    current_row = 1
    current_col = 1
    current_direction_index = 0

    while True:

        command_input = input()
        command_type = command_input[0]

        if command_type in ['F', 'B']:
            number_of_steps = int(command_input.split()[1])
            current_row, current_col = movement_functions[current_direction_index][command_type](
                current_row,
                current_col,
                number_of_steps
            )

        elif command_type in ['R', 'L']:
            current_direction_index = direction_change[command_type](current_direction_index)

        else:
            print(current_row, current_col)
            break