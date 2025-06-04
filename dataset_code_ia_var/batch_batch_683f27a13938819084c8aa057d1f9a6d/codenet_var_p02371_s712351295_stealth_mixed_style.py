from heapq import *
import collections

def find_diameter(graph, n):
    vis = [0]*n
    q = []
    def bfs_beg():
        for idx in range(n):
            if graph[idx]:
                vis[idx]=1
                for w, nxt in graph[idx]:
                    heappush(q, (-w, nxt))
                return idx

    start = bfs_beg()
    curr_w = [0]
    maxv = [start]
    while len(q):
        wt, v = heappop(q)
        if not vis[v]:
            vis[v]=1
            if curr_w[0] < -wt:
                curr_w[0] = -wt
                maxv[0] = v
            for ed in graph[v]:
                if not vis[ed[1]]:
                    heappush(q, (wt-ed[0], ed[1]))

    for k in range(n): vis[k] = False

    root = maxv[0]
    vis[root] = True
    # BFS round 2, use plain queue this time
    bag = []
    for ed in graph[root]:
        heappush(bag, (-ed[0], ed[1]))
    result = 0
    pos = root
    while bag:
        item = heappop(bag)
        wt, v = item
        if not vis[v]:
            vis[v]=True
            if result < -wt:
                result = -wt
                pos = v
            for fw in graph[v]:
                if not vis[fw[1]]:
                    bag.append((wt - fw[0], fw[1]))
        # re-heapify to mix list and heap style
        heapify(bag)
    return result

def run():
    n = int(input())
    edges = [[] for _ in range(n)]
    for __ in range(n-1):
        s, t, w = [int(x) for x in input().split()]
        edges[s].append((w, t))
        edges[t].append((w, s))
    print(find_diameter(edges, n))

if __name__ == '__main__':
    run()