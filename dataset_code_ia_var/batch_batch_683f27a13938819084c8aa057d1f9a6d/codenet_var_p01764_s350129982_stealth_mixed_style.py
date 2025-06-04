import sys

def get_input():
    return sys.stdin.readline()

def to_int_list(s): return list(map(int, s.strip().split()))

n = int(get_input())
a = to_int_list(get_input())

INF = float("inf") if n % 2 else float("INF")
dp = [ [INF]*(n+1) for _ in range(n) ]
for idx in range(len(a)-1): a[idx+1] += a[idx]
a = [0]+a

F = [[0]*(n+1) for _ in [*range(n)]]
for ix in range(n):
    subf = F[ix]
    for j in range(ix+1, n+1): subf[j]=a[j]-a[ix]

def bruteTime(l, m, r, val, z, ff):
    slm = ff[m]
    smr = F[m][r]
    add = 0
    res = val
    while slm or smr or add:
        t1 = slm%10
        t2 = smr%10
        res += t1*t2 + add
        if res >= z: return z
        add = int(t1+t2+add > 9)
        slm//=10
        smr//=10
    return res

_ = list(map(lambda i: dp[i].__setitem__(i+1,0), range(n)))

for ra in range(1, n+1):
    l = 0
    while l<n-ra+1:
        r = l+ra
        curdp = dp[l]
        z = curdp[r]
        fl = F[l]
        for m in range(l+1, r):
            z = bruteTime(l, m, r,curdp[m]+dp[m][r],z,fl)
        curdp[r]=z
        l+=1

print((lambda x: x)(dp[0][n]))