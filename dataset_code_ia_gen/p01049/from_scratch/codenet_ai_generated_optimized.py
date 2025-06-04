import sys
sys.setrecursionlimit(10**7)

N = int(sys.stdin.readline())
a, d = map(int, sys.stdin.readline().split())
M = int(sys.stdin.readline())

pos = list(range(N+1))  # pos[i] = position in original arithmetic sequence of element i
for _ in range(M):
    x, y, z = map(int, sys.stdin.readline().split())
    if x == 0:
        pos[y], pos[z] = pos[z], pos[y]
    else:
        pos[y] = pos[z]

K = int(sys.stdin.readline())
idx = pos[K]
print(a + (idx - 1) * d)