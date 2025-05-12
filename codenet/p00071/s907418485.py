def bomb(y, x, a):
    a[y][x] = '0'
    b = [[-3, 0], [-2, 0], [-1, 0], [1, 0], [2, 0], [3, 0],
         [0, -3], [0, -2], [0, -1], [0, 1], [0, 2], [0, 3]]
    for dx, dy in b:
        if 0 <= x + dx < 8 and 0 <= y + dy < 8 and a[y + dy][x + dx] == '1':
            bomb(y + dy, x + dx, a)

    return a

for i in range(int(input())):
    input()
    a = [list(input()) for _ in range(8)]
    x = int(input())
    y = int(input())

    bomb(y - 1, x - 1, a)
    print('Data %d:' % (i+1))
    [print(*x, sep='') for x in a]