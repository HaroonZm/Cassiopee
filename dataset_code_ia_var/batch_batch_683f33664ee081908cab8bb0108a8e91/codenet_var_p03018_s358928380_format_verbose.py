import sys
from collections import defaultdict

input_stream = sys.stdin.buffer

def get_values_from_input_line(element_processing_function=lambda s: s.decode()):
    """
    Reads a line from input and returns an iterator of its space-separated elements,
    each processed by the specified function.
    """
    return map(element_processing_function, input_stream.readline().split())

def get_single_processed_line(processing_function=lambda s: s.decode()):
    """
    Reads a line from input, strips the trailing newline, and processes it with
    the specified function.
    """
    return processing_function(input_stream.readline().rstrip())

def main():
    input_character_list = [character for character in get_single_processed_line()]
    total_abc_substring_count = 0
    consecutive_a_count = 0
    current_position = 0

    while current_position < len(input_character_list) - 2:

        current_three_characters = "".join(
            input_character_list[current_position : current_position + 3]
        )

        if current_three_characters == "ABC":
            total_abc_substring_count += consecutive_a_count + 1
            current_position += 2
            input_character_list[current_position] = "A"
        else:
            if input_character_list[current_position] == "A":
                consecutive_a_count += 1
            else:
                consecutive_a_count = 0
            current_position += 1

    print(total_abc_substring_count)

if __name__ == "__main__":
    main()