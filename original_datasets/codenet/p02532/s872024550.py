stack = [[] for i in xrange(input()+1)]
while True:
    line = raw_input().split()
    if line[0] == 'quit': break
    elif line[0] == 'push':
        stack[int(line[1])].append(line[2])
    elif line[0] == 'pop':
        print stack[int(line[1])].pop()
    elif line[0] == 'move':
        stack[int(line[2])].append(stack[int(line[1])].pop())