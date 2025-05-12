# Graph I - Breadth First Search
from collections import deque
def bfs(A,d):
    dq = deque()
    dq.append(0)
    d[0] = 0
    while len(dq):
        v = dq.pop()
        for i in range(len(A[v])-1,-1,-1):
            f = A[v][i]
            if f == 1 and d[i] == -1:
                d[i] = d[v] + 1
                dq.appendleft(i)

n = int(input())
A = []
for _ in range(n):
    ss = list(map(int, input().split()))
    u = ss[0] - 1
    row = [0 for _ in range(n)]
    for i in range(ss[1]):
        idx = 2 + i
        row[ss[idx]-1] = 1
    A.append(row)

d = [-1 for _ in range(n)]
bfs(A,d)

for i,t in enumerate(d): print(i+1,t)