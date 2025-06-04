import sys
input=sys.stdin.readline

N=int(input())
bugs=[]
for _ in range(N):
    a,b=map(int,input().split())
    bugs.append((a,b))

bugs.sort(key=lambda x:x[1])

def can(k):
    if k==0:
        return True
    selected_bugs=bugs[:k]
    selected_bugs.sort(key=lambda x:x[0])
    total_a=sum(x[0] for x in selected_bugs)
    for i in range(k):
        if total_a>selected_bugs[i][1]*k:
            return False
    return True

left,right=0,N
while left<right:
    mid=(left+right+1)//2
    if can(mid):
        left=mid
    else:
        right=mid-1
print(left)