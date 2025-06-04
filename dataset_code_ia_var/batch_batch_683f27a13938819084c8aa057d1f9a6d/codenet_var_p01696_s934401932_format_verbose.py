def char_to_alphabet_index(character):
    return ord(character) - ord('A')

def parse_input_string(input_string):
    current_offset = 0
    instruction_table = []
    
    for current_character in input_string:
        if current_character == '+':
            current_offset += 1
            
        elif current_character == '-':
            current_offset -= 1
            
        elif current_character == '[':
            instruction_table.append(current_character)
            
        elif current_character == ']':
            instruction_table.append(current_character)
            
        elif current_character == '?':
            instruction_table.append(current_character)
            current_offset = 0
            
        else:
            alphabet_index_with_offset = (char_to_alphabet_index(current_character) + current_offset) % 26
            instruction_table.append(alphabet_index_with_offset)
            current_offset = 0

    for table_index in range(len(instruction_table)):
        if instruction_table[table_index] == '?':
            instruction_table[table_index] = 0

    return instruction_table

def reverse_instructions(instruction_table):
    reconstructed_string = ""
    table_pointer = 0

    while table_pointer < len(instruction_table):
        current_element = instruction_table[table_pointer]
        
        if current_element == '[':
            bracket_depth = 1
            temp_pointer = table_pointer + 1

            while bracket_depth > 0:
                if instruction_table[temp_pointer] == '[':
                    bracket_depth += 1
                if instruction_table[temp_pointer] == ']':
                    bracket_depth -= 1
                temp_pointer += 1

            inner_reversed = reverse_instructions(instruction_table[table_pointer + 1 : temp_pointer - 1])[::-1]
            reconstructed_string += inner_reversed
            table_pointer = temp_pointer - 1

        elif current_element == ']':
            pass

        else:
            reconstructed_character = chr(current_element + ord('A'))
            reconstructed_string += reconstructed_character

        table_pointer += 1

    return reconstructed_string

while True:
    input_string = input()

    if input_string[0] == '.':
        break

    processed_table = parse_input_string(input_string)
    decoded_result = reverse_instructions(processed_table)
    print(decoded_result)