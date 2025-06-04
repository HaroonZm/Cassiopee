from functools import lru_cache

@lru_cache(maxsize=10000)
def canProd(i, m):
    if m == 0:
        return True
    if i >= n:
        return False
    return canProd(i + 1, m) or canProd(i + 1, m - a[i])

n = int(input())
a = [int(x) for x in input().split()]
q = int(input())
m = [int(x) for x in input().split()]

for i in m:
    if canProd(0, i):
        print("yes")
    else:
        print("no")