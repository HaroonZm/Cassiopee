import sys
input=sys.stdin.readline
N=int(input())
arts=[tuple(map(int,input().split())) for _ in range(N)]
arts.sort(key=lambda x:x[0])
res=-10**18
s=0
l=0
for r in range(N):
    s+=arts[r][1]
    while arts[r][0]-arts[l][0]>s:
        s-=arts[l][1]
        l+=1
    res=max(res,s-(arts[r][0]-arts[l][0]))
print(res)