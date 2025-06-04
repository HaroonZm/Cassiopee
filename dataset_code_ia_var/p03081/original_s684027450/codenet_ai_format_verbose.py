number_of_elements, number_of_queries = [int(value) for value in input().split()]

character_sequence = input()

transformation_directions = []
for _ in range(number_of_queries):
    transformation_character, movement_direction = input().split()
    transformation_directions.append((transformation_character, movement_direction))


def character_is_eliminated(sequence_index):
    current_index = sequence_index
    for character, direction in transformation_directions:
        if character == character_sequence[current_index]:
            if direction == 'L':
                current_index -= 1
                if current_index == -1:
                    return -1
            else:
                current_index += 1
                if current_index == number_of_elements:
                    return +1
    return 0


binary_search_left, binary_search_right = -1, number_of_elements

while binary_search_right - binary_search_left > 1:
    middle_index = (binary_search_left + binary_search_right) // 2
    if character_is_eliminated(middle_index) == -1:
        binary_search_left = middle_index
    else:
        binary_search_right = middle_index

leftmost_surviving_index = binary_search_right

binary_search_left, binary_search_right = -1, number_of_elements

while binary_search_right - binary_search_left > 1:
    middle_index = (binary_search_left + binary_search_right) // 2
    if character_is_eliminated(middle_index) == +1:
        binary_search_right = middle_index
    else:
        binary_search_left = middle_index

rightmost_surviving_index = binary_search_left

number_of_surviving_characters = rightmost_surviving_index - leftmost_surviving_index + 1

print(number_of_surviving_characters)

# print((leftmost_surviving_index, rightmost_surviving_index))
# print([character_is_eliminated(idx) for idx in range(number_of_elements)])