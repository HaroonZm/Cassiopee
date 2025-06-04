d, n, b = map(int, input().split())
O = []
for i in range(n):
    ligne = input().split()
    O.append([int(ligne[0]), int(ligne[1])])

def solve(b):
    l = d / (b + 1)
    idx = 0
    vx2 = 10**9
    for i in range(b + 1):
        while idx < n and O[idx][0] * (b + 1) <= d * (i + 1):
            p = O[idx][0]
            h = O[idx][1]
            p -= l * i
            temp = p * (l - p) / (2 * h)
            if temp < vx2:
                vx2 = temp
            idx += 1
    if vx2 == 0:
        return 10**9
    if l <= vx2 * 2:
        return l
    return vx2 + l**2 / (4 * vx2)

ans = 10**9
for i in range(b + 1):
    res = solve(i)
    if res < ans:
        ans = res

import math
print(math.sqrt(ans))