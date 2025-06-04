import sys
sys.setrecursionlimit(999999)  # on pousse la limite pour pas planter la récursion

def calc(p1, p2, v):
    # On récupère vite fait les distances depuis v
    ds = dists[v]
    if v == n-1:
        # cas de base, on retourne la somme des distances
        return ds[p1] + ds[p2]
    if visited[p1][p2]:
        # déjà vu ce cas donc autant renvoyer ce qu’on a stocké
        return dp[p1][p2]
    # Quelques arrangements pour éviter de se perdre
    a = ds[p1] + calc(p2, v, v+1)
    b = ds[p2] + calc(p1, v, v+1)
    dp[p1][p2] = min(a, b)
    visited[p1][p2] = True
    return dp[p1][p2]

n = int(input())
points = []
for _ in range(n):
    # On stocke chaque point comme un complexe, c’est plus simple à manipuler après
    x, y = map(int, input().split())
    points.append(complex(x, y))

dists = []
for p in points:
    row = []
    for q in points:
        row.append(abs(p-q))
    dists.append(row)

visited = []
for i in range(n):
    visited.append([False]*n)

dp = []
for i in range(n):
    dp.append([0]*n)

# On met tout ensemble et on lance la machine...
res = calc(0, 0, 0)
print(res) # afficher le résultat, normalement c'est bon (à tester avec de vrais cas)