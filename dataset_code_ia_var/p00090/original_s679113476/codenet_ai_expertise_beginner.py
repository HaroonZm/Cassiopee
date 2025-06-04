def x(p0, p1):
    distance = abs(p0 - p1)
    if distance > 2:
        return []
    elif distance == 2:
        return [ (p0 + p1) / 2 ]
    else:
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
        s = input()
        x_str, y_str = s.split(',')
        x_f = float(x_str)
        y_f = float(y_str)
        P.append(complex(x_f, y_f))
    Q = []
    for i in range(n):
        for j in range(i + 1, n):
            results = x(P[i], P[j])
            for r in results:
                Q.append(r)
    counts = []
    for q in Q:
        count = 0
        for p in P:
            if abs(q - p) <= 1.01:
                count += 1
        counts.append(count)
    ans = 1
    if counts:
        ans = max(counts)
    print(ans)