import sys
import heapq

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def dijkstra(start, graph, n):
    # Dijkstra algorithm to find shortest distances from start to all nodes
    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    hq = [(0, start)]
    while hq:
        cd, v = heapq.heappop(hq)
        if dist[v] < cd:
            continue
        for nv, nd in graph[v]:
            ndist = cd + nd
            if dist[nv] > ndist:
                dist[nv] = ndist
                heapq.heappush(hq, (ndist, nv))
    return dist

def main():
    N, R = map(int, input().split())

    # Build the graph as adjacency list: each edge bidirectional
    graph = [[] for _ in range(N+1)]
    edges = []
    for _ in range(R):
        s, t, d = map(int, input().split())
        graph[s].append((t,d))
        graph[t].append((s,d))
        edges.append((s, t, d))

    # Step 1: For each node, run Dijkstra to get shortest paths to all others
    # But full all-pairs Dijkstra would be too heavy for N=1500 and R=3000
    # We optimize using the following approach:
    # Since all roads can be used to reach any node from any other (connected),
    # We run Dijkstra from every node to get dist matrix (N x N).
    # This is O(N * (R log N)) which should be feasible with good implementation.

    # To save memory, store distances as a list of lists
    dist = [None]*(N+1)
    for i in range(1,N+1):
        dist[i] = dijkstra(i, graph, N)

    # Step 2: Find pair (u, v) where dist[u][v] is maximal among all pairs (shortest path max)
    max_dist = -1
    candidates = []
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            if dist[i][j] > max_dist:
                max_dist = dist[i][j]
                candidates = [(i,j)]
            elif dist[i][j] == max_dist:
                candidates.append((i,j))

    # Step 3: For one of these pairs, find one shortest path (any one) between them
    # We pick the first candidate pair
    start_node, goal_node = candidates[0]

    # To reconstruct one shortest path from start_node to goal_node,
    # we use the dist array and graph edges:

    # Backtracking from goal_node to start_node while all edges on shortest path:
    # parent candidates: for each node, any neighbor that satisfies dist[start_node][node] = dist[start_node][neighbor] + weight

    path_nodes = set()
    def backtrack_path(s, g):
        # BFS from g backwards to s on shortest path edges (distances known)
        from collections import deque
        queue = deque()
        queue.append(g)
        visited = [False]*(N+1)
        visited[g] = True
        parents = [[] for _ in range(N+1)]  # to store predecessors on shortest path
        while queue:
            cur = queue.popleft()
            if cur == s:
                continue
            for nxt, cost in graph[cur]:
                # Because edges are bidirectional, we check from cur to nxt
                # but shortest path is from s to g, so sure the path from s->nxt->cur
                # So dist[s][cur] = dist[s][nxt]+cost if edge nxt->cur is on shortest path
                if dist[s][cur] == dist[s][nxt] + cost:
                    parents[cur].append(nxt)
                    if not visited[nxt]:
                        visited[nxt] = True
                        queue.append(nxt)
        return parents

    parents = backtrack_path(start_node, goal_node)

    # Collect nodes on one shortest path by DFS from goal_node to start_node through parents
    path = []
    def dfs_path(cur):
        path.append(cur)
        if cur == start_node:
            return True
        for p in parents[cur]:
            if dfs_path(p):
                return True
        path.pop()
        return False

    dfs_path(goal_node)
    # path is from goal_node to start_node reversed, reverse it
    path.reverse()
    path_set = set(path)

    # Step 4: Identify towns that are never used on *any* maximum shortest path route possible?
    # Actually we only consider the towns used in the *selected* course.
    # The problem states:
    # "町の組み合わせが複数ある場合、そのうちのどれか一つを選ぶ。" and "最短経路が複数ある場合、そのうちのどれか一つを選ぶ。"
    # So only those towns on the selected course can appear on maximum shortest paths.

    # So towns used *could* appear on the course, all others cannot.
    # Thus, towns not in path_set are never used on the route.

    not_used_towns = []
    for town in range(1, N+1):
        if town not in path_set:
            not_used_towns.append(town)

    # Print the results
    print(len(not_used_towns))
    for t in not_used_towns:
        print(t)

if __name__ == '__main__':
    main()