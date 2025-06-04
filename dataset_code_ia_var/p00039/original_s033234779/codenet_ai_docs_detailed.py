import sys

def roman_char_to_int():
    """
    Returns a dictionary that maps Roman numeral characters to their corresponding integer values.

    Returns:
        dict: Mapping of Roman numeral symbols (str) to their integer values (int)
    """
    return {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

def roman_to_int(roman_str, value_mapping):
    """
    Converts a Roman numeral string to its corresponding integer value.
    Handles subtractive notation (e.g., 'IV' = 4, 'IX' = 9).

    Args:
        roman_str (str): The Roman numeral string to convert.
        value_mapping (dict): A dictionary mapping Roman symbols to integers.

    Returns:
        int: The integer value of the Roman numeral.
    """
    # Convert each Roman character to its corresponding value using the mapping.
    values = [value_mapping[char] for char in roman_str.rstrip()]
    # If there's only one character, its value is returned directly.
    if len(values) == 1:
        return values[0]
    # Start with the sum of all values.
    total = sum(values)
    # Traverse values to account for subtractive pairs.
    for i in range(len(values) - 1):
        # If a smaller value precedes a larger one, subtract twice that value.
        # This corrects for the initial sum which treated all additions as positive.
        if values[i] < values[i + 1]:
            total -= 2 * values[i]
    return total

def main():
    """
    Main function to process standard input for Roman numerals, convert each line
    to its integer value, and print the result.
    """
    value_mapping = roman_char_to_int()
    for line in sys.stdin:
        # Strip newline and whitespace, convert to integer, and print.
        integer_value = roman_to_int(line, value_mapping)
        print(integer_value)

if __name__ == '__main__':
    main()