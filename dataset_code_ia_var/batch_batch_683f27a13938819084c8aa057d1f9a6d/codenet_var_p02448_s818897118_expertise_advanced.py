from sys import stdin

n = int(stdin.readline())
P = [line.split() for line in (stdin.readline() for _ in range(n))]
for p in P:
    p[:2] = map(int, p[:2])
    p[3] = int(p[3])
P.sort()
for row in P:
    print(*row)