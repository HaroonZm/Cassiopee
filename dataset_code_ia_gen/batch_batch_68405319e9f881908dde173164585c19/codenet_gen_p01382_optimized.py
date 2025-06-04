import sys
input = sys.stdin.readline

N = int(input())
a = sorted((int(input()) for _ in range(N)), reverse=True)

def can_make_triangle(x, y, z):
    return x < y + z

perimeters = []
for i in range(N - 2):
    if can_make_triangle(a[i], a[i+1], a[i+2]):
        perimeters.append(a[i] + a[i+1] + a[i+2])
        i += 2
        if len(perimeters) == 2:
            break

res = 0
if len(perimeters) >= 2:
    res = perimeters[0] + perimeters[1]
else:
    # Try to find two triangles from non-overlapping sticks greedily
    # Since we used overlapping indices above, try another approach:
    sticks = a[:]
    triangles = []
    i = 0
    while i + 2 < len(sticks):
        if can_make_triangle(sticks[i], sticks[i+1], sticks[i+2]):
            triangles.append(sticks[i] + sticks[i+1] + sticks[i+2])
            del sticks[i:i+3]
            if len(triangles) == 2:
                break
            i = 0
        else:
            i += 1
    if len(triangles) == 2:
        res = max(res, triangles[0] + triangles[1])

print(res)