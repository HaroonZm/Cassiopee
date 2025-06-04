import sys
input=sys.stdin.readline
N,M=map(int,input().split())
yokans=[tuple(map(int,input().split())) for _ in range(N)]
left=[0]*(N+1)
right=[0]*(N+1)
for i,(L,R) in enumerate(yokans,1):
    left[i]=max(left[i-1],R*2-L)
for i,(L,R) in enumerate(reversed(yokans),1):
    right[i]=max(right[i-1],(M-L)*2-(M-R))
right=right[::-1]
ans=10**20
for i in range(N+1):
    ans=min(ans,left[i]+right[i])
print(ans)