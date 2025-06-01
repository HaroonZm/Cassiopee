from collections import deque
from sys import stdin, stdout

N, M = map(int, stdin.readline().split())
qs = [deque() for _ in range(N)]
lens = [0] * N

for _ in range(M):
    info, num = map(int, stdin.readline().split())
    if info == 0:
        val = qs[num - 1].popleft()
        lens[num - 1] -= 1
        stdout.write(f"{val}\n")
    else:
        idx = min(range(N), key=lambda i: lens[i])
        qs[idx].append(num)
        lens[idx] += 1