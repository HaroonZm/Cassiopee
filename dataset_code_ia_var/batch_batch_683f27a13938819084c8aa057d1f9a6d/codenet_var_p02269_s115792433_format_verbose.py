number_of_commands = int(input())

command_types = [''] * number_of_commands
target_strings = [''] * number_of_commands

for command_index in range(number_of_commands):
    current_command_type, current_target_string = map(str, input().split())
    command_types[command_index] = current_command_type
    target_strings[command_index] = current_target_string

string_dictionary = {}

for command_index in range(number_of_commands):
    current_command_type = command_types[command_index]
    current_target_string = target_strings[command_index]

    if current_command_type == 'insert':
        string_dictionary.setdefault(current_target_string, 0)
    else:
        if current_target_string in string_dictionary:
            print('yes')
        else:
            print('no')