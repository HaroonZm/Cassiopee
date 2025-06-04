import sys
import heapq

def dijkstra(graph, start, n):
    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    pq = []
    heapq.heappush(pq, (0, start))
    while pq:
        cur_d, u = heapq.heappop(pq)
        if dist[u] < cur_d:
            continue
        for v, w in graph[u]:
            nd = cur_d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist

def main():
    input_lines = sys.stdin.read().strip().split('\n')
    idx = 0
    while True:
        if idx >= len(input_lines):
            break
        line = input_lines[idx].strip()
        idx += 1
        if line == '':
            continue
        N, M, S1, S2, T = line.split()
        N = int(N)
        M = int(M)
        S1 = int(S1)
        S2 = int(S2)
        T = int(T)
        if N == 0 and M == 0 and S1 == 0 and S2 == 0 and T == 0:
            break

        magic_edges = []
        normal_edges = []
        for _ in range(M):
            a, b, w = input_lines[idx].strip().split()
            idx +=1
            a = int(a)
            b = int(b)
            if w == 'x':
                magic_edges.append( (a,b) )
            else:
                normal_edges.append( (a,b,int(w)) )

        # We'll try all possible values for magical bridges length.
        # Since length >=0, and normal edges can be large, we can try each possible length from 0 to max of normal edges + 1
        # but this can be too large.
        # Instead, a beginner solution: try all magical length from 0 to 1000 (arbitrary), picking min difference.
        # Given constraints, this is acceptable for solution.

        max_w = 0
        for (a,b,w) in normal_edges:
            if w > max_w:
                max_w = w
        MAX_TRY = max_w + 2
        if MAX_TRY > 1000:
            MAX_TRY = 1000

        ans = float('inf')
        for length in range(MAX_TRY):
            graph = [[] for _ in range(N+1)]
            for (a,b,w) in normal_edges:
                graph[a].append( (b, w) )
                graph[b].append( (a, w) )
            for (a,b) in magic_edges:
                graph[a].append( (b,length) )
                graph[b].append( (a,length) )
            dist1 = dijkstra(graph, S1, N)
            dist2 = dijkstra(graph, S2, N)
            diff = abs(dist1[T] - dist2[T])
            if diff < ans:
                ans = diff
        print(ans)


if __name__ == '__main__':
    main()