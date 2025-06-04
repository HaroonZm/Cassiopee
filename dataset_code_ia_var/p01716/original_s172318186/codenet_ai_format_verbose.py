def depth_first_search(possibilities_list, input_string, character_pool, min_allowed_count, max_allowed_count):

    if len(possibilities_list) == 0:
        return solve_palindrome(input_string, character_pool, min_allowed_count, max_allowed_count)

    current_character, character_limit = possibilities_list[0]
    updated_character_pool = character_pool + current_character

    if character_limit <= 9:
        min_allowed_count[current_character] = 0
        max_allowed_count[current_character] = character_limit
        return depth_first_search(
            possibilities_list[1:], input_string, updated_character_pool, min_allowed_count, max_allowed_count
        )

    min_allowed_count[current_character] = 0
    max_allowed_count[current_character] = 9
    partial_result = depth_first_search(
        possibilities_list[1:], input_string, updated_character_pool, min_allowed_count, max_allowed_count
    )

    uppercase_character = current_character.upper()
    translated_input_string = input_string.translate(
        str.maketrans({current_character: uppercase_character + current_character})
    )
    extended_character_pool = updated_character_pool + uppercase_character

    if character_limit % 10 == 9:
        min_allowed_count[uppercase_character] = 1
        max_allowed_count[uppercase_character] = character_limit // 10
        return partial_result + depth_first_search(
            possibilities_list[1:], translated_input_string, extended_character_pool, min_allowed_count, max_allowed_count
        )

    if character_limit >= 20:
        min_allowed_count[uppercase_character] = 1
        max_allowed_count[uppercase_character] = (character_limit // 10) - 1
        partial_result += depth_first_search(
            possibilities_list[1:], translated_input_string, extended_character_pool, min_allowed_count, max_allowed_count
        )

    min_allowed_count[current_character] = 0
    max_allowed_count[current_character] = character_limit % 10
    min_allowed_count[uppercase_character] = character_limit // 10
    max_allowed_count[uppercase_character] = character_limit // 10

    return partial_result + depth_first_search(
        possibilities_list[1:], translated_input_string, extended_character_pool, min_allowed_count, max_allowed_count
    )

def solve_palindrome(input_string, character_pool, min_allowed_count, max_allowed_count):

    union_find_structure = [-1] * 128
    half_length = len(input_string) // 2

    first_half_characters = map(ord, input_string[:half_length])
    second_half_characters = map(ord, input_string[::-1][:half_length])

    for left_char, right_char in zip(first_half_characters, second_half_characters):
        root_left = find_root(union_find_structure, left_char)
        root_right = find_root(union_find_structure, right_char)

        if root_left != root_right:
            if union_find_structure[root_left] >= union_find_structure[root_right]:
                union_find_structure[root_left] += union_find_structure[root_right]
                union_find_structure[root_right] = root_left
            else:
                union_find_structure[root_right] += union_find_structure[root_left]
                union_find_structure[root_left] = root_right

    min_count_by_root, max_count_by_root = {}, {}

    for char in character_pool:
        root_index = find_root(union_find_structure, ord(char))
        root_str = str(root_index)
        try:
            max_count_by_root[root_str] = min(max_count_by_root[root_str], max_allowed_count[char])
            min_count_by_root[root_str] = max(min_count_by_root[root_str], min_allowed_count[char])
        except KeyError:
            max_count_by_root[root_str] = max_allowed_count[char]
            min_count_by_root[root_str] = min_allowed_count[char]

    total_ways = 1
    for root_str in max_count_by_root.keys():
        if max_count_by_root[root_str] < min_count_by_root[root_str]:
            return 0
        total_ways *= max_count_by_root[root_str] - min_count_by_root[root_str] + 1

    return total_ways

def find_root(union_find_array, position):
    if union_find_array[position] < 0:
        return position
    union_find_array[position] = find_root(union_find_array, union_find_array[position])
    return union_find_array[position]

import sys

input_stream = sys.stdin

_, _ = map(int, input_stream.readline().split())
input_line = input_stream.readline().strip()
input_possibilities = [line.split() for line in input_stream]

for possibility in input_possibilities:
    possibility[1] = int(possibility[1])

minimum_count_constraints = {str(digit): digit for digit in range(10)}
maximum_count_constraints = {str(digit): digit for digit in range(10)}
starting_characters = '0123456789'

result = depth_first_search(
    input_possibilities,
    input_line,
    starting_characters,
    minimum_count_constraints,
    maximum_count_constraints
)

print(result % (10 ** 9 + 7))