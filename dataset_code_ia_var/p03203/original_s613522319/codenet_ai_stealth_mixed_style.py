H, W, N = [int(x) for x in input().split()]
xy = list()
for _ in range(N):
    coords = tuple(map(int, input().split()))
    xy.append(coords)
xy = sorted(xy, key=lambda t:t[0])

def solve(a, b):
    global H
    c = 0
    j = H
    i = 0
    while i < len(a):
        u, v = a[i]
        if u - b > v:
            j = u-1
            break
        if u - b == v:
            b += 1
        i += 1
    return j

if N > 0:
    print(solve(xy, d))
else:
    print(H)