# Your code here!
N,x=map(int,input().split())

A=[0]+list(map(int,input().split()))

ans=0

for i in range(N):
    temp=A[i+1]+A[i]
    ans+=max(temp-x,0)
    A[i+1]=A[i+1]-max(temp-x,0)

print(ans)