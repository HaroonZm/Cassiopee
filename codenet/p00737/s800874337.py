from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,copy,time
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp(): return int(input())
def inpl(): return list(map(int, input().split()))
def inpl_str(): return list(input().split())

def cal(x,y,a):
    return (x+y*W)*4 + a

def uncal(val):
    a = val%4
    vxy = val//4
    x,y = vxy%W, vxy//W
    return x,y,a

def dijkstra(lines,N,s):
    weight = [INF]*N
    weight[s] = 0
    def search(s,w_0,q,weight):
        for t,w in lines[s]:
            w += w_0
            if weight[t] > w:
                heapq.heappush(q,[w,t])
                weight[t] = w
    q = [[0,s]]
    heapq.heapify(q)
    while q:
        w,n = heapq.heappop(q)
        search(n,w,q,weight)
    return weight

while True:
    W,H = inpl()
    if W==0 and H==0:
        break

    ss = [inpl() for _ in range(H)]
    cc = inpl() # 直進，右折，反転，左折

    dx = [0,1,0,-1]
    dy = [-1,0,1,0]
    lines = defaultdict(set)
    for x in range(W):
        for y in range(H):
            for a in range(4): # 向いてる方向
                s = cal(x,y,a)
                costs = cc[:]
                if ss[y][x] <= 3:
                    costs[ss[y][x]] = 0

                for st in range(4): # 進む向き (直進，右折，反転，左折)
                    ar = (a + st)%4
                    tx,ty = x+dx[ar],y+dy[ar]
                    if (0<=tx<W) and (0<=ty<H):
                        t = cal(tx,ty,ar)
                        lines[s].add((t,costs[st]))

    weights = dijkstra(lines,H*W*4,cal(0,0,1))
    #for y in range(H):
    #    for x in range(W):
    #        print(x,y,weights[cal(x,y,0):cal(x,y,3)+1])

    print(min(weights[cal(x,y,0):cal(x,y,3)+1]))