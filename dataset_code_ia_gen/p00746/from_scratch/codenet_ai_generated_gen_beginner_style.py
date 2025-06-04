while True:
    N = int(input())
    if N == 0:
        break
    positions = {}
    positions[0] = (0, 0)  # first square at origin
    for i in range(1, N):
        line = input().split()
        n_i = int(line[0])
        d_i = int(line[1])
        x, y = positions[n_i]
        if d_i == 0:  # left
            positions[i] = (x - 1, y)
        elif d_i == 1:  # down
            positions[i] = (x, y - 1)
        elif d_i == 2:  # right
            positions[i] = (x + 1, y)
        elif d_i == 3:  # up
            positions[i] = (x, y + 1)
    xs = [pos[0] for pos in positions.values()]
    ys = [pos[1] for pos in positions.values()]
    width = max(xs) - min(xs) + 1
    height = max(ys) - min(ys) + 1
    print(width, height)