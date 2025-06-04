import sys
import math
from collections import deque

def dist(a, b):
    return math.hypot(a[0]-b[0], a[1]-b[1])

def bfs(graph, start, goal):
    queue = deque([start])
    prev = {start: None}
    while queue:
        u = queue.popleft()
        if u == goal:
            path = []
            while u is not None:
                path.append(u)
                u = prev[u]
            return path[::-1]
        for v in graph[u]:
            if v not in prev:
                prev[v] = u
                queue.append(v)
    return None

input=sys.stdin.readline
while True:
    n=int(input())
    if n==0:
        break
    buildings = {}
    positions = {}
    for _ in range(n):
        b,x,y= map(int,input().split())
        buildings[b]=(x,y)
        positions[b]=(x,y)
    m=int(input())
    queries = [tuple(map(int,input().split())) for _ in range(m)]
    keys = list(buildings.keys())
    graph = {b:[] for b in keys}
    for i in range(n):
        for j in range(i+1,n):
            b1,b2 = keys[i], keys[j]
            if dist(buildings[b1], buildings[b2]) <= 50:
                graph[b1].append(b2)
                graph[b2].append(b1)
    for s,g in queries:
        path = bfs(graph,s,g)
        if path:
            print(*path)
        else:
            print("NA")