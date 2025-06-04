import sys

standard_input_stream = sys.stdin

def read_integer():
    return int(read_string())

def read_integer_list():
    return list(map(int, standard_input_stream.readline().split()))

def read_string():
    return standard_input_stream.readline()

input_string = input()

result_string = ""

for character_index in range(len(input_string)):

    current_character = input_string[character_index]

    if current_character == '0' or current_character == '1':
        result_string += current_character
    else:
        if len(result_string) > 0:
            result_string = result_string[:-1]

print(result_string)