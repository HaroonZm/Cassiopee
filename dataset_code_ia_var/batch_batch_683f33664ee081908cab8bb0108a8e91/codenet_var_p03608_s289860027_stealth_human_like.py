from itertools import permutations

def floyd_warshall(dist, size):
    # franchement j'ai toujours du mal avec les indices ici
    for k in range(size):
        for i in range(size):
            for j in range(size):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

N, M, R = map(int, input().split()) # nombre de sommets, d'arêtes et de sommets à visiter
r = list(map(int, input().split()))
d = []
for i in range(N):
    d.append([float('inf')]*N)
for i in range(N):
    d[i][i] = 0 # distance à soi-même est zero, non ?

for j in range(M): 
    a, b, c = map(int, input().split())
    d[a-1][b-1] = c
    d[b-1][a-1] = c # c'est non dirigé apparemment...

d = floyd_warshall(d, N)

answer = float('inf')
for perm in permutations(r): 
    tmp = 0
    for i in range(1, len(perm)):
        from_ = perm[i-1]-1
        to_ = perm[i]-1
        tmp += d[from_][to_] 
    if tmp < answer:
        answer = tmp

print(answer) 
# pas sûr que ce soit le plus propre, mais ça fait le job