skip_input = input()
raw_input_line = input()
raw_input_list = raw_input_line.split(' ')
int_input_list = [int(element) for element in raw_input_list]
sequence_max_length = 1
current_sequence_length = 1
for current_value in int_input_list:
    if current_value == 1:
        current_sequence_length += 1
    else:
        sequence_max_length = max(sequence_max_length, current_sequence_length)
        current_sequence_length = 1
sequence_max_length = max(sequence_max_length, current_sequence_length)
print(sequence_max_length)