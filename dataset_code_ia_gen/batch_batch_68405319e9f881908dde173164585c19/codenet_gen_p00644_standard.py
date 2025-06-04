import sys
import heapq

def dijkstra(n, graph, start):
    dist = [float('inf')] * n
    dist[start] = 0
    count = [0] * n
    count[start] = 1
    heap = [(0, start)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                count[v] = count[u]
                heapq.heappush(heap, (nd, v))
            elif nd == dist[v]:
                count[v] += count[u]
    return dist, count

def main():
    input = sys.stdin.readline
    while True:
        n, m, p = map(int, input().split())
        if n == 0 and m == 0 and p == 0:
            break
        graph = [[] for _ in range(n)]
        for _ in range(m):
            u,v,w = map(int, input().split())
            graph[u].append((v,w))
            graph[v].append((u,w))
        children = [int(input()) for _ in range(p)]

        dist_start, cnt_start = dijkstra(n, graph, 0)
        dist_end, cnt_end = dijkstra(n, graph, n-1)
        total_paths = cnt_start[n-1]
        res = []
        for c in children:
            # A node c is on a shortest path if dist_start[c] + dist_end[c] == dist_start[n-1]
            # Probability that node c is on chosen path = (number of shortest paths going through c) / total_paths
            # number of shortest paths through c = cnt_start[c] * cnt_end[c] if on shortest path
            if dist_start[c] + dist_end[c] == dist_start[n-1]:
                prob = cnt_start[c] * cnt_end[c] / total_paths
            else:
                prob = 0.0
            res.append(prob)
        print('\n'.join(map(str, res))+'\n')

if __name__ == '__main__':
    main()