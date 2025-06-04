import math

user_input_string = raw_input()

memory_cells_ascii_values = [ascii_value for ascii_value in range(30, 121, 10)]

brainfuck_code_output = ''

# Initialize memory cells with required ASCII values
for ascii_value in range(30, 121, 10):
    brainfuck_code_output += ('+' * ascii_value) + '>'

# Move data pointer back to the start
brainfuck_code_output += '<' * 10

current_cell_index = 0

for character in user_input_string:
    target_ascii_value = ord(character)
    target_cell_index = (target_ascii_value // 10) - 3

    cell_movement_distance = int(math.fabs(current_cell_index - target_cell_index))

    if current_cell_index < target_cell_index:
        brainfuck_code_output += '>' * cell_movement_distance
    else:
        brainfuck_code_output += '<' * cell_movement_distance

    current_cell_index = target_cell_index

    value_adjustment_distance = int(math.fabs(memory_cells_ascii_values[current_cell_index] - target_ascii_value))

    if memory_cells_ascii_values[current_cell_index] < target_ascii_value:
        brainfuck_code_output += '+' * value_adjustment_distance
    else:
        brainfuck_code_output += '-' * value_adjustment_distance

    memory_cells_ascii_values[current_cell_index] = target_ascii_value

    brainfuck_code_output += '.'

print brainfuck_code_output