from sys import stdin
def side(a, b, c):
    return ((c[1]-a[1])*(b[0]-a[0])-(b[1]-a[1])*(c[0]-a[0])) > 0
def is_inner(x):
    s = side(p0, p1, x)
    return s == side(p1, p2, x) == side(p2, p0, x)

input_iter = iter(stdin.read().split())
for _ in range(int(next(input_iter))):
    coords = list(map(int, (next(input_iter) for _ in range(10))))
    p0, p1, p2 = coords[:2], coords[2:4], coords[4:6]
    x1, x2 = coords[6:8], coords[8:10]
    print("NG" if is_inner(x1) == is_inner(x2) else "OK")