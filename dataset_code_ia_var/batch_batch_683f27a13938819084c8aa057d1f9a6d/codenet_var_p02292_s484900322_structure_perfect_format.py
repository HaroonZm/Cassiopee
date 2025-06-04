def dot(a, b):
    return a[0] * b[0] + a[1] * b[1]

def cross(a, b):
    return a[0] * b[1] - a[1] * b[0]

def Order(a, b):
    crs = cross(a, b)
    if crs > 0:
        return "COUNTER_CLOCKWISE"
    elif crs < 0:
        return "CLOCKWISE"
    else:
        if dot(a, b) < 0:
            return "ONLINE_BACK"
        elif dot(a, a) < dot(b, b):
            return "ONLINE_FRONT"
        else:
            return "ON_SEGMENT"

x0, y0, x1, y1 = [int(i) for i in input().split()]
a = [x1 - x0, y1 - y0]

q = int(input())
for i in range(q):
    x2, y2 = [int(i) for i in input().split()]
    b = [x2 - x0, y2 - y0]
    print(Order(a, b))