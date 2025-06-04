import sys

mod = 998244353
N, K = map(int, input().split())

seg = 110
lim = K+1
M = (1<<(lim*seg)) - 1
segb = (1<<seg)-1
fold = 47
tm = (1<<fold)%mod
bfilter = 0

for _ in range(lim):
    bfilter = bfilter<<seg
    bfilter = bfilter | ((1<<fold) -1)
cfilter = M ^ bfilter

Edge = [[] for _ in range(N)]
D = [0]*N
for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    a -= 1
    b -= 1
    Edge[a].append(b)
    Edge[b].append(a)

# getpar, topological_sort_tree en mode non fonctions (flat code)
N = len(Edge)
par = [0]*N
par[0] = -1
p = 0
stack = [p]
visited = set([p])
while stack:
    vn = stack.pop()
    for vf in Edge[vn]:
        if vf in visited:
            continue
        visited.add(vf)
        par[vf] = vn
        stack.append(vf)
P = par

Q = [0]
L = []
visited2 = set([0])
while Q:
    vn = Q.pop()
    L.append(vn)
    for vf in Edge[vn]:
        if vf not in visited2:
            visited2.add(vf)
            Q.append(vf)

# On réécrit modulo en ligne
dp1 = [(1<<seg)]*N
dp2 = [1]*N
for l in L[:0:-1]:
    p = P[l]
    x = dp1[p]*((dp1[l]>>seg) + dp1[l] + dp2[l])
    x = x&M
    b = x&bfilter
    c = ((x&cfilter)>>fold) * tm
    x = b+c
    b = x&bfilter
    c = ((x&cfilter)>>fold) * tm
    x = b+c
    b = x&bfilter
    c = ((x&cfilter)>>fold) * tm
    x = b+c
    dp1[p] = x

    x = dp2[p]*(dp1[l]+dp2[l])
    x = x&M
    b = x&bfilter
    c = ((x&cfilter)>>fold) * tm
    x = b+c
    b = x&bfilter
    c = ((x&cfilter)>>fold) * tm
    x = b+c
    b = x&bfilter
    c = ((x&cfilter)>>fold) * tm
    x = b+c
    dp2[p] = x

res1 = (dp1[0]>>(K*seg)) & segb
res2 = (dp2[0]>>(K*seg)) & segb
print((res1+res2)%mod)