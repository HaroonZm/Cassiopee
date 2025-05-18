import sys
from collections import defaultdict
sys.setrecursionlimit(1000000)

def dfs(d,s,l,v,dic):
    s_ = tuple(s)
    if dic[(d,s_)] != None:
        return dic[(d,s_)]
    if d == l:
        dic[(d,s_)] = 1
        for x in s:
            if x > (n>>1):
                dic[(d,s_)] = 0
                return 0
        return 1
    else:
        res = 0
        i,j = v[d]
        if s[i] < (n>>1):
            s[i] += 1
            res += dfs(d+1,s,l,v,dic)
            s[i] -= 1
        if s[j] < (n>>1):
            s[j] += 1
            res += dfs(d+1,s,l,v,dic)
            s[j] -= 1
        dic[(d,s_)] = res
        return res

def solve(n):
    dic = defaultdict(lambda : None)
    m = int(sys.stdin.readline())
    s = [0]*n
    f = [[1]*n for i in range(n)]
    for i in range(n):
        f[i][i] = 0
    for i in range(m):
        x,y = [int(x) for x in sys.stdin.readline().split()]
        x -= 1
        y -= 1
        s[x] += 1
        f[x][y] = 0
        f[y][x] = 0
    v = []
    for i in range(n):
        for j in range(i+1,n):
            if f[i][j]:
                v.append((i,j))
    l = len(v)
    print(dfs(0,s,l,v,dic))

while 1:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    solve(n)