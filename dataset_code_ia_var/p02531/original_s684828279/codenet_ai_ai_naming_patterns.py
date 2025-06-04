command_stack = []
while True:
    input_parts = raw_input().split()
    command_action = input_parts[0]
    if command_action == 'quit':
        break
    elif command_action == 'push':
        command_stack.append(input_parts[1])
    elif command_action == 'pop':
        print command_stack.pop()