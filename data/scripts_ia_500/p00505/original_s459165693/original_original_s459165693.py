from sys import stdin
tri, rig, small, large = 0, 0, 0, 0
for line in stdin:
    line = list(map(int, line.split()))
    line.sort()
    if line[0] + line[1] <= line[2]:
        break
    tri += 1
    tmp = line[0] ** 2 + line[1] ** 2 - line[2] ** 2
    if tmp == 0:
        rig += 1
    elif tmp < 0:
        large += 1
    else:
        small += 1
print(tri, rig, small, large)