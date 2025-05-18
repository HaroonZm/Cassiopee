import sys
readline = sys.stdin.readline

inf = 10**18+3
def merge(d1a, d2a, d1b, d2b):
    la = len(d1a)
    lb = len(d1b)
    k = la+lb
    res1 = [inf]*k
    res2 = [inf]*k
    for i in range(la):
        for j in range(lb):
            res1[i+j] = min(res1[i+j], d1a[i]+d1b[j], d1a[i]+d2b[j], d2a[i]+d1b[j])
            res2[i+j] = min(res2[i+j], d2a[i]+d2b[j])
    
    for j in range(lb):
        if d1b[j] < 0 or d2b[j] < inf:
            for i in range(la):
                res1[i+j+1] = min(res1[i+j+1], d1a[i])
                res2[i+j+1] = min(res2[i+j+1], d2a[i])
    return res1, res2

def parorder(Edge, p):
    N = len(Edge)
    par = [0]*N
    par[p] = -1
    stack = [p]
    order = []
    visited = set([p])
    ast = stack.append
    apo = order.append
    while stack:
        vn = stack.pop()
        apo(vn)
        for vf in Edge[vn]:
            if vf in visited:
                continue
            visited.add(vf)
            par[vf] = vn
            ast(vf)
    return par, order

def getcld(p):
    res = [[] for _ in range(len(p))]
    for i, v in enumerate(p[1:], 1):
        res[v].append(i)
    return res

N = int(readline())
A = list(map(int, readline().split()))
Edge = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, readline().split())
    a -= 1
    b -= 1
    Edge[a].append(b)
    Edge[b].append(a)

P, L = parorder(Edge, 0)
#C = getcld(P)

dp1 = [[A[i] if A[i] < 0 else inf] for i in range(N)]
dp2 = [[A[i] if A[i] > 0 else inf] for i in range(N)]

for l in L[:0:-1]:
    p = P[l]
    dp1[p], dp2[p] = merge(dp1[p], dp2[p], dp1[l], dp2[l])
    
    
ans = N-1
for i in range(N):
    if dp1[0][i] < 0 or dp2[0][i] < inf:
        ans = i
        break
print(ans)