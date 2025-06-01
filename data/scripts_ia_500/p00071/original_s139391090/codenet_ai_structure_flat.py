explosion = [i for i in range(-3, 4) if i] + [0] * 6
for i in range(int(input())):
    input()
    field = []
    for j in range(8):
        line = input()
        row = []
        for c in line:
            row.append(int(c))
        field.append(row)
    x = int(input()) - 1
    y = int(input()) - 1
    stack = [(x, y)]
    while stack:
        cx, cy = stack.pop()
        field[cy][cx] = 0
        for idx in range(len(explosion)):
            dx = explosion[idx]
            dy = explosion[-1 - idx]
            nx = cx + dx
            ny = cy + dy
            if 0 <= nx < 8 and 0 <= ny < 8:
                if field[ny][nx] == 1:
                    stack.append((nx, ny))
                field[ny][nx] = 0
    print("Data %d:" % (i + 1))
    for row in field:
        s = ""
        for val in row:
            s += str(val)
        print(s)