import sys
input=sys.stdin.readline

while True:
    line=input()
    if not line:
        break
    N,M=map(int,line.split())
    idols=[]
    for _ in range(N):
        name=input().rstrip('\n')
        C,V,D,L=map(int,input().split())
        idols.append((C,V,D,L))
    dp=[(0,0,0)]*(M+1)
    dp=[(0,0,0) for _ in range(M+1)]
    for C,V,D,L in idols:
        for cost in range(C,M+1):
            v_,d_,l_=dp[cost-C]
            nv,nl,nd=v_+V,l_+L,d_+D
            old=dp[cost]
            if max(nv,nd,nl)>max(old):
                dp[cost]=(nv,nd,nl)
    ans=max(max(v,d,l) for v,d,l in dp)
    print(ans) if ans>0 else print(0)