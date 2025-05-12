N,M = list(map(int, input().split()))
A = list(map(int, input().split()))

sum_a = sum(A)
ans = 0
for i,a in enumerate(A):
    if a >= sum_a / (4 * M):
        ans += 1

if ans >= M:
    print('Yes')
else:
    print('No')