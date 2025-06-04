stack_data = []
output_data = []

while True:
    try:
        command_parts = map(str, raw_input().split(' '))
        command_action = command_parts[0]
        if command_action == 'quit':
            for output_item in output_data:
                print output_item
            break
        elif command_action == 'push':
            stack_data.append(command_parts[1])
        else:  # pop
            output_data.append(stack_data[-1])
            stack_data.pop()
    except EOFError:
        break