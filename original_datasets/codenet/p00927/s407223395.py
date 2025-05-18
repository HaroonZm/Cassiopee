import math
d, n, b = map(int, input().split())
O = [list(map(int, input().split())) for i in range(n)]

def solve(b):
    l = d / (b+1)
    idx = 0
    vx2 = 10**9
    for i in range(b+1):
        while idx < n and O[idx][0]*(b+1) <= d*(i+1):
            p, h = O[idx]
            p -= l*i
            vx2 = min(vx2, p*(l-p)/(2*h))
            idx += 1
    if vx2 == 0:
        return 10**9
    return l if l <= vx2 * 2 else vx2 + l**2 / (4*vx2)
print(math.sqrt(min(map(solve, range(b+1)))))