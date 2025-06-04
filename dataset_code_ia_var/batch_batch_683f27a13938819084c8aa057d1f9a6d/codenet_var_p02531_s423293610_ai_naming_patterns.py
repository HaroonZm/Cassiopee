data_stack = []
while True:
    input_line = raw_input().split()
    command = input_line[0]
    if command == 'quit':
        break
    elif command == 'push':
        data_stack.append(input_line[1])
    elif command == 'pop':
        print data_stack[-1]
        data_stack.pop()