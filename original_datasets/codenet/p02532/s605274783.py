n = input()

blocks = [ [] for x in range(n)]
pops = []

while True:
    try:
        order = map(str, raw_input().split(' '))
        if order[0] == 'quit':
            for po in pops:
                print po
            break
        elif order[0] == 'push':
            blocks[int(order[1])-1].append(order[2])
            
            
        elif order[0] == 'pop':
            pops.append(blocks[int(order[1])-1][-1])
            blocks[int(order[1])-1].pop()
            
            
        else : #move
            blocks[int(order[2])-1].append(blocks[int(order[1])-1][-1])
            blocks[int(order[1])-1].pop()
            
            
    except EOFError:
        break