shift_value = int(input())
input_string = input()
result_string = ""
for char_index in range(len(input_string)):
    char_code = ord(input_string[char_index])
    shifted_code = char_code + shift_value
    if shifted_code <= 90:
        result_string += chr(shifted_code)
    else:
        result_string += chr(shifted_code - 26)
print(result_string)