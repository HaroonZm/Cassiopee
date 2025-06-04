def raySW(x, y):
    return x - y

n, w, d = map(int, input().split())

def toRange(xyf):
    sx, sy, f = xyf
    x = int(sx)
    y = int(sy)
    if f == 'S':
        s = raySW(x, y)
        t = w - raySW(w - x, y)
        return (s, t)
    if f == 'E':
        s = w - raySW(w - x, y)
        t = w + d + raySW(w - x, d - y)
        return (s, t)
    if f == 'N':
        s = w + d + raySW(w - x, d - y)
        t = w + d + w - raySW(x, d - y)
        return (s, t)
    if f == 'W':
        s = w + d + w - raySW(x, d - y)
        t = w + d + w + d + raySW(x, y)
        return (s, t) if t <= w + d + w + d else (s - w - w - d - d, t - w - w - d - d)
    exit(-1)

xyfs = [input().split() for _ in range(n)]

def swap(xy):
    x, y = xy
    return (y, x)

stso = list(map(swap, list(map(toRange, xyfs))))
sts = sorted(stso)

def contains(s, t, r):
    if t <= r <= s:
        return True
    if t <= r + d + d + w + w <= s:
        return True
    if t <= r - d - d - w - w <= s:
        return True
    return False

def findMin(sts):
    c = 0
    r = w + w + d + d + w + w + d + d + w + w + d + d
    for s, t in sts:
        if not contains(s, t, r):
            c += 1
            r = s
    return c

mins = [findMin(sts[i:] + sts[:i]) for i in range(n)]
print(min(mins))