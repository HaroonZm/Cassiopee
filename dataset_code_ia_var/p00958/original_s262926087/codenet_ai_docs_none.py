from collections import defaultdict
from collections import deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
def LI(): return list(map(int, sys.stdin.readline().split()))
def I(): return int(sys.stdin.readline())
def LS():return list(map(list, sys.stdin.readline().split()))
def S(): return list(sys.stdin.readline())[:-1]
def IR(n):
    l = [None for i in range(n)]
    for i in range(n):l[i] = I()
    return l
def LIR(n):
    l = [None for i in range(n)]
    for i in range(n):l[i] = LI()
    return l
def SR(n):
    l = [None for i in range(n)]
    for i in range(n):l[i] = S()
    return l
def LSR(n):
    l = [None for i in range(n)]
    for i in range(n):l[i] = LS()
    return l
sys.setrecursionlimit(1000000)
mod = 1000000007

def A():
    n,k = LI()
    ans = 0
    for l in range(1,n+1):
        for i in range(1000):
            if i*k > l:break
            j = l-i*k+i
            if j%2:
                j //= 2
                j += 1
                s = 1
                for a in range(i):
                    s *= j-a
                    s //= a+1
                ans += s
    print(ans)
    return

def dfs(d,k,f,n,nu,v,e):
    global ans
    if d == nu:
        l = defaultdict(int)
        for i in k:
            l[i] += 1
        res = 0
        for i in l.values():
            res += calc(i)
        if res > ans:
            ans = res
    else:
        for i in range(n):
            if f[i]:
                p = i
                break
        f_ = [f[i] if i != p else 0 for i in range(n)]
        for q in range(p+1,n):
            if f[q]:
                m = e[(p,q)]
                k_ = [k[i] if i != d else m for i in range(nu)]
                f__ = [f_[i] if i != q else 0 for i in range(n)]
                dfs(d+1,k_,f__,n,nu,v,e)

def calc(n):
    return n*(n-1)//2

def gcd(a,b):
    if a == 0:
        return b
    return gcd(b%a,a)
ans = 0
def B():
    n = I()
    nu = n//2
    v = LIR(n)
    v.sort()
    e = defaultdict(set)
    for p in range(n):
        for q in range(p+1,n):
            x,y = v[q][0]-v[p][0],v[q][1]-v[p][1]
            if x == 0:
                if y < 0:
                    m = (0,-1)
                else:
                    m = (0,1)
            elif y == 0:
                m = (1,0)
            else:
                g = gcd(x,abs(y))
                m = (x//g,y//g)
            e[(p,q)] = m
    f = [1 for i in range(n)]
    k = [None for i in range(n//2)]
    dfs(0,k,f,n,nu,v,e)
    print(ans)
    return

def C():
    while 1:
        n = I()
        if n == 0:
            break
        v = [input().split() for i in range(n)]
        d = defaultdict(int)
        f = [[1 for j in range(n)] for i in range(n)]
        i = 0
        s = 0
        while i < n:
            v[i][1] = int(v[i][1])
            v[i][2] = int(v[i][2])
            if v[i][2] == 0:
                s += v[i][1]
                v.pop(i)
                n -= 1
            else:
                d[v[i][0]] = i
                i += 1
        for i in range(n):
            for j in v[i][3:]:
                f[i][d[j]] = 0
        e = [[] for i in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j:continue
                if f[i][j]:
                    e[i].append(j)
        for i in e:
            print(i)
        print(ans)
    return

def D():
    n = I()
    s = [0 for i in range(100001)]
    l = LIR(n)
    l.sort(key = lambda x:x[1])
    r = [l[i][0] for i in range(n)]
    r.sort()
    f = [0 for i in range(100001)]
    for a,b in l:
        s[a] += 1
        s[b] -= 1
        f[b] += 1
    for i in range(100000):
        s[i+1] += s[i]
        f[i+1] += f[i]
    ans = 0
    for a,b in l:
        ri = bisect.bisect_left(r,b)
        ri = n-ri
        le = f[a]
        ans = max(ans,n-(ri+le))
    print(ans,max(s))
    return

def E():
    n = I()
    c = LI()
    f = [[i,c[i]] for i in range(n)]
    f.sort(key = lambda x:x[1])
    v = [[] for i in range(n)]
    m = I()
    for i in range(m):
        a,b = LI()
        a -= 1
        b -= 1
        v[a].append(b)
        v[b].append(a)
    q = deque()
    bfs_map = [1 for i in range(n)]
    ans = [0 for i in range(n)]
    for i,j in f:
        if not bfs_map[i]:continue
        q.append(i,-1)
        bfs_map[i] = 0
        ans[i] = 1
        while q:
            x,pre = q.popleft()
            for y in v[x]:
                if bfs_map[y]:
                    if x == 0:
                        bfs_map[y] = 0
                        q.append(y)
    print(sum(ans))
    return

def F():
    return

def G():
    return

def H():
    return

def I_():
    return

def J():
    return

if __name__ == "__main__":
    B()