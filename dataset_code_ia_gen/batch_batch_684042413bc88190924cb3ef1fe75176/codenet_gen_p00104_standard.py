while True:
    H, W = map(int, input().split())
    if H == 0 and W == 0:
        break
    room = [input() for _ in range(H)]
    x, y = 0, 0
    visited = set()
    while True:
        if (x, y) in visited:
            print("LOOP")
            break
        visited.add((x, y))
        tile = room[y][x]
        if tile == '.':
            print(x, y)
            break
        elif tile == '>':
            x += 1
        elif tile == '<':
            x -= 1
        elif tile == '^':
            y -= 1
        elif tile == 'v':
            y += 1