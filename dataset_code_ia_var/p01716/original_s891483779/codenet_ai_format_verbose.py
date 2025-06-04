import sys
from itertools import product

read_input_line = sys.stdin.readline
write_output = sys.stdout.write

def solve():
    MODULO = 10**9 + 7

    number_of_characters, number_of_patterns = map(int, read_input_line().split())
    input_string = read_input_line().strip()
    pattern_max_value = [0] * number_of_patterns
    pattern_length = [0] * number_of_patterns

    symbol_to_index = {}

    for digit_character in range(10):
        symbol_to_index[str(digit_character)] = digit_character

    for pattern_index in range(number_of_patterns):
        pattern_symbol, pattern_digit_string = read_input_line().split()
        symbol_to_index[pattern_symbol] = pattern_index + 10
        pattern_length[pattern_index] = len(pattern_digit_string)
        pattern_max_value[pattern_index] = int(pattern_digit_string)

    def find_representative(element_index):
        if parent[element_index] == element_index:
            return element_index
        parent[element_index] = resulting_parent = find_representative(parent[element_index])
        return resulting_parent

    def unite_elements(element_index_a, element_index_b):
        parent_a = find_representative(element_index_a)
        parent_b = find_representative(element_index_b)
        if parent_a < parent_b:
            parent[element_index_b] = parent_a
        else:
            parent[element_index_a] = parent_b

    mapping_list = list(map(symbol_to_index.__getitem__, input_string))
    total_number_of_ways = 0

    for pattern_choices in product([1, 2], repeat=number_of_patterns):

        pattern_choice_valid = True
        for current_pattern_index in range(number_of_patterns):
            if pattern_choices[current_pattern_index] > pattern_length[current_pattern_index]:
                pattern_choice_valid = False
                break
        if not pattern_choice_valid:
            continue

        parent = list(range(10 + number_of_patterns * 2))

        left_index = 0
        current_left_pattern_progress = pattern_choices[mapping_list[left_index] - 10] - 1 if mapping_list[left_index] >= 10 else 0
        right_index = number_of_characters - 1
        current_right_pattern_progress = 0

        while left_index < right_index or (left_index == right_index and current_right_pattern_progress < current_left_pattern_progress):
            if mapping_list[left_index] >= 10:
                left_element = mapping_list[left_index] * 2 - 10 + current_left_pattern_progress
                if current_left_pattern_progress - 1 == -1:
                    left_index += 1
                    current_left_pattern_progress = pattern_choices[mapping_list[left_index] - 10] - 1 if mapping_list[left_index] >= 10 else 0
                else:
                    current_left_pattern_progress -= 1
            else:
                left_element = mapping_list[left_index]
                left_index += 1
                current_left_pattern_progress = pattern_choices[mapping_list[left_index] - 10] - 1 if mapping_list[left_index] >= 10 else 0

            if mapping_list[right_index] >= 10:
                right_element = mapping_list[right_index] * 2 - 10 + current_right_pattern_progress
                if current_right_pattern_progress + 1 == pattern_choices[mapping_list[right_index] - 10]:
                    right_index -= 1
                    current_right_pattern_progress = 0
                else:
                    current_right_pattern_progress += 1
            else:
                right_element = mapping_list[right_index]
                right_index -= 1
                current_right_pattern_progress = 0

            unite_elements(left_element, right_element)

        for digit_index in range(10):
            if find_representative(digit_index) != digit_index:
                pattern_choice_valid = False
                break
        if not pattern_choice_valid:
            continue

        min_digit_for_group = [0] * (10 + number_of_patterns * 2)
        max_digit_for_group = [9] * (10 + number_of_patterns * 2)
        min_digit = [0] * (10 + number_of_patterns * 2)
        max_digit = [9] * (10 + number_of_patterns * 2)
        parent_backup = parent[:]

        for subpattern_choices in product([0, 1], repeat=number_of_patterns):

            min_digit[:] = min_digit_for_group
            max_digit[:] = max_digit_for_group
            subpattern_valid = True

            for current_pattern_index in range(number_of_patterns):
                if pattern_choices[current_pattern_index] < pattern_length[current_pattern_index] and subpattern_choices[current_pattern_index] == 1:
                    subpattern_valid = False
                    break
            if not subpattern_valid:
                continue

            parent[:] = parent_backup

            for digit_index in range(10):
                min_digit[digit_index] = max_digit[digit_index] = digit_index

            for current_pattern_index in range(number_of_patterns):
                if pattern_length[current_pattern_index] == 1:
                    match_digit = pattern_max_value[current_pattern_index]
                    pattern_element_0 = 2 * current_pattern_index + 10
                    if subpattern_choices[current_pattern_index]:
                        unite_elements(match_digit, pattern_element_0)
                    else:
                        max_digit[pattern_element_0] = match_digit - 1
                else:
                    pattern_first_digit, pattern_second_digit = divmod(pattern_max_value[current_pattern_index], 10)
                    pattern_element_0 = 2 * current_pattern_index + 10
                    pattern_element_1 = 2 * current_pattern_index + 11
                    if subpattern_choices[current_pattern_index]:
                        unite_elements(pattern_first_digit, pattern_element_1)
                        max_digit[pattern_element_0] = pattern_second_digit
                    else:
                        max_digit[pattern_element_0] = 9
                        if pattern_choices[current_pattern_index] == 2:
                            max_digit[pattern_element_1] = pattern_first_digit - 1
                            min_digit[pattern_element_1] = 1

            for group_index in range(10 + 2 * number_of_patterns):
                group_representative = find_representative(group_index)
                min_digit[group_representative] = max(min_digit[group_representative], min_digit[group_index])
                max_digit[group_representative] = min(max_digit[group_representative], max_digit[group_index])

            for digit_index in range(10):
                if find_representative(digit_index) != digit_index or not (min_digit[digit_index] == digit_index == max_digit[digit_index]):
                    subpattern_valid = False
                    break
            if not subpattern_valid:
                continue

            number_of_combinations = 1
            for current_pattern_index in range(number_of_patterns):
                pattern_element_0 = 2 * current_pattern_index + 10
                pattern_element_1 = 2 * current_pattern_index + 11
                if pattern_choices[current_pattern_index] == 2:
                    if find_representative(pattern_element_1) == pattern_element_1:
                        if not min_digit[pattern_element_1] <= max_digit[pattern_element_1]:
                            number_of_combinations = 0
                            break
                        number_of_combinations = number_of_combinations * (max_digit[pattern_element_1] - min_digit[pattern_element_1] + 1) % MODULO
                if find_representative(pattern_element_0) == pattern_element_0:
                    if not min_digit[pattern_element_0] <= max_digit[pattern_element_0]:
                        number_of_combinations = 0
                        break
                    number_of_combinations = number_of_combinations * (max_digit[pattern_element_0] - min_digit[pattern_element_0] + 1) % MODULO

            total_number_of_ways += number_of_combinations

    total_number_of_ways %= MODULO
    write_output("%d\n" % total_number_of_ways)

solve()