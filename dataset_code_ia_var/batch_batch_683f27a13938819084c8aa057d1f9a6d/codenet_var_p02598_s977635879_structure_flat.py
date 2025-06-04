N, K = map(int, input().split())
A = list(map(int, input().split()))

if K == 0:
    print(max(A))
    exit()

A_max = max(A)
ok = 0
ng = A_max

from math import ceil

while ng - ok > 1:
    mid = (ok + ng) // 2
    cnt = 0
    for i in A:
        if i % mid == 0:
            cnt += i // mid - 1
        else:
            cnt += i // mid
    if cnt <= K:
        ng = mid
    else:
        ok = mid

print(ceil(ng))