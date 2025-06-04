n = int(input())
t_points = [tuple(map(float, input().split())) for _ in range(n)]
pts = []
for re, im in t_points:
    pts.append(complex(re, im))
pts.append(pts[0])

def cross(a, b):
    return (a.real * b.imag - a.imag * b.real)

diff = lambda idx: pts[idx+1] - pts[idx]

min_idx = 0
for idx in range(n):
    if t_points[idx] < t_points[min_idx]:
        min_idx = idx

max_idx = 0
for idx in range(n):
    if t_points[idx] > t_points[max_idx]:
        max_idx = idx

def dist(i, j):
    return abs(pts[i] - pts[j])

i = min_idx
j = max_idx
d = dist(i, j)

ii, jj = i, j
while 1:
    val = cross(diff(ii), diff(jj))
    if val >= 0:
        jt2 = (jj + 1) % n
        jj = jt2
    else:
        ii = (ii + 1) % n
    d = max(d, dist(ii, jj))
    if ii == i and jj == j:
        break

print(d)