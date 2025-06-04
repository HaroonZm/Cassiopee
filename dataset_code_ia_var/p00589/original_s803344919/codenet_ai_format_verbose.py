# Définition du tableau de correspondance des chiffres du clavier au texte
keypad_digit_to_characters = [
    "",
    "',.!?",
    "abcABC",
    "defDEF",
    "ghiGHI",
    "jklJKL",
    "mnoMNO",
    "pqrsPQRS",
    "tuvTUV",
    "wxyzWXYZ"
]

while True:
    try:
        input_line = input().strip()
    except:
        break

    decoded_text = ''
    current_position = 0

    while current_position < len(input_line):
        current_digit_character = input_line[current_position]
        repetition_count = 0
        keypad_digit = int(current_digit_character)
        current_position += 1

        # Compte le nombre de pressions consécutives sur la même touche
        while (current_position < len(input_line) and 
               input_line[current_position] == current_digit_character):
            repetition_count += 1
            current_position += 1

        if keypad_digit == 0:
            decoded_text += ' ' * repetition_count
        else:
            corresponding_characters = keypad_digit_to_characters[keypad_digit]
            selected_character = corresponding_characters[repetition_count % len(corresponding_characters)]
            decoded_text += selected_character

    print(decoded_text)