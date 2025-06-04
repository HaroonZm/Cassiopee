import itertools
import bisect

cubes = []
for n in range(1, 1111):
    cubes.append(n ** 3)

num = []
for n in cubes:
    for m in cubes:
        if m >= n:
            num.append(n + m)

num.sort()

while True:
    z = input()
    z = int(z)
    z_cube = z ** 3
    if z_cube == 0:
        break
    pos = bisect.bisect(num, z_cube)
    print(z_cube - num[pos - 1])