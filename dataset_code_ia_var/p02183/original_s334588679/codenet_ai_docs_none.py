from collections import defaultdict,deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS():return [list(x) for x in sys.stdin.readline().split()]
def S():
    res = list(sys.stdin.readline())
    if res[-1] == "\n":
        return res[:-1]
    return res
def IR(n):
    return [I() for i in range(n)]
def LIR(n):
    return [LI() for i in range(n)]
def SR(n):
    return [S() for i in range(n)]
def LSR(n):
    return [LS() for i in range(n)]

sys.setrecursionlimit(1000000)
mod = 1000000007

def solve():
    def dfs(t,j,num):
        if num == 3:
            tt = tuple([tuple(t[k]) for k in range(H)])
            d[tt] = 1
        else:
            nt = [[t[y][x] for x in range(W)] for y in range(H)]
            for y in range(H-len(s[j])+1):
                for x in range(W-len(s[j][0])+1):
                    f = 0
                    for y_ in range(len(s[j])):
                        for x_ in range(len(s[j][0])):
                            if s[j][y_][x_]:
                                Y,X = y+y_,x+x_
                                if nt[Y][X]:
                                    f = 1
                                    break
                                nt[Y][X] = 1
                        if f:
                            break
                    if f:
                        nt = [[t[y][x] for x in range(W)] for y in range(H)]
                    else:
                        nj = j+1
                        if nj == i:
                            nj += 1
                        dfs(nt,nj,num+1)
                        nt = [[t[y][x] for x in range(W)] for y in range(H)]

    s = []
    for i in range(4):
        h,w = LI()
        b = SR(h)
        s.append([[1 if b[i][j] == "#" else 0 for j in range(w)] for i in range(h)])
    H,W = 4,10
    d = defaultdict(lambda : 0)
    for i in range(4):
        t = [[0]*W for i in range(H)]
        j = 0 if i > 0 else 1
        dfs(t,j,0)
    n = I()
    for i in range(n):
        b = SR(H)
        t = tuple([tuple([0 if b[i][j] == "#" else 1 for j in range(W)]) for i in range(H)])
        if d[t]:
            print("Yes")
        else:
            print("No")
    return

if __name__ == "__main__":
    solve()