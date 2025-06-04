x0, y0, x1, y1 = map(int, input().split())
p0 = [x0, y0]
p1 = [x1, y1]
v1 = [p1[0] - p0[0], p1[1] - p0[1]]
q = int(input())

def cross(a, b):
    crs = a[0] * b[1] - a[1] * b[0]
    return crs

def dot(a, b):
    dt = a[0] * b[0] + a[1] * b[1]
    return dt

eps = 0.000001
for i in range(q):
    p2 = list(map(int, input().split()))
    v2 = [p2[0] - p0[0], p2[1] - p0[1]]
    crs = cross(v1, v2)
    dt = dot(v1, v2)
    if crs > eps:
        print("COUNTER_CLOCKWISE")
    elif crs < -eps:
        print("CLOCKWISE")
    elif dt < -eps:
        print("ONLINE_BACK")
    elif v1[0] ** 2 + v1[1] ** 2 < v2[0] ** 2 + v2[1] ** 2:
        print("ONLINE_FRONT")
    else:
        print("ON_SEGMENT")