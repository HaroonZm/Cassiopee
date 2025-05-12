from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,copy,time
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp(): return int(input())
def inpl(): return list(map(int, input().split()))
def inpl_str(): return list(input().split())

def dfs(x,y,s,c):
    global tmpp
    if not(0<=x<W and 0<=y<H):
        return
    elif tmpp[y][x] != s:
        return
    else:
        tmpp[y][x] = c
        dfs(x+1,y,s,c)
        dfs(x-1,y,s,c)
        dfs(x,y+1,s,c)
        dfs(x,y-1,s,c)

def calc(x,y):
    global tmpp
    if not(0<=x<W and 0<=y<H):
        return 0
    elif tmpp[y][x] != C:
        return 0
    else:
        tmpp[y][x] = -1
        return calc(x+1,y) + calc(x-1,y) + calc(x,y+1) + calc(x,y-1) + 1

while True:
    H,W,C = inpl()
    if H == 0:
        break
    pp = [inpl() for _ in range(H)]
    ans = 0

    for arg in itertools.product(range(1,7),repeat=4):
        colors = list(arg) + [C]
        tmpp = [p[:] for p in pp]
        for c in colors:
            if tmpp[0][0] == c:
                continue
            else:
                dfs(0,0,tmpp[0][0],c)

        ans = max(calc(0,0),ans)

    print(ans)