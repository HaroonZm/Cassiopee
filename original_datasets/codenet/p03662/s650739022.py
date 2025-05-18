import sys
sys.setrecursionlimit(10**8)

def find_path(now, par):
    if now == n - 1:
        path.append(n - 1)
        return True
    for to in g[now]:
        if to == par: continue
        if find_path(to, now):
            path.append(now)
            return True
    return False

def dfs1(now, par, color):
    color[now] = "b"
    for to in g[now]:
        if to == par: continue
        if color[to] == "w": continue
        dfs1(to, now, color)

def dfs2(now, par, color):
    color[now] = "w"
    for to in g[now]:
        if to == par: continue
        if color[to] == "b": continue
        dfs2(to, now, color)

n = int(raw_input())
g = [[] for _ in xrange(n)]
for i in xrange(n - 1):
    a, b = map(int, raw_input().split())
    a -= 1; b -=1
    g[a].append(b)
    g[b].append(a)
path = []
find_path(0, -1)
path.reverse()
color = ["bl"] * n
color[0] = "b"
color[n - 1] = "w"
j = 1
k = len(path) - 2
for i in xrange(1, len(path) - 1):
    if i % 2 == 1:
        v = path[j]
        color[v] = "b"
        j += 1
    else:
        v = path[k]
        color[v] = "w"
        k -= 1
dfs1(0, -1, color)
dfs2(n - 1, -1, color)
cntf = 0
cnts = 0
for i in xrange(n):
    if color[i] == "b":
        cntf += 1
    else:
        cnts += 1
if cntf > cnts:
    print "Fennec"
else:
    print "Snuke"