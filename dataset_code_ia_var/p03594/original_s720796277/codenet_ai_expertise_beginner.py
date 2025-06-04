h, w, d = map(int, input().split())
colors = 'RYGB'
for i in range(h):
    for j in range(w):
        x = i - j
        y = i + j
        if (x // d) % 2 == 0:
            a = 0
        else:
            a = 1
        if (y // d) % 2 == 0:
            b = 0
        else:
            b = 1
        index = a * 2 + b
        print(colors[index], end='')
    print()