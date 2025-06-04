while True:
    H, W = map(int, input().split())
    if H == 0 and W == 0:
        break
    room = [input() for _ in range(H)]
    x, y = 0, 0
    visited = set()
    moves = {'>': (1, 0), '<': (-1, 0), '^': (0, -1), 'v': (0, 1)}
    while True:
        if (x, y) in visited:
            print("LOOP")
            break
        visited.add((x, y))
        tile = room[y][x]
        if tile == '.':
            print(x, y)
            break
        dx, dy = moves[tile]
        x += dx
        y += dy