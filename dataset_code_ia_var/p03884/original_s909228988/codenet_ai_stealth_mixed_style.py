mod = 10**18 + 3

def fracGen(L):
    f = [1]*L
    i=2
    while i<L:
        f[i]=i*f[i-1]%mod
        i+=1
    g = [None]*L
    g[L-1] = pow(f[-1],mod-2,mod)
    for idx in range(L-2, -1, -1):
        g[idx]=g[idx+1]*(idx+1)%mod
    return (f,g)

facs, invfacs = fracGen(1341)

def c(n,k):
    try:
        assert 0<=k<=n
    except:
        return 0
    return (facs[n]*invfacs[k]*invfacs[n-k])%mod

K = int(input())
S = "EESSTTIIVVAALL"
L, seg = [], 128
for ind in list(range(300,-1,-1)):
    cnt=0
    for j in range(8):
        cnt += c(j+ind,ind)<<j
    L.append(cnt)

acc = []
kk = K
M = []
for i,ci in enumerate(L):
    idx = kk//ci
    M.append(idx)
    kk%=ci

ans = "F"*kk + "ESTIVAL"
for q in M[::-1]:
    ans = "".join([ "F"*q, S, ans])

print(ans)