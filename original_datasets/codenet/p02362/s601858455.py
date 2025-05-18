from collections import defaultdict
from collections import deque
from sys import stdin

def sp(G,R,V):
    d = {}
    INF = float('inf')
    for i in range(V):
        d[i] = INF
    d[R] = 0
    for i in range(1,V+1):
        for (u,v) in G.keys():
            if d[v] > d[u] + G[u,v]:
                d[v] = d[u] + G[u,v]
                if i == V:
                    return 'NEGATIVE CYCLE'
    return d

V, E, R = [int(x) for x in stdin.readline().split()]
G = defaultdict()
for case in range(E):
    s, t, w = [int(x) for x in stdin.readline().split()]
    G[(s,t)] = w
d = sp(G, R, V)
if d == 'NEGATIVE CYCLE':
    print('NEGATIVE CYCLE')
else:
    for k in range(V):
        if d[k] == float('inf'):
            print("INF")
        else:
            print(d[k])