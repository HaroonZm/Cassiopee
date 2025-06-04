import sys
import heapq

def solve():
    input = sys.stdin.readline
    while True:
        N,M,L,K,A,H = map(int, input().split())
        if N==0 and M==0 and L==0 and K==0 and A==0 and H==0:
            break
        fsets = set(map(int, input().split())) if L>0 else set()
        fsets.add(A)
        fsets.add(H)
        graph = [[] for _ in range(N)]
        for _ in range(K):
            X,Y,T = map(int, input().split())
            graph[X].append((Y,T))
            graph[Y].append((X,T))
        # dist[node][remain] = minimum delivery time to arrive at node with remain mins of freshness
        dist = [[float('inf')]*(M+1) for _ in range(N)]
        dist[A][M] = 0
        pq = [(0,A,M)]
        while pq:
            time,node,remain = heapq.heappop(pq)
            if dist[node][remain] < time:
                continue
            if node == H:
                print(time)
                break
            for nxt,t in graph[node]:
                if t > remain:
                    continue
                new_time = time + t
                new_remain = remain - t
                if nxt in fsets and new_remain < M:
                    # refreeze for M - new_remain minutes
                    cool = M - new_remain
                    new_time += cool
                    new_remain = M
                if dist[nxt][new_remain] > new_time:
                    dist[nxt][new_remain] = new_time
                    heapq.heappush(pq, (new_time, nxt, new_remain))
        else:
            print("Help!")

if __name__ == "__main__":
    solve()