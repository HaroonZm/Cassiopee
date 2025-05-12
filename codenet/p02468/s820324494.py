import sys
sys.setrecursionlimit(10**5)

def expsq(n,k):
    global mod

    if k==0:
        return 1
    elif k%2==0:
        return pow(expsq(n,k/2),2,mod)
    else:
        return expsq(n,k-1)*n%mod

m,n=map(int,raw_input().split())
mod=10**9+7
print(expsq(m,n)%mod)