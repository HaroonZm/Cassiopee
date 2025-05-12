import itertools

n, a, b = map(int, input().split())
x = list(map(int, input().split()))

ans = sum(min(a * abs(p - q), b) for p, q in zip(x, x[1:]))
print(ans)