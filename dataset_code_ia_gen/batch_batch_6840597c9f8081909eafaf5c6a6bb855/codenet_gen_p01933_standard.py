import sys
sys.setrecursionlimit(10**7)
input=lambda:sys.stdin.readline()

N,K=map(int,input().split())
A=[int(input()) for _ in range(N)]

children=[[] for _ in range(N+1)]
for i,a in enumerate(A,1):
    if a>0:
        children[a].append(i)

no_reply_to_any = [a==0 for a in A]
no_reply_from_any = [len(children[i])==0 for i in range(1,N+1)]

displayed = set()
for i in range(1,N+1):
    if no_reply_to_any[i-1] or no_reply_from_any[i-1]:
        displayed.add(i)
        
from collections import deque
for i in range(1,N+1):
    if no_reply_from_any[i-1]:
        steps = 0
        cur = i
        while steps<K:
            if A[cur-1]==0: break
            cur = A[cur-1]
            if cur in displayed:
                break
            displayed.add(cur)
            steps+=1

print(len(displayed))