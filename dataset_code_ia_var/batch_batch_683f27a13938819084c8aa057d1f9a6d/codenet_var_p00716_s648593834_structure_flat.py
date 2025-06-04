m = int(input())
for _ in range(m):
    a = int(input())
    y = int(input())
    n = int(input())
    b = []
    for i in range(n):
        t, r, c = input().split()
        r = float(r)
        c = int(c)
        if t == '0':
            o = 0
            for j in range(y):
                o += int((a - j * c) * r)
            o += a - y * c
            b.append(o)
        else:
            o = a
            for j in range(y):
                o = int(o * (1 + r)) - c
            b.append(o)
    print(max(b))