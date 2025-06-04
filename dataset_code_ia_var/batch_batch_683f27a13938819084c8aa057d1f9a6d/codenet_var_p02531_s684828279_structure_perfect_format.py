stack = []
while True:
    s = raw_input().split()
    if s[0] == 'quit':
        break
    elif s[0] == 'push':
        stack.append(s[1])
    elif s[0] == 'pop':
        print stack.pop()