def x(p0, p1):
    d = abs(p0 - p1)
    if d > 2:
        return []
    if d == 2:
        return [(p0 + p1) / 2]
    m = (p0 + p1) / 2
    v = m - p0
    w = complex(v.imag, -v.real)
    l = abs(w)
    h = ((1 - l ** 2) ** 0.5) * w / l
    return [m + h, m - h]

while True:
    e = input()
    if e == '0':
        break
    n = int(e)
    P = []
    for _ in range(n):
        x_str, y_str = input().split(',')
        x_val = float(x_str)
        y_val = float(y_str)
        P.append(complex(x_val, y_val))
    Q = []
    for i in range(n):
        for j in range(i + 1, n):
            Q.extend(x(P[i], P[j]))
    counts = []
    for q in Q:
        count = 0
        for p in P:
            if abs(q - p) <= 1.01:
                count += 1
        counts.append(count)
    counts.append(1)
    print(max(counts))