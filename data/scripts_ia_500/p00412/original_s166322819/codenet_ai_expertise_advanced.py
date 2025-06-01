from sys import stdin, stdout
from collections import deque

input = stdin.readline
N, M = map(int, input().split())
L = [deque() for _ in range(N)]
ans = []

for _ in range(M):
    info, num = map(int, input().split())
    if info == 1:
        x = min(range(N), key=lambda i: len(L[i]))
        L[x].append(num)
    else:
        ans.append(L[num-1].popleft())

stdout.write('\n'.join(map(str, ans)))