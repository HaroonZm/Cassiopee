import sys
from collections import deque
import heapq

def read_ints():
    return list(map(int, sys.stdin.readline().split()))

# Input block (procedural)
N, M, X = map(int, input().split())
height = [0]
for _ in range(N):
    h = int(sys.stdin.readline())
    height.append(h)

# Imperative + list comprehension
adj = [[] for i in range(N+1)]
edge_lines = sys.stdin.readlines()
for ll in edge_lines:
    a, b, t = (int(z) for z in ll.strip().split())
    adj[a] += [(b, t)]
    adj[b].append((a, t))

# Imperative + object-style variables
vertex_state = [float('inf')] * (N+1)
queue = []
heapq.heappush(queue, (0, 1, X))

def process_vertex():
    while len(queue):
        tmp = heapq.heappop(queue)
        (cur_time, vtx, cur_height) = tmp
        if vtx == N:
            # direct print: scripting
            print(cur_time + (height[vtx]-cur_height))
            sys.exit()
        if cur_time > vertex_state[vtx]:
            continue
        vertex_state[vtx] = cur_time
        maxh = height[vtx]
        for to_, dist_ in adj[vtx]:
            if maxh-dist_ < 0:
                continue
            nh = cur_height - dist_
            nt = cur_time + dist_
            if nh < 0:
                nt -= nh
                nh = 0
            elif nh > height[to_]:
                nt += nh - height[to_]
                nh = height[to_]
            if vertex_state[to_] > nt:
                heapq.heappush(queue, (nt, to_, nh))
    print(-1)

# OOP-mimic with function call
if __name__ == "__main__":
    process_vertex()