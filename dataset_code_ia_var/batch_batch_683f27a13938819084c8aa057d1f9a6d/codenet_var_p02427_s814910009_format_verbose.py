number_of_elements_in_set = int(input())

print('0:')

for current_subset_integer in range(1, 2 ** number_of_elements_in_set):

    binary_representation_reversed = f'{current_subset_integer:b}'[::-1]

    selected_element_indices = [
        element_index
        for element_index, bit_char in enumerate(binary_representation_reversed)
        if bit_char == '1'
    ]

    subset_elements_str = " ".join(map(str, selected_element_indices))

    print(f'{current_subset_integer}: {subset_elements_str}')