from bisect import bisect_left

N = int(input())
T = sorted(int(input()) for _ in range(N))
if N == 1:
    print(0)
else:
    y = T[-1]
    R = [d for d in range(1, int(y ** 0.5) + 1) if y % d == 0]
    R += [y // d for d in reversed(R) if d != y // d]
    ans = sum(R[bisect_left(R, t)] - t for t in T)
    print(ans)