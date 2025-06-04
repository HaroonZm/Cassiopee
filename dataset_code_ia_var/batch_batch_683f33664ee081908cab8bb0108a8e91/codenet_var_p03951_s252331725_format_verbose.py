import sys

def read_next_nonempty_string() -> str:
    current_string = ""
    while True:
        next_character = sys.stdin.read(1)
        if next_character.strip() != "":
            current_string += next_character
        elif next_character != '\r':
            break
    return current_string

def main() -> None:
    number_of_characters_in_strings = int(read_next_nonempty_string())
    first_string = read_next_nonempty_string()
    second_string = read_next_nonempty_string()

    minimum_concatenated_length = number_of_characters_in_strings

    for overlap_start_index in range(number_of_characters_in_strings):

        is_overlap_invalid = False

        for comparison_offset in range(number_of_characters_in_strings - overlap_start_index):

            first_char = first_string[overlap_start_index + comparison_offset]
            second_char = second_string[comparison_offset]

            if first_char != second_char:
                minimum_concatenated_length += 1
                is_overlap_invalid = True
                break

        if not is_overlap_invalid:
            break

    print(minimum_concatenated_length)

if __name__ == '__main__':
    main()