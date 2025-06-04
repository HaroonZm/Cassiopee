input_count = int(input())
sequence_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
for index_sequence in range(input_count):
    current_last_digit = sequence_list[index_sequence][-1]
    current_base = sequence_list[index_sequence]
    if current_last_digit == "9":
        sequence_list.append(current_base + str(int(current_last_digit) - 1))
        sequence_list.append(current_base + current_last_digit)
    elif current_last_digit == "0":
        sequence_list.append(current_base + current_last_digit)
        sequence_list.append(current_base + str(int(current_last_digit) + 1))
    else:
        sequence_list.append(current_base + str(int(current_last_digit) - 1))
        sequence_list.append(current_base + current_last_digit)
        sequence_list.append(current_base + str(int(current_last_digit) + 1))
print(sequence_list[input_count - 1])