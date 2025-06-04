stack_list = []
while True:
    command_input = raw_input().split()
    command_action = command_input[0]
    if command_action == "push":
        stack_list.append(command_input[1])
    elif command_action == "pop":
        print stack_list.pop()
    elif command_action == "quit":
        break