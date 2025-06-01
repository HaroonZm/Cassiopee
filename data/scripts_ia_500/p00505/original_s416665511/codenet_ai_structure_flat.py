import sys

lines = sys.stdin.readlines()
lines = [line.split() for line in lines]

lines_int = [sorted(list(map(int, line))) for line in lines]
a = 0
b = 0
c = 0

for line in lines_int:
    if line[0] + line[1] > line[2]:
        if line[2] ** 2 == line[0] ** 2 + line[1] ** 2:
            a += 1
        elif line[2] ** 2 < line[0] ** 2 + line[1] ** 2:
            b += 1
        elif line[2] ** 2 > line[0] ** 2 + line[1] ** 2:
            c += 1
    else:
        break

print(f"{a + b + c} {a} {b} {c}")