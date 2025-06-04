import sys

# Liste des lettres majuscules anglaises de 'A' à 'Z'
alphabet_uppercase_list = [chr(ascii_code) for ascii_code in range(ord('A'), ord('Z') + 1)]

def reverse_bracketed_substring(input_string, original_position_offset):
    reversed_result = ""
    collected_substring = ""
    current_index = 0

    while current_index < len(input_string):

        if input_string[current_index] == '[':
            nested_result, updated_index = reverse_bracketed_substring(input_string[current_index + 1:], current_index + 1)
            collected_substring += nested_result

        elif input_string[current_index] == ']':
            # Retourne la sous-chaîne inversée et la nouvelle position
            return collected_substring[::-1], current_index + original_position_offset

        else:
            collected_substring += input_string[current_index]

        current_index += 1

def process_letter_expression(input_expression):
    alphabet_shift_accumulator = 0
    expression_with_letters_applied = ""

    for character in input_expression:

        if character == '+':
            alphabet_shift_accumulator += 1

        if character == '-':
            alphabet_shift_accumulator -= 1

        if 'A' <= character <= 'Z':
            shifted_index = ((ord(character) - ord('A') + alphabet_shift_accumulator + 26 * 30) % 26)
            expression_with_letters_applied += alphabet_uppercase_list[shifted_index]
            alphabet_shift_accumulator = 0

        if character == '?':
            expression_with_letters_applied += 'A'
            alphabet_shift_accumulator = 0

        if character == '[' or character == ']':
            expression_with_letters_applied += character

    final_result_after_bracket_reversal = ""
    parse_index = 0

    while parse_index < len(expression_with_letters_applied):

        if expression_with_letters_applied[parse_index] == '[':
            reversed_substring, new_index = reverse_bracketed_substring(expression_with_letters_applied[parse_index + 1:], parse_index + 1)
            final_result_after_bracket_reversal += reversed_substring
            parse_index = new_index

        elif expression_with_letters_applied[parse_index] != ']':
            final_result_after_bracket_reversal += expression_with_letters_applied[parse_index]

        parse_index += 1

    return final_result_after_bracket_reversal

def main():
    while True:
        try:
            user_input_line = raw_input()
        except EOFError:
            break

        if user_input_line == ".":
            break

        print process_letter_expression(user_input_line)

main()