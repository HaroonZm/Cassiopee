import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import deque

def dfs(v, p):
    global pos
    
    seen[v] = True
    hist.append(v)

    for nv in adj_list[v]:
        if nv==p:
            continue
        
        if seen[nv]:
            pos = nv
            return
        
        dfs(nv, v)
        
        if pos!=-1:
            return
    
    hist.pop()

N = int(input())
adj_list = [[] for _ in range(N)]

for _ in range(N):
    ui, vi = map(int, input().split())
    adj_list[ui-1].append(vi-1)
    adj_list[vi-1].append(ui-1)

seen = [False]*N
hist = deque([])
pos = -1
dfs(0, -1)
cycle = set()

while hist:
    t = hist.pop()
    cycle.add(t)
    
    if t==pos:
        break

Q = int(input())

for _ in range(Q):
    ai, bi = map(int, input().split())
    
    if ai-1 in cycle and bi-1 in cycle:
        print(2)
    else:
        print(1)