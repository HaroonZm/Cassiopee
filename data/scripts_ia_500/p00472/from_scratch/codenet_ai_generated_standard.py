n,m=map(int,input().split())
dist=[0]*(n+1)
for i in range(1,n):
    s=int(input())
    dist[i]=dist[i-1]+s
pos=1
mod=10**5
ans=0
for _ in range(m):
    a=int(input())
    new_pos=pos+a
    ans+=(abs(dist[new_pos-1]-dist[pos-1]))
    pos=new_pos
print(ans%mod)