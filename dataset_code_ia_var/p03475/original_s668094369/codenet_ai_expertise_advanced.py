import sys
import numpy as np

input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8')
sys.setrecursionlimit(1 << 25)
inf = float('inf')
mod = 10**9 + 7

n = int(input())
C, S, F = np.array([list(map(int, input().split())) for _ in range(n-1)]).T

for start in range(n-1):
    time = S[start]
    idx = start
    while idx < n-1:
        next_time = max(time, S[idx])
        if next_time % F[idx]:
            next_time += F[idx] - (next_time % F[idx])
        time = next_time + C[idx]
        idx += 1
    print(time)
print(0)