while True:
    H, W = map(int,raw_input().split())
    if H == W == 0:
        break
    room = [list(raw_input()) for i in range(H)]
    x,y = 0,0
    while True:
        tile = room[y][x]
        room[y][x] = '*'
        if tile == '>':
            x += 1
        elif tile == '<':
            x -= 1
        elif tile == 'v':
            y += 1
        elif tile == '^':
            y -= 1
        elif tile == '.':
            print x,y
            break
        else:
            print 'LOOP'
            break