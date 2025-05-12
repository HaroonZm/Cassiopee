N, K = map(int, input().split())
A = list(map(int, input().split()))

if K == 0:
    print(max(A))
    exit()

def f(x):
    cnt = 0
    for i in A:
        if i % x == 0:
            cnt += i//x - 1
        else:
            cnt += i//x
    
    if cnt <= K:
        return True
    else:
        return False

A_max = max(A)
ok = 0
ng = A_max
from math import log2, ceil
while ng - ok > 1:
    mid = (ok + ng) // 2
    if f(mid):
        ng = mid
    else:
        ok = mid
print(ceil(ng))