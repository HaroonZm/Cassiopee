def is_non_decreasing_sequence(sequence):
    for current_index in range(1, len(sequence)):
        if sequence[current_index] < sequence[current_index - 1]:
            return False
    return True


def can_split_into_non_decreasing_sequences(input_array, sequence_one, sequence_two, current_position):
    total_selected_elements = len(sequence_one) + len(sequence_two)

    if total_selected_elements == 10:
        return is_non_decreasing_sequence(sequence_one) and is_non_decreasing_sequence(sequence_two)

    updated_sequence_one = sequence_one[:]
    updated_sequence_two = sequence_two[:]

    updated_sequence_one.append(input_array[current_position])
    updated_sequence_two.append(input_array[current_position])

    return (
        can_split_into_non_decreasing_sequences(input_array, updated_sequence_one, sequence_two, current_position + 1)
        or
        can_split_into_non_decreasing_sequences(input_array, sequence_one, updated_sequence_two, current_position + 1)
    )


def process_datasets():
    number_of_datasets = int(input())
    for dataset_index in range(number_of_datasets):
        elements = [int(element) for element in input().split()]
        split_possible = can_split_into_non_decreasing_sequences(elements, [], [], 0)
        print('YES' if split_possible else 'NO')


if __name__ == '__main__':
    process_datasets()