H, W, d = map(int, input().split())

colors = 'RYGB'
for i in range(H):
    for j in range(W):
        x = i - j
        y = i + j
        print(colors[(x // d % 2) * 2 + (y // d % 2)], end='')
    print()