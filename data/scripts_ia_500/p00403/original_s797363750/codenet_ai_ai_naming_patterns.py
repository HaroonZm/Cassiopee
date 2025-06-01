line_count = int(input())
commands_list = list(map(int, input().split()))
active_stack = []
for command_index in range(len(commands_list)):
    current_command = commands_list[command_index]
    if current_command > 0:
        if active_stack.count(current_command):
            print(command_index + 1)
            exit(0)
        else:
            active_stack.append(current_command)
    else:
        if len(active_stack) == 0 or active_stack[-1] != abs(current_command):
            print(command_index + 1)
            exit(0)
        else:
            del active_stack[-1]
print('OK')