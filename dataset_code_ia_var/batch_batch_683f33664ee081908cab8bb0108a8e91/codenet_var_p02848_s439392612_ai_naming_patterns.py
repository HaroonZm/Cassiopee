shift_value = int(input())
input_string = input()

output_string = ''
ascii_upper_a = ord('A')
ascii_upper_z = ord('Z')
for char in input_string:
    shifted_ascii = ord(char) + shift_value

    if shifted_ascii > ascii_upper_z:
        wrapped_ascii = ascii_upper_a + (shifted_ascii - ascii_upper_z - 1)
        output_string += chr(wrapped_ascii)
    else:
        output_string += chr(shifted_ascii)
        
print(output_string)