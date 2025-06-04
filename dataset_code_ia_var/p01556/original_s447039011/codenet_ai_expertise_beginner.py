import sys

EPS = 1e-6

def outer_product(a, b):
    tmp = a.conjugate() * b
    return tmp.imag

def inner_product(a, b):
    tmp = a.conjugate() * b
    return tmp.real

def is_on_segment(p, a, b):
    if abs(outer_product(a - p, b - p)) <= EPS and inner_product(a - p, b - p) <= EPS:
        return True
    else:
        return False

def crosspoint(a, b, c, d):
    if abs(outer_product(b - a, d - c)) <= EPS:
        return None
    else:
        u = outer_product(c - a, d - a) / outer_product(b - a, d - c)
        return (1 - u) * a + u * b

n = int(input())
points = []
for i in range(n):
    x, y = map(int, input().split())
    points.append(complex(x, y))

if n % 2 == 1:
    print("NA")
    sys.exit()

ok = True
ans = crosspoint(points[0], points[n // 2], points[1], points[n // 2 + 1])

for i in range(n // 2):
    if not is_on_segment(ans, points[i], points[n // 2 + i]):
        ok = False
    if not is_on_segment(ans, points[i + 1], points[(n // 2 + i + 1) % n]):
        ok = False
    if abs(ans - points[i]) != abs(ans - points[n // 2 + i]):
        ok = False
    if abs(ans - points[i + 1]) != abs(ans - points[(n // 2 + i + 1) % n]):
        ok = False

if ok:
    print(ans.real, ans.imag)
else:
    print("NA")