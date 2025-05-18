mod=1000000007
n,k=map(int,input().split())
s=int(n**0.5)
Num=[0]*(s+1)
for i in range(s,0,-1):
    Num[i]=i
    Num.append(n//i)
l=len(Num)
for i in range(1,l):
    Num[-i]=Num[-i]-Num[-i-1]
DP=[[0]*l for _ in range(k)]
DP[0]=Num[:]
for i in range(1,k):
    tmp=0
    for j in range(1,l):
        tmp+=DP[i-1][j]
        tmp%=mod
        DP[i][-j]=(tmp*Num[-j])%mod
ans=0
for i in DP[-1][1:]:
    ans+=i
    ans%=mod
print(ans)