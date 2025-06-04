import math
EPS = 10**-7

class P2():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.norm2 = (self.x**2 + self.y**2)**0.5

    def __add__(self, other):
        return P2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return P2(self.x - other.x, self.y - other.y)

    def smul(self, a):
        return P2(self.x * a, self.y * a)

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def det(self, other):
        return self.x * other.y - self.y * other.x

n, k = map(int, input().split())
p = []
c = []
for _ in range(n):
    x, y, cc = map(float, input().split())
    p.append(P2(x, y))
    c.append(cc)

dist = [[(p[i] - p[j]).norm2 for j in range(n)] for i in range(n)]

def check(r):
    r_c = tuple(r / c[i] for i in range(n))
    cand = [pi for pi in p]
    for i in range(n - 1):
        for j in range(i + 1, n):
            d_ij = p[i] - p[j]
            if dist[i][j] < r_c[i] + r_c[j] - EPS:
                x = ((r_c[j])**2 - (r_c[i])**2 + d_ij.norm2**2) / (2 * d_ij.norm2)
                h = math.sqrt(max((r_c[j])**2 - x**2, 0.0))
                v = P2(-d_ij.y, d_ij.x).smul(h / d_ij.norm2)
                dx = p[j] + d_ij.smul(x / d_ij.norm2)
                cand.append(dx + v)
                cand.append(dx - v)
    for cand_p in cand:
        cnt = 0
        for i in range(n):
            if (p[i] - cand_p).norm2 < r_c[i] + EPS:
                cnt += 1
                if cnt >= k:
                    return True
    return False

lb = 0.0
ub = 3000 * 100
while ub - lb > EPS:
    mid = (ub + lb) / 2
    if check(mid):
        ub = mid
    else:
        lb = mid

print(ub)