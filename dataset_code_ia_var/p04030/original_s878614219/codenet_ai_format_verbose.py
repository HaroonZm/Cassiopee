input_string = input().strip()

resulting_string = ''

for current_character in input_string:

    if current_character == 'B':

        if len(resulting_string) > 0:
            resulting_string = resulting_string[:-1]

    else:
        resulting_string += current_character

print(resulting_string)