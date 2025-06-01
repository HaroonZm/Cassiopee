while True:
    n = int(input())
    if n == 0:
        break
    for i in range(n):
        x1, y1, z1, w1, x2, y2, z2, w2 = map(int, input().split())
        print(
            (x1 * x2 - y1 * y2 - z1 * z2 - w1 * w2),
            (x1 * y2 + x2 * y1 + z1 * w2 - z2 * w1),
            (x1 * z2 - y1 * w2 + x2 * z1 + y2 * w1),
            (x1 * w2 + y1 * z2 - y2 * z1 + x2 * w1)
        )