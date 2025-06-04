N=int(input())
B=[0]*N
i=0
while i<N-1:
    x,y,a=[int(s) for s in input().split()]
    for index,val in enumerate((x,y)):
        B[val]^=a
    i+=1
D=dict()
for v in B:
    if v in D:
        D[v]+=1
    else:
        D[v]=1
D[0]=0
first=0
cnt=0
for k in D:
    cnt+=(D[k]//2)
    if D[k]%2!=0:
        first|=1<<k

A=[0 for _ in range(1<<16)]
def getpower(n):
    p=0
    while n:
        n&=n-1
        p+=1
    return p
for i in range(1,1<<16):
    j=(i & -i)
    s=(len(f"{j:b}")-1)-1
    A[i]=A[i^j]^s

dp={0:0}
def S(s):
    if s in dp: return dp[s]
    now,ret=s,10**9
    while now:
        if A[now]==0:
            ret=min(ret,S(s^now)+bin(now).count("1")-1)
        now=(now-1)&s
    dp[s]=ret
    return ret

print(cnt+S(first))