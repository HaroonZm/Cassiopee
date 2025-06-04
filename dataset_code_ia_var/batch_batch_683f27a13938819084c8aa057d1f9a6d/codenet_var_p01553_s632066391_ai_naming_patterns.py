input_size = int(input())
input_sequence = [input() for input_index in range(input_size)]
modulus_value = 10 ** 9 + 7

dynamic_table = [[0 for dp_col in range(input_size + 1)] for dp_row in range(input_size + 1)]
dynamic_table[0][0] = 1

for seq_index, sequence_char in enumerate(input_sequence):
    if sequence_char == "-":
        for state_count in range(input_size + 1):
            if state_count + 1 < input_size + 1:
                dynamic_table[seq_index + 1][state_count + 1] += dynamic_table[seq_index][state_count]
                dynamic_table[seq_index + 1][state_count + 1] %= modulus_value

    if sequence_char == "U":
        for state_count in range(input_size + 1):
            dynamic_table[seq_index + 1][state_count] += dynamic_table[seq_index][state_count]
            dynamic_table[seq_index + 1][state_count] %= modulus_value
            if state_count + 1 < input_size + 1:
                dynamic_table[seq_index + 1][state_count + 1] += dynamic_table[seq_index][state_count] * (seq_index - state_count)
                dynamic_table[seq_index + 1][state_count + 1] %= modulus_value

    if sequence_char == "D":
        for state_count in range(input_size + 1):
            if state_count + 1 < input_size + 1:
                dynamic_table[seq_index + 1][state_count + 1] += dynamic_table[seq_index][state_count] * (seq_index - state_count)
                dynamic_table[seq_index + 1][state_count + 1] %= modulus_value
            if state_count + 2 < input_size + 1:
                dynamic_table[seq_index + 1][state_count + 2] += dynamic_table[seq_index][state_count] * (seq_index - state_count) ** 2
                dynamic_table[seq_index + 1][state_count + 2] %= modulus_value

print(dynamic_table[-1][-1])