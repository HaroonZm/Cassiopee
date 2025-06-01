cat_presence_flags = [0 for index_cat in range(101)]
cat_stack = []

sequence_length = int(input())
command_values = [int(command) for command in input().split()]

error_position = -1
for position in range(sequence_length):
    current_command = command_values[position]
    if current_command > 0:
        if cat_presence_flags[current_command] == 1:
            error_position = position + 1
            break
        else:
            cat_presence_flags[current_command] = 1
            cat_stack.append(current_command)
    else:
        absolute_command = -current_command
        if cat_presence_flags[absolute_command] == 0:
            error_position = position + 1
            break
        else:
            cat_presence_flags[absolute_command] = 0
            if cat_stack.pop() != absolute_command:
                error_position = position + 1
                break
if error_position < 0:
    print("OK")
else:
    print(error_position)