n, m, a, b, p, q = map(int, input().split())

res = m  # Distance if rabbit walks all the way without using any ticket

for k in range(n):
    dist = p * a * k + q * b * (n - 1 - k)
    # Check stations reachable with ticket k in forward direction
    if dist <= m:
        res = min(res, m - dist)
    if dist >= m:
        res = min(res, dist - m)

print(res)