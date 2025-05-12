import heapq

def main():
    n,m = map(int,input().split())
    e = [[] for _ in range(n)]
    for _ in range(m):
        a,b,c = map(int,input().split())
        e[a].append([b,c])
        e[b].append([a,c])

    inf = 1000000007
    d = [inf]*n
    d[0] = 0
    visited = [False]*n
    pq = [[0,0]]
    heapq.heapify(pq)
    while pq:
        c,v = heapq.heappop(pq)
        visited[v] = True
        for u,nc in e[v]:
            if not visited[u] and nc < d[u]:
                d[u] = nc
                heapq.heappush(pq,[nc,u])

    res = 0
    for i in range(n):
        res+=d[i]
    print(res)

if __name__ == '__main__':
    main()