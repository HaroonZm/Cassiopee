n=int(input())
t=list(map(int,input().split()))

S=sum(t)
m=int(input())
ans=[0]*m

for i in range(m):
    a,b=map(int,input().split())
    ans[i]=S+b-t[a-1]

for i in range(m):
    print(ans[i])