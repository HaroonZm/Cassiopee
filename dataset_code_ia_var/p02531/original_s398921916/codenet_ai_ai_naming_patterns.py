stack_content = ""
while True:
    command_parts = raw_input().split()
    command_action = command_parts[0]
    if command_action == "quit":
        break
    if command_action == "push":
        stack_content += command_parts[1]
    elif command_action == "pop":
        stack_length = len(stack_content)
        top_index = stack_length - 1
        print stack_content[top_index]
        stack_content = stack_content[:top_index]