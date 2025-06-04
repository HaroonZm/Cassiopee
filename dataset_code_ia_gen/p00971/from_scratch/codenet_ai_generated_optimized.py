s=input().rstrip()
t=input().rstrip()
n,m=len(s),len(t)
next_s=[[n]*2 for _ in range(n+1)]
next_t=[[m]*2 for _ in range(m+1)]
for i in range(n-1,-1,-1):
    for c in range(2):
        next_s[i][c]=next_s[i+1][c]
    next_s[i][int(s[i])]=i
for i in range(m-1,-1,-1):
    for c in range(2):
        next_t[i][c]=next_t[i+1][c]
    next_t[i][int(t[i])]=i
from collections import deque
dq=deque()
dq.append((0,0,""))
visited=set()
visited.add((0,0))
while dq:
    i,j,p=dq.popleft()
    for c in "0","1":
        ni=next_s[i][int(c)]
        nj=next_t[j][int(c)]
        if ni==n or nj==m:
            print(p+c)
            exit()
        if (ni+1,nj+1) not in visited:
            visited.add((ni+1,nj+1))
            dq.append((ni+1,nj+1,p+c))