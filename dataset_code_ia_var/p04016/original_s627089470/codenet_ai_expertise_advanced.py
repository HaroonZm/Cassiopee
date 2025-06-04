from functools import lru_cache

@lru_cache(maxsize=None)
def f(b, n):
    if n < b:
        return n
    return f(b, n // b) + n % b

n, s = int(input()), int(input())

if n == s:
    print(n + 1)
    exit()

limit = int(n ** 0.5) + 2

for i in range(2, limit + 1):
    if f(i, n) == s:
        print(i)
        exit()

ans = float('inf')
for k in range(1, limit + 1):
    if n - s >= 0 and (n - s) % k == 0:
        b = (n - s) // k + 1
        if b > 1 and f(b, n) == s:
            ans = min(ans, b)

print(int(ans) if ans != float('inf') else -1)