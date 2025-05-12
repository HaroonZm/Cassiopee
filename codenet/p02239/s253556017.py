n = int(input())
 
adj = [None]
for i in range(n):
    adji = list(map(int, input().split()[2:]))
    adj.append(adji)
isSearched = [None] + [False] * n
distance = [None] + [-1] * n
def BFS(u):
    d = 0
    isSearched[u] = True
    distance[u] = d
    edge = [u]
    while edge:
        q = list(edge)
        edge = []
        d += 1
        for ce in q:
            for ne in adj[ce]:
                if not isSearched[ne]:
                    isSearched[ne] = True
                    edge.append(ne)
                    distance[ne] = d
BFS(1)
for i, x in enumerate(distance[1:], start=1):
    print(i, x)