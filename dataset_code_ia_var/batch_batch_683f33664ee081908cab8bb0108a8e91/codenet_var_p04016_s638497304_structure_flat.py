import math

n = int(input())
s = int(input())

ans = -1

if n == s:
    ans = n + 1
else:
    found = False
    limit = math.floor(n ** 0.5) + 1
    for b in range(2, limit):
        nb = n
        res = 0
        while nb >= b:
            res += nb % b
            nb //= b
        res += nb
        if res == s:
            ans = b
            found = True
            break
    if not found:
        upper = math.ceil(n ** 0.5)
        for p in range(1, upper):
            if (n - s) % p != 0:
                continue
            b = (n - s) // p + 1
            if limit - 1 < b <= n:
                nb = n
                res = 0
                while nb >= b:
                    res += nb % b
                    nb //= b
                res += nb
                if res == s:
                    ans = b
                    break
print(ans)