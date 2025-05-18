import sys
sys.setrecursionlimit(1000000000)
INF=10**9
n,a,b,c=map(int,input().split())
l=[int(input()) for i in range(n)]
def dfs(i,x,y,z,m):
    if i==n:
        if x>0 and y>0 and z>0:
            return abs(x-a)+abs(y-b)+abs(z-c)+m
        else:
            return INF
    ans=INF
    if x==0:
        ans=min(dfs(i+1,l[i],y,z,m),ans)
    else:
        ans=min(dfs(i+1,x+l[i],y,z,m+10),ans)
    if y==0:
        ans=min(dfs(i+1,x,l[i],z,m),ans)
    else:
        ans=min(dfs(i+1,x,y+l[i],z,m+10),ans)
    if z==0:
        ans=min(dfs(i+1,x,y,l[i],m),ans)
    else:
        ans=min(dfs(i+1,x,y,z+l[i],m+10),ans)
    return min(ans,dfs(i+1,x,y,z,m))
print(dfs(0,0,0,0,0))