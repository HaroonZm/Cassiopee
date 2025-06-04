import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

all_vertices = set(range(1,N+1))

current = set([1])
seen = set()
steps = 0
visited_states = set()

while True:
    if current == all_vertices:
        print(steps)
        break
    current_tuple = tuple(sorted(current))
    if current_tuple in visited_states:
        print(-1)
        break
    visited_states.add(current_tuple)
    found = set()
    for v in current:
        for u in graph[v]:
            found.add(u)
    current = found
    steps += 1