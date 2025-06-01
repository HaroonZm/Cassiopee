for i in range(int(input())):
    input()
    a = [list(input()) for _ in range(8)]
    x = int(input()) - 1
    y = int(input()) - 1
    stack = [(y, x)]
    while stack:
        cy, cx = stack.pop()
        if a[cy][cx] == '1':
            a[cy][cx] = '0'
            for dy, dx in [(-3, 0), (-2, 0), (-1, 0), (1, 0), (2, 0), (3, 0), (0, -3), (0, -2), (0, -1), (0, 1), (0, 2), (0, 3)]:
                ny, nx = cy + dy, cx + dx
                if 0 <= ny < 8 and 0 <= nx < 8 and a[ny][nx] == '1':
                    stack.append((ny, nx))
    print('Data %d:' % (i + 1))
    for row in a:
        print(''.join(row))