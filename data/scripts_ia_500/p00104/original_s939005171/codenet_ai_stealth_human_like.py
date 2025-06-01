while True:
    H, W = map(int, raw_input().split())
    if H == 0 and W == 0:
        # end of input
        break
    room = []
    for _ in range(H):
        room.append(list(raw_input()))
    x, y = 0, 0
    while True:
        current = room[y][x]
        room[y][x] = '*'  # mark visited
        if current == '>':
            x += 1
        elif current == '<':
            x -= 1
        elif current == 'v':
            y += 1
        elif current == '^':
            y -= 1
        elif current == '.':
            print x, y
            break
        else:
            # some kind of loop detected
            print "LOOP"
            break