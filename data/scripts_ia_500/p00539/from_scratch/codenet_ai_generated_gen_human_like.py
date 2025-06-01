import sys
import heapq

def main():
    input = sys.stdin.readline
    N, M, C = map(int, input().split())
    edges = [[] for _ in range(N+1)]
    edge_list = []
    for _ in range(M):
        A, B, D = map(int, input().split())
        edges[A].append((B, D))
        edges[B].append((A, D))
        edge_list.append((A, B, D))

    # Dijkstra to find shortest distance from node 1
    dist = [10**15] * (N+1)
    dist[1] = 0
    hq = [(0,1)]
    while hq:
        cd, v = heapq.heappop(hq)
        if dist[v] < cd:
            continue
        for nv, nd in edges[v]:
            ndist = cd + nd
            if ndist < dist[nv]:
                dist[nv] = ndist
                heapq.heappush(hq, (ndist, nv))

    # We want to find X (distance cutoff from node 1) that minimizes:
    # cost = C * X + sum of lengths of edges NOT both endpoints in {nodes with dist <= X}

    # Collect all distances, and all distinct distances
    # Those distances are candidates for X
    distinct_dists = list(set(dist[1:] ))
    distinct_dists.append(0)
    distinct_dists = list(set(dist[1:] + [0]))
    distinct_dists.sort()

    # Prepare prefix sums or process edges in order of max dist of endpoints.
    # For efficiency:
    # For each edge, max_dist = max(dist[A], dist[B])
    # If X >= max_dist --> both endpoints are within distance X -> edge removed (not repaired)
    # Else edge remains (repaired)

    max_dists = []
    for A, B, D in edge_list:
        maxd = max(dist[A], dist[B])
        max_dists.append((maxd, D))

    # Sort edges by maxd
    max_dists.sort()

    # We try each candidate X in ascending order
    # sum_d: total length of edges with max_dist > X
    # When X increases, edges with max_dist <= X get removed from sum_d
    total_length = sum(d for _, d in max_dists)
    answer = total_length  # case X=0, cost = 0 + total_length

    idx = 0
    l = len(max_dists)
    for X in distinct_dists:
        while idx < l and max_dists[idx][0] <= X:
            total_length -= max_dists[idx][1]
            idx += 1
        cost = C * X + total_length
        if cost < answer:
            answer = cost

    print(answer)

if __name__ == "__main__":
    main()