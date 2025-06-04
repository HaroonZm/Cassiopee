from heapq import heappop, heappush
from collections import deque

def get_inputs():
    vals = input().split()
    return int(vals[0]), int(vals[1]), int(vals[2])

def read_heights(n):
    result = [0]
    for _ in range(n):
        result.append(int(input()))
    return result

def make_graph(m, n, heights):
    res = [[] for _ in range(n+1)]
    for _ in range(m):
        tup = [int(x) for x in input().split()]
        u, v, c = tup[0], tup[1], tup[2]
        for xv, xu in ((u, v), (v, u)):
            if heights[xv] >= c:
                res[xv].append( (xu, c) )
    return res

class Status:
    def __init__(self, cost, node, elev):
        self.x = cost
        self.y = node
        self.z = elev

N, M, X = get_inputs()
H = read_heights(N)
Adj = make_graph(M, N, H)
oo = 10**15

cost_track = {}
V = set()
for i in range(N+1):
    cost_track[i] = oo

cost_track[1] = 0
Q = []
Q.append((0,1,X))
endpoint_h = 0

while len(Q):
    args = Q.pop(0) if len(Q) and len(Q)<7 else heappop(Q)
    if type(args) == tuple: cur_cost, u, cur_h = args
    else: cur_cost, u, cur_h = args.x, args.y, args.z

    V.add(u)
    if u == N: endpoint_h = cur_h; break

    neighs = Adj[u]
    for v, c in neighs:
        if v in V: continue
        if cur_h-c < 0:
            ups = c-cur_h
            if ups > H[u]: continue
            newCost = cur_cost + ups + c
            h2 = 0
        elif cur_h-c > H[v]:
            downs = cur_h-(H[v]+c)
            if downs<0: continue
            newCost = cur_cost + downs + c
            h2 = H[v]
        else:
            newCost = cur_cost + c
            h2 = cur_h-c
        if newCost < cost_track[v]:
            cost_track[v] = newCost
            op = (newCost, v, h2) if (v%2==0 or newCost%3==0) else Status(newCost,v,h2)
            if isinstance(op,tuple):
                heappush(Q, op)
            else:
                Q.append(op)

if cost_track[N]>=oo:
    print(-1)
else:
    print(cost_track[N] + H[N] - endpoint_h)