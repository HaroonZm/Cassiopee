stack = []
while True:
    line = raw_input().split()
    if line[0] == 'quit':
        break
    elif line[0] == 'push':
        stack.append(line[1])
    elif line[0] == 'pop':
        print stack[-1]
        stack.pop()