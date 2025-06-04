from functools import lru_cache

n, x = map(int, input().split())
j = [1]
k = [1]
for _ in range(n):
    j.append((j[-1] << 1) + 3)
    k.append((k[-1] << 1) + 1)

@lru_cache(maxsize=None)
def do(level, x):
    if x <= 0:
        return 0
    if level == 0:
        return 1
    if x == 1:
        return 0
    elif x <= 1 + j[level-1]:
        return do(level-1, x-1)
    elif x == 2 + j[level-1]:
        return k[level-1] + 1
    elif x <= j[level]:
        return k[level-1] + 1 + do(level-1, x-2-j[level-1])
    else:
        return k[level]
        
print(do(n, x))