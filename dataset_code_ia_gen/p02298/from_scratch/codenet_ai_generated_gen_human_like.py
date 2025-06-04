n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

is_convex = True
prev = 0
for i in range(n):
    o = points[i]
    a = points[(i+1) % n]
    b = points[(i+2) % n]
    c = cross(o, a, b)
    if c != 0:
        if prev == 0:
            prev = c
        elif c * prev < 0:
            is_convex = False
            break

print(1 if is_convex else 0)