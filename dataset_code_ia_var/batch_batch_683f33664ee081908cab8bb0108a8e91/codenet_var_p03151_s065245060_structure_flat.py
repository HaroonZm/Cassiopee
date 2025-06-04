from bisect import bisect_left

N = int(input())
A = tuple(map(int, input().split()))
B = tuple(map(int, input().split()))

surplus = []
need = 0
ans = 0

for i in range(N):
    diff = A[i] - B[i]
    if diff >= 0:
        surplus.append(diff)
    else:
        need += -diff
        ans += 1

surplus.sort(reverse=True)

cusum = [0] * (len(surplus) + 1)
i = 0
while i < len(surplus):
    cusum[i+1] = cusum[i] + surplus[i]
    i += 1

ans += bisect_left(cusum, need)
if ans > N:
    print(-1)
else:
    print(ans)