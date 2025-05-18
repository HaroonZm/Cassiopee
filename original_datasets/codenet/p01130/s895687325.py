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
    N,M,s,g1,g2 = inpl()
    if N == 0 and M == 0:
        break
    else:
        lines1 = defaultdict(set)
        lines2 = defaultdict(set)
        for _ in range(M):
            x,y,c = inpl()
            x,y = x-1,y-1
            lines1[x].add((y,c))
            lines2[y].add((x,c))

        weights_s  = dijkstra(lines1,N,s-1)
        weights_b1 = dijkstra(lines2,N,g1-1)
        weights_b2 = dijkstra(lines2,N,g2-1)

        ans = INF
        for i in range(N):
            tmp = weights_s[i] + weights_b1[i] + weights_b2[i]
            ans = min(ans,tmp)
        print(ans)