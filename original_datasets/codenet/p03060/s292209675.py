N=int(input())
V=list(map(int,input().split()))
C=list(map(int,input().split()))
Ans=0
for i in range(N):
    if V[i]-C[i]>0:
        Ans+=V[i]-C[i]
print(Ans)