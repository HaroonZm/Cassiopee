EPS = 1.0e-8

def cross_point(p1, p2):
    A = (p1.real - p2.real) / 2
    B = (p1.imag - p2.imag) / 2
    d = (A * A + B * B) ** 0.5
    if d * d > 1.0 + EPS:
        return
    h = (1 - d * d) ** 0.5
    k = h / d
    X = (p1.real + p2.real) / 2
    Y = (p1.imag + p2.imag) / 2
    cross.append(complex(X + k * B, Y - k * A))
    cross.append(complex(X - k * B, Y + k * A))

while True:
    n = int(input())
    if n == 0:
        break
    circle = []
    for i in range(n):
        x_str, y_str = input().split(',')
        x = float(x_str)
        y = float(y_str)
        circle.append(complex(x, y))
    cross = []
    for i in range(n):
        for j in range(i + 1, n):
            cross_point(circle[i], circle[j])
    ans = 0
    for point in cross:
        f = 0
        for c in circle:
            dx = c.real - point.real
            dy = c.imag - point.imag
            d = dx * dx + dy * dy
            if abs(d - 1.0) <= EPS or d < 1.0:
                f += 1
        if f > ans:
            ans = f
    if ans == 0:
        print(1)
    else:
        print(ans)