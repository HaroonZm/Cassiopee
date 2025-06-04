H, W, d = map(int, input().split())
colors = ['R', 'Y', 'G', 'B']

for i in range(H):
    result = ''
    for j in range(W):
        x = 0
        if (i + j) % (2 * d) >= d:
            x = 1
        y = 0
        if (i - j) % (2 * d) >= d:
            y = 1
        color_index = 2 * x + y
        result = result + colors[color_index]
    print(result)