def are_strings_rotationally_equivalent(original_string, rotated_string):
    length_of_rotated = len(rotated_string)

    for rotation_index in range(length_of_rotated):
        rotated_string = rotated_string[-1] + rotated_string[0:(length_of_rotated - 1)]

        if original_string == rotated_string:
            return 'Yes'

    return 'No'


def read_two_strings_from_input():
    first_input_string = input()
    second_input_string = input()
    return (first_input_string, second_input_string)


def main():
    original_string, rotated_string = read_two_strings_from_input()
    rotation_equivalence_result = are_strings_rotationally_equivalent(original_string, rotated_string)
    print(rotation_equivalence_result)


if __name__ == '__main__':
    main()