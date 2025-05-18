import sys
from collections import Counter
from collections import deque
import heapq
import math
import fractions
import bisect
import itertools
def input(): return sys.stdin.readline().strip()
def mp(): return map(int,input().split())
def lmp(): return list(map(int,input().split()))

n=int(input())
tree=[[] for i in range(n+1)]
for i in range(n-1):
    a,b,c=mp()
    tree[a].append([a,b,c])
    tree[b].append([b,a,c])
ans=[-1]*(n+1)
ans[1]=0
que=deque()
que.append(tree[1])
while len(que):
    q=que.popleft()
    for x,y,z in q:
        if ans[y]==-1:
            ans[y]=(ans[x]+z)%2
            que.append(tree[y])
print(*ans[1:],sep="\n")