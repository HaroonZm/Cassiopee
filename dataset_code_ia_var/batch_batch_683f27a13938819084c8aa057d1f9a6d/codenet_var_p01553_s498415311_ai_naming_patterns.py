input_count = int(input())
input_lines = [input() for input_index in range(input_count)]
input_sequence = "".join(input_lines).replace("-", "")
sequence_length = len(input_sequence)
modulo_value = 10**9 + 7
dp_table = [[0 for column_index in range(sequence_length + 1)] for row_index in range(sequence_length + 1)]
dp_table[0][0] = 1
for current_position in range(sequence_length):
    current_char = input_sequence[current_position]
    if current_char == "D":
        for stack_depth in range(1, sequence_length + 1):
            dp_table[current_position + 1][stack_depth] = (dp_table[current_position + 1][stack_depth] + dp_table[current_position][stack_depth] * stack_depth) % modulo_value
            dp_table[current_position + 1][stack_depth - 1] = (dp_table[current_position + 1][stack_depth - 1] + dp_table[current_position][stack_depth] * stack_depth ** 2) % modulo_value
    else:
        for stack_depth in range(sequence_length):
            dp_table[current_position + 1][stack_depth + 1] = (dp_table[current_position + 1][stack_depth + 1] + dp_table[current_position][stack_depth]) % modulo_value
            dp_table[current_position + 1][stack_depth] = (dp_table[current_position + 1][stack_depth] + dp_table[current_position][stack_depth] * stack_depth) % modulo_value
print(dp_table[sequence_length][0])