blocks = []
pops = []

while True:
    try:
        order = map(str, raw_input().split(' '))
        if order[0] == 'quit':
            for po in pops:
                print po
            break
        elif order[0] == 'push':
            blocks.append(order[1])
        else:#pop
            pops.append(blocks[-1])
            blocks.pop()
            
            
    except EOFError:
        break