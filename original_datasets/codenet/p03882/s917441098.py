from math import sqrt
n = input()
P = [map(int, raw_input().split()) for i in xrange(n)]
A = [e[2] for e in P]

def dist(p, q):
    return sqrt((p[0] - q[0])**2 + (p[1] - q[1])**2)
que = []
for i in xrange(n):
    for j in xrange(i+1, n):
        que.append((dist(P[i], P[j]), i, j))
que.sort()

memo = [-1]*2**n
memo[0] = 0
def calc(state):
    if memo[state] != -1:
        return memo[state]
    res = 0
    cnt = 0
    for i in xrange(n):
        if (state >> i) & 1:
            res += A[i]
            cnt += 1
    parent = range(n)
    def root(x):
        if x != parent[x]:
            parent[x] = x = root(parent[x])
        return x
    def unite(x, y):
        px = root(x); py = root(y)
        if px < py:
            parent[py] = px
        else:
            parent[px] = py
    for d, i, j in que:
        if (state >> i) & 1 and (state >> j) & 1 and root(i) != root(j):
            unite(i, j)
            res -= d
    res /= float(cnt)
    memo[state] = res
    return res

dic = {}
for i in xrange(n):
    dic[1<<i] = A[i]
def dfs(state):
    if state in dic:
        return dic[state]

    res = calc(state)
    sub = (state - 1) & state
    while sub != 0:
        if sub <= sub ^ state:
            res = max(res, min(calc(sub ^ state), dfs(sub)))
        sub = (sub - 1) & state
    dic[state] = res
    return res
print "%.10f" % dfs(2**n-1)