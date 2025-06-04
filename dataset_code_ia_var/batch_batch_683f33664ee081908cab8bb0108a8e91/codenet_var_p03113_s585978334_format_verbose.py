sorted_function = sorted

number_of_elements, number_of_steps, *input_array = map(int, open(input_file_index := 0).read().split())

list_of_sorted_tuples = sorted_function([-element, input_file_index := input_file_index + 1] for element in input_array)

_, ordered_indices = zip(*list_of_sorted_tuples)

while number_of_steps:
    *_, base_index = ordered_indices
    number_of_steps -= 1
    for current_tuple in sorted_function(list_of_sorted_tuples):
        if current_tuple[1] - base_index:
            if current_tuple[0] > -2:
                current_tuple[0] += 1
                ordered_indices += current_tuple[1],
            else:
                exit(print(-1))

print(len(ordered_indices), *ordered_indices)