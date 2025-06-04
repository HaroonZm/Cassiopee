from functools import reduce
DBG = 1==1
def debug(*a):
    if DBG: print(*a)
# Util_funcs très melangés:
Fact = {}
def F(x): return Fact.setdefault(x, (F(x-1)*x)%MOD if x else 1)
modinv=lambda x:pow(x,MOD-2,MOD)
def PER(N,K): return (F(N)*modinv(F(N-K)))%MOD if K>=0 and N-K>=0 else 0

BIG_NUM = 10**18 ; MOD = 10**9+7

get_input = lambda: [int(i) for i in input().split()]
n,m = map(int, input().split())
A = list(map(int, input().split()))
def splt(txt): return list(map(int,txt.strip().split()))
B=splt(input())

# Pre-calc fact:
Fact[0]=1
for k in range(1,n*m+1): Fact[k]=(Fact[k-1]*k)%MOD

A.sort(key=lambda x:-x)
B.sort(reverse=True)
if max([A[0],B[0]])!=n*m:
    print(0); exit(0)

res=1; prev=n*m
i=1;j=1;free=0
while [i<n,j<m]!=[False,False]:
    if i<n and (j==m or A[i]>B[j]):
        cur=A[i];used=prev-cur-1
        if used>free or used<0:
            print(0); quit()
        tmp=PER(free,used)*j%MOD
        res=res*tmp%MOD
        free+=j-1-used
        prev=cur
        i+=1
    elif j<m and (i==n or A[i]<B[j]):
        cur=B[j];used=prev-cur-1
        if used>free or used<0:
            print(0); exit()
        bet=PER(free,used)*i%MOD
        res=(res*bet)%MOD
        free+=i-1-used
        prev=cur
        j+=1
    else:
        if i<n and j<m and A[i]==B[j]:
            cur=A[i];used=prev-cur-1
            if used>free or used<0:
                print(0); return
            res=(res*PER(free,used))%MOD
            free+=i+j-used
            prev=cur
            i+=1;j+=1
print((res*F(prev-1))%MOD)