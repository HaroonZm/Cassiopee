w, h, v, t, x, y, p, q = map(int, input().split())

def count(a, b):
    res = 0
    C = v * t
    ky = 0
    while True:
        B = b + 2 * h * ky
        D = C * C - (B - y) * (B - y)
        if D < 0:
            break
        SQ = D ** 0.5 + 1e-7
        k0 = int((x - a - SQ) // (2 * w))
        k1 = int((x - a + SQ) // (2 * w))
        if k1 - k0 > 0:
            res += k1 - k0
        ky += 1
    ky = -1
    while True:
        B = b + 2 * h * ky
        D = C * C - (B - y) * (B - y)
        if D < 0:
            break
        SQ = D ** 0.5 + 1e-7
        k0 = int((x - a - SQ) // (2 * w))
        k1 = int((x - a + SQ) // (2 * w))
        if k1 - k0 > 0:
            res += k1 - k0
        ky -= 1
    return res

ans = 0
for a_val in [p, 2 * w - p]:
    for b_val in [q, 2 * h - q]:
        ans += count(a_val, b_val)
print(ans)