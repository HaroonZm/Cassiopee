import sys
import heapq

def dijkstra(n, adj):
    dist = [float('inf')] * (n+1)
    dist[1] = 0
    pq = [(0,1)]
    while pq:
        cd,u = heapq.heappop(pq)
        if cd > dist[u]:
            continue
        for v,w,_ in adj[u]:
            nd = cd + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq,(nd,v))
    return dist

def main():
    input=sys.stdin.readline
    while True:
        n,m,c = map(int,input().split())
        if n==0 and m==0 and c==0:
            break
        adj = [[] for _ in range(n+1)]
        edges = []
        for i in range(m):
            f,t,w = map(int,input().split())
            adj[f].append((t,w,i))
            edges.append((f,t,w))
        dist = dijkstra(n,adj)
        original = dist[n]
        # We want to reduce dist from original > c to exactly c by changing minimal edges
        # We model a graph where each edge change cost = 1, else 0
        # Also, edge weights after change must be >=0 and can be adjusted to non-negative
        # So for each edge (f,t,w), two options:
        # 1) do not change: cost w, changes 0
        # 2) if w > new_w >=0, and we want total path cost c, we can reduce some edges
        # Idea: Dijkstra on (node, change_count), store minimal distance with given changed edges
        max_changes = m
        dist2 = [[float('inf')] * (max_changes+1) for _ in range(n+1)]
        dist2[1][0] = 0
        # priority queue of (distance, changes, node)
        heap = [(0,0,1)]
        while heap:
            cd,ch,u = heapq.heappop(heap)
            if dist2[u][ch]<cd:
                continue
            if u == n and cd == c:
                print(ch)
                break
            if u == n and cd > c:
                continue
            for v,w,i_edge in adj[u]:
                # option1: no change
                nd = cd + w
                if nd <= c and nd < dist2[v][ch]:
                    dist2[v][ch] = nd
                    heapq.heappush(heap,(nd,ch,v))
                # option2: change edge cost to reduce path cost if w > 0 and ch +1 <=m
                # set edge cost = max(0, c - (cd + sum_of_rest)) but we only know cd and w now
                if ch+1<=m:
                    # we can set edge cost to c - cd if >=0 and <=w to reduce cost
                    new_w = c - cd
                    if new_w <0:
                        new_w =0
                    if new_w < w:
                        nd2 = cd + new_w
                        if nd2 <= c and nd2 < dist2[v][ch+1]:
                            dist2[v][ch+1] = nd2
                            heapq.heappush(heap,(nd2,ch+1,v))
        else:
            # no break => no exact c
            # but problem states c < original min cost, so solution must exist
            # we print minimal ch that achieve dist2[n][ch] == c
            ans = -1
            for ch in range(max_changes+1):
                if dist2[n][ch]==c:
                    ans=ch
                    break
            print(ans if ans>=0 else 0)

if __name__=="__main__":
    main()