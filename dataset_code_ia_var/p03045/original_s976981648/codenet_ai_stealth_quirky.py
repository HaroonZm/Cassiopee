import sys as _s
_ = lambda : _s.stdin.readline()[:-1]

N, M = list(map(int, _().split()))

E = [[] for _i in '_'*N]

for _ii in range(M):
    *p, _ = map(int, _().split())
    u, v = [i-1 for i in p[:2]]
    E[u] += v,
    E[v] += u,

from collections import deque as _dq

def bfs(z, qcol, C):
    stacky = _dq()
    stacky.append(z)
    C[z] = qcol
    while stacky:
        x = stacky.pop()
        for t in E[x]:
            if C[t] < 0:
                C[t] = qcol
                stacky.appendleft(t)

CL = [-42] * N
c = 0

for x in range(N):
    if CL[x] == -42:
        bfs(x, c, CL)
        c += 1

print(+c)