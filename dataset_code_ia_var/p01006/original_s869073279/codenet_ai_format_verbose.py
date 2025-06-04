import sys

def main():
    input_password_lines = []
    
    for input_line in sys.stdin.readlines():
        stripped_password = input_line.strip()
        input_password_lines.append(stripped_password)
    
    validated_passwords = filter_passwords_by_hitofude(input_password_lines)
    
    for valid_password in validated_passwords:
        print(valid_password)
    
    return 0

def filter_passwords_by_hitofude(password_list):
    return [
        password
        for password in password_list
        if is_hitofude_password(password)
    ]

def is_hitofude_password(password_text):
    for current_letter, next_letter in generate_reversed_pairs(password_text):
        if next_letter == '':
            break
        if not is_adjacent_on_keyboard(current_letter, next_letter):
            return False
    return True

def generate_reversed_pairs(text):
    reversed_characters = list(text)
    reversed_characters.reverse()
    while True:
        if len(reversed_characters) >= 2:
            yield (reversed_characters.pop(), reversed_characters[-1])
        elif len(reversed_characters) == 1:
            yield (reversed_characters.pop(), '')
        else:
            break

keyboard_rows = [
    "ABC",
    "DEF",
    "GHI"
]

adjacent_key_pairs = []

for row_index, row_keys in enumerate(keyboard_rows):
    for column_index, key_char in enumerate(row_keys):
        
        if column_index + 1 < len(row_keys):
            adjacent_key_pairs.append((key_char, row_keys[column_index + 1]))
        
        if column_index - 1 >= 0:
            adjacent_key_pairs.append((key_char, row_keys[column_index - 1]))
        
        if row_index + 1 < len(keyboard_rows):
            adjacent_key_pairs.append((key_char, keyboard_rows[row_index + 1][column_index]))
        
        if row_index - 1 >= 0:
            adjacent_key_pairs.append((key_char, keyboard_rows[row_index - 1][column_index]))

def is_adjacent_on_keyboard(first_character, second_character):
    return (first_character, second_character) in adjacent_key_pairs

if __name__ == '__main__':
    main()