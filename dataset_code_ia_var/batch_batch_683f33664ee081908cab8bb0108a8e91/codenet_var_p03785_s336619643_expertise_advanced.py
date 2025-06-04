from heapq import heapify, heappop
from itertools import islice

N, C, K = map(int, input().split())
l = [int(input()) for _ in range(N)]
l.sort(reverse=True)
ans = 0
idx = N - 1

while idx >= 0:
    h = l[idx]
    cnt = 1
    while cnt < C and idx - cnt >= 0 and l[idx] - l[idx - cnt] <= K:
        cnt += 1
    idx -= cnt
    ans += 1

print(ans)