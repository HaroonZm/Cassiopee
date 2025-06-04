shift_value = int(input())
input_string = input()
alphabet_list = []
for alphabet_index in range(26):
    alphabet_list.append(chr(65 + alphabet_index))
output_string = ''
for character_index in range(len(input_string)):
    current_position = alphabet_list.index(input_string[character_index])
    shifted_position = (current_position + shift_value) % 26
    output_string += alphabet_list[shifted_position]
print(output_string)