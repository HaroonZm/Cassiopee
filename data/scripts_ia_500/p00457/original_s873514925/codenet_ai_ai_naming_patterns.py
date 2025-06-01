def read_input_block(num_elements):
    compressed_values = [int(input())]
    counts = [1]
    for _ in range(1, num_elements):
        current_value = int(input())
        if compressed_values[-1] == current_value:
            counts[-1] += 1
        else:
            compressed_values.append(current_value)
            counts.append(1)
    return compressed_values, counts

def evaluate_removal(compressed_values, counts, left_index, right_index):
    length = len(compressed_values)
    total_removed = 0
    if 0 <= left_index and counts[left_index] >= 4 and (right_index >= length or compressed_values[left_index] != compressed_values[right_index]):
        total_removed += counts[left_index]
        left_index -= 1
    if right_index < length and counts[right_index] >= 4 and (left_index < 0 or compressed_values[left_index] != compressed_values[right_index]):
        total_removed += counts[right_index]
        right_index += 1
    while 0 <= left_index and right_index < length and compressed_values[left_index] == compressed_values[right_index] and counts[left_index] + counts[right_index] >= 4:
        total_removed += counts[left_index] + counts[right_index]
        left_index -= 1
        right_index += 1
    return total_removed

def compute_max_removal(compressed_values, counts):
    length = len(compressed_values)
    max_removed = 0
    for index in range(length):
        counts[index] -= 1
        if index + 1 < length:
            counts[index + 1] += 1
            if counts[index] > 0:
                max_removed = max(max_removed, evaluate_removal(compressed_values, counts, index, index + 1))
            else:
                max_removed = max(max_removed, evaluate_removal(compressed_values, counts, index - 1, index + 1))
            counts[index + 1] -= 1
        if index - 1 >= 0:
            counts[index - 1] += 1
            if counts[index] > 0:
                max_removed = max(max_removed, evaluate_removal(compressed_values, counts, index - 1, index))
            else:
                max_removed = max(max_removed, evaluate_removal(compressed_values, counts, index - 1, index + 1))
            counts[index - 1] -= 1
        counts[index] += 1
    return max_removed

while True:
    number_of_elements = int(input())
    if number_of_elements == 0:
        break
    compressed_seq, counts_seq = read_input_block(number_of_elements)
    print(number_of_elements - compute_max_removal(compressed_seq, counts_seq))