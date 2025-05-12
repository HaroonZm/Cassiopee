while True:
    n = int(input())
    if not n:
        break

    poles = [tuple(map(int, input().split())) for _ in range(n)]
    poles_set = set(poles)

    max_square = 0
    for i in range(n):
        x1, y1 = poles[i]
        for j in range(i, n):
            x2, y2 = poles[j]
            dx, dy = x2 - x1, y2 - y1
            if ((x2 + dy, y2 - dx) in poles_set and (x1 + dy, y1 - dx) in poles_set) \
                    or ((x2 - dy, y2 + dx) in poles_set and (x1 - dy, y1 + dx) in poles_set):
                edge = dx ** 2 + dy ** 2
                if max_square < edge:
                    max_square = edge
    print(max_square)