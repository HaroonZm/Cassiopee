import sys

triangles = 0
right = 0
acute = 0
obtuse = 0

for line in sys.stdin:
    parts = line.split()
    sides = []
    for part in parts:
        sides.append(int(part))
    sides.sort()
    if sides[0] + sides[1] <= sides[2]:
        break
    triangles += 1
    value = sides[0]**2 + sides[1]**2 - sides[2]**2
    if value == 0:
        right += 1
    elif value > 0:
        acute += 1
    else:
        obtuse += 1

print(triangles, right, acute, obtuse)