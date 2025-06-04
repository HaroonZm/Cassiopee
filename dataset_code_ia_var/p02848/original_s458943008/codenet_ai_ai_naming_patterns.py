shift_offset = int(input())
input_string = input()

def apply_shift(character, shift_amount):
    normalized_shift = shift_amount % 26
    base_ascii = ord(character)
    shifted_ascii = base_ascii + normalized_shift
    if shifted_ascii > ord('Z'):
        shifted_ascii -= 26
    return chr(shifted_ascii)

output_string = ""
for current_char in input_string:
    output_string += apply_shift(current_char, shift_offset)

print(output_string)