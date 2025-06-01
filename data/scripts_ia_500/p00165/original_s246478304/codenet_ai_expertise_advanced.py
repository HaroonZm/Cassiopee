import sys
import itertools

M = 1_000_001
p = [True, False, False] + [True]*(M-3)
for i in range(2, int(M**0.5)+1):
    if p[i]:
        p[i*i:M:i] = [False]*len(range(i*i, M, i))
cs = list(itertools.accumulate(p))

input_iter = iter(sys.stdin.read().split())
while True:
    N = int(next(input_iter))
    if N == 0:
        break
    ans = 0
    for _ in range(N):
        p_, m_ = int(next(input_iter)), int(next(input_iter))
        low = max(p_ - m_ - 1, 0)
        high = min(p_ + m_, M-1)
        x = cs[high] - cs[low]
        ans += x - 1 if x else -1
    print(ans)