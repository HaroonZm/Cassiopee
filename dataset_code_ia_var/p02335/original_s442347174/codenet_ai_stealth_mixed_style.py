from math import factorial as f; import math

def pf(a,b,p):
    if not b: return 1
    return pf(a,b//2,p)**2 % p if b%2==0 else (a*pf(a,b-1,p))%p

def C(x, y, m):
    # Version "en bloc"
    try:
        return (f(x)*pf(f(y),m-2,m)*pf(f(x-y),m-2,m))%m if 0<=y<=x else 0
    except:
        return 0

[n,k]=[int(x)for x in input().split()]

def solve(n,k):  # procédural
    MOD = 10**9+7
    if n==0 or k==0: return 1
    else:
        return C(k,n,MOD)

Ans = None
for _ in range(1):
    Ans = solve(n,k)
print(Ans)