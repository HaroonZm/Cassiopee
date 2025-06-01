from sys import stdin
tri = rig = small = large = 0
for line in stdin:
    line = list(map(int, line.split()))
    line.sort()
    if line[0] + line[1] <= line[2]:
        break
    tri += 1
    if line[0] ** 2 + line[1] ** 2 == line[2] ** 2:
        rig += 1
    elif line[0] ** 2 + line[1] ** 2 < line[2] ** 2:
        large += 1
    else:
        small += 1
print(tri, rig, small, large)