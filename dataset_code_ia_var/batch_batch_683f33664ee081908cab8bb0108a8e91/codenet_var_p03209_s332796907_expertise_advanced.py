from functools import lru_cache

N, X = map(int, input().split())

num = [1]
full = [1]
for _ in range(50):
    num.append(num[-1] << 1 | 3)
    full.append(full[-1] << 1 | 1)

@lru_cache(maxsize=None)
def f(n, x):
    if n == 0:
        return 1
    if x == 1:
        return 0
    elif x <= num[n - 1] + 1:
        return f(n - 1, x - 1)
    elif x == num[n - 1] + 2:
        return full[n - 1] + 1
    elif x >= num[n]:
        return 2 * full[n - 1] + 1
    else:
        return full[n - 1] + 1 + f(n - 1, x - 2 - num[n - 1])

print(f(N, X))