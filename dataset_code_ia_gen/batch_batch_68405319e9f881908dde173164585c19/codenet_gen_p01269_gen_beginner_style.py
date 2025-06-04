import sys

def main():
    input = sys.stdin.readline
    while True:
        N, M, L = map(int, input().split())
        if N == 0 and M ==0 and L ==0:
            break
        edges = [[] for _ in range(N+1)]
        for _ in range(M):
            A, B, D, E = map(int, input().split())
            edges[A].append((B, D, E))
            edges[B].append((A, D, E))

        # dist[node][cost] = minimal thief count to reach node with cost used = cost
        # Initialize with large number
        INF = 10**9
        dist = [[INF]*(L+1) for _ in range(N+1)]
        dist[1][0] = 0

        for cost in range(L+1):
            for node in range(1, N+1):
                if dist[node][cost] == INF:
                    continue
                cur_thief = dist[node][cost]
                for nxt, d, e in edges[node]:
                    # If we can use guard to protect on this road
                    if cost + d <= L:
                        if dist[nxt][cost + d] > cur_thief:
                            dist[nxt][cost + d] = cur_thief
                    # Without guard, pay thief count
                    if dist[nxt][cost] > cur_thief + e:
                        dist[nxt][cost] = cur_thief + e

        # Find minimal thief count at destination N with any cost <= L
        ans = min(dist[N])
        print(ans)

if __name__ == "__main__":
    main()