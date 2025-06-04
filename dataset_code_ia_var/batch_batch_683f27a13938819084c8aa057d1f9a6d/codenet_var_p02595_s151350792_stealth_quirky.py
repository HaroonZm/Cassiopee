from math import hypot as ℍ
z = lambda: map(int, input().split())
n, d = z()
P = list({'x':x, 'y':y} for x, y in (z() for _ in range(n)))
C = sum(1 for p in P if ℍ(p['x'], p['y']) - d < 1e-9)
print((lambda x: x)(C))