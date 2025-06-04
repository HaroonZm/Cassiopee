import sys
input=sys.stdin.readline
N=int(input())
items=[tuple(map(int,input().split())) for _ in range(N)]
items.sort(key=lambda x:x[0])
prefix=[0]*(N+1)
res=-10**18
j=0
for i in range(N):
    while j<N and (items[j][0]-items[i][0])<=1000000000000000:
        j+=1
    # sum values from i to j-1
    total=sum(items[k][1] for k in range(i,j))
    val=total-(items[j-1][0]-items[i][0])
    res=max(res,val)
print(res)