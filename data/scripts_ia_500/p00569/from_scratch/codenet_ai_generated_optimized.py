import sys
input=sys.stdin.readline
N,K,L=map(int,input().split())
A=[int(input()) for _ in range(N)]
def count(x):
    res=0
    left=0
    from collections import deque
    q=deque()
    for right in range(N):
        while q and A[q[-1]]>=A[right]:
            q.pop()
        q.append(right)
        while q[0]<left:
            q.popleft()
        while right-left+1>=K:
            if A[q[0]]<=x:
                res+=right-left+1-K+1
                break
            left+=1
    return res
low,high=1,N
while low<high:
    mid=(low+high)//2
    if count(mid)>=L:
        high=mid
    else:
        low=mid+1
print(low)