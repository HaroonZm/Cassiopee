import sys
stdin = sys.stdin
stdout = sys.stdout

def _comb(n,k,f,rf,MOD):
    return f[n]*rf[n-k]%MOD*rf[k]%MOD

MOD = pow(10,9)+7

def make_fact(n,MOD):
    fs=[1]*(n+1)
    rfs=[1]*(n+1)
    v=1
    for j in range(1,n+1):
        v *= j
        v %= MOD
        fs[j]=v
    rv=pow(fs[n],MOD-2,MOD)
    rfs[n]=rv
    for j in range(n,0,-1):
        rv *= j
        rv %= MOD
        rfs[j-1]=rv
    return fs,rfs

def main():
    line = stdin.readline
    N,M,K = list(map(int,line().split()))
    maxl = N+M+2*K

    fact,rfact = make_fact(maxl,MOD)

    F = lambda n,k: (fact[n+k] * (n-k+1) % MOD) * (rfact[k]*rfact[n+1]%MOD)%MOD

    res=0
    for q in range(K+1):
        z=K-q
        t1=_comb(N+2*q+M+2*z,N+2*q,fact,rfact,MOD)
        t2=F(N+q,q)
        t3=F(M+z,z)
        res+=t1*t2*t3%MOD
    res%=MOD
    print(res,file=stdout)

main()