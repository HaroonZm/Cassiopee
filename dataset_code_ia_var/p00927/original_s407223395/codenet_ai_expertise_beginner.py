import math

d, n, b = map(int, input().split())
O = []
for i in range(n):
    line = input().split()
    O.append([int(line[0]), int(line[1])])

def solve(cur_b):
    l = d / (cur_b + 1)
    idx = 0
    vx2 = 1000000000
    for i in range(cur_b + 1):
        while idx < n and O[idx][0] * (cur_b + 1) <= d * (i + 1):
            p = O[idx][0]
            h = O[idx][1]
            p = p - l * i
            possible = p * (l - p) / (2 * h)
            if possible < vx2:
                vx2 = possible
            idx = idx + 1
    if vx2 == 0:
        return 1000000000
    if l <= vx2 * 2:
        return l
    else:
        return vx2 + (l ** 2) / (4 * vx2)

res = []
for i in range(b + 1):
    val = solve(i)
    res.append(val)
ans = min(res)
print(math.sqrt(ans))