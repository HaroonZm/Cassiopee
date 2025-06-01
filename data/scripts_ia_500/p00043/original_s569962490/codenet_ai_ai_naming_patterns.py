import sys

def process_line(remaining_numbers):
    if not remaining_numbers and sequence_counter == 1:
        valid_sequences.append(current_check_number)
        return True
    for number in remaining_numbers:
        if has_triplet(number, remaining_numbers):
            return True
        if has_pair(number, remaining_numbers):
            return True
        if has_straight(number, remaining_numbers):
            return True

def has_triplet(number, remaining_numbers):
    count = 0
    for check_number in remaining_numbers[:3]:
        if check_number == number:
            count += 1
    else:
        if count == 3:
            if process_line(remaining_numbers[3:]):
                return True

def has_pair(number, remaining_numbers):
    global sequence_counter
    count = 0
    for check_number in remaining_numbers[:2]:
        if check_number == number:
            count += 1
    else:
        if count == 2:
            sequence_counter += 1
            if process_line(remaining_numbers[2:]):
                return True
            sequence_counter -= 1

def has_straight(number, remaining_numbers):
    sequence_numbers = [number, number + 1, number + 2]
    while True:
        for seq_num in sequence_numbers:
            if seq_num < 0 or seq_num not in remaining_numbers:
                sequence_numbers = [x -1 for x in sequence_numbers]
                break
        else:
            temp_numbers = remaining_numbers.copy()
            for seq_num in sequence_numbers:
                temp_numbers.remove(seq_num)
            if process_line(temp_numbers):
                return True
            break

sequence_counter = 0
valid_sequences = []
current_check_number = 0
for input_line in sys.stdin:
    input_line = input_line.rstrip()
    for i in range(9):
        current_check_number = i + 1
        combined_line = sorted(input_line + str(current_check_number))
        combined_line_str = ''.join(combined_line)
        idx = combined_line_str.find(str(current_check_number))
        if combined_line_str[idx:idx + 5] == str(current_check_number) * 5:
            continue
        process_line([int(char) for char in combined_line])
        result = sorted([str(num) for num in valid_sequences])
        sequence_counter = 0
    else:
        if valid_sequences:
            print(' '.join(result))
        else:
            print(0)
    sequence_counter = 0
    valid_sequences = []
    current_check_number = 0