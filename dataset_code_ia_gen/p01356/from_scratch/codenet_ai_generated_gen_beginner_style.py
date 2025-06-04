n, m, a, b, p, q = map(int, input().split())

min_walk = m
for k in range(n):
    dist = p * a * k + q * b * k
    walk = abs(m - dist)
    if walk < min_walk:
        min_walk = walk

print(min_walk)