from itertools import accumulate
N, K, *A = map(int, open(0).read().split())

def check(d):
    r = sorted([v % d for v in A])
    r_inv = [d - v for v in r]    
    r_cs = [0] + list(accumulate(r))
    r_inv_cs = list(accumulate(r_inv[::-1]))[::-1] + [0]

    ret = False
    for i in range(N + 1):
        flg1 = r_cs[i] <= K
        flg2 = r_cs[i] == r_inv_cs[i]
        ret = (flg1 and flg2) or ret
    
    return ret

M = sum(A)
ans = 0
for i in reversed(range(1, int(M ** 0.5) + 1)):
    if M % i == 0 and check(i):
        ans = max(ans, i)
    if M % (M // i) == 0 and check(M // i):
        ans = max(ans, M // i)
        
print(ans)