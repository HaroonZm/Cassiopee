number_of_letter_shifts = int(input())

original_text = input()

def shift_character_in_alphabet(character_to_shift, shift_amount):

    if shift_amount > 25:
        shift_amount = shift_amount % 26

    if ord(character_to_shift) + shift_amount > ord('Z'):
        shift_amount = shift_amount - 26

    return chr(ord(character_to_shift) + shift_amount)

shifted_text = ""

for character in original_text:
    shifted_text += shift_character_in_alphabet(character, number_of_letter_shifts)

print(shifted_text)