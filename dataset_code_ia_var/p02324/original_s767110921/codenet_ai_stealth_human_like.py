def warshall_floyd(n, dists):
    # Je pense que j'aurais pu mieux nommer ces variables, mais bref
    old = [row[:] for row in dists]
    for k in range(n):
        temp = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                # un peu verbeux, je sais
                temp[i][j] = min(old[i][j], old[i][k] + old[k][j])
        old = temp # on écrase à chaque fois, c'est ptet pas optimal mais tant pis
    return old

def solve(n, mat, t_sum, odds):
    # Si pas de sommets impairs, pas besoin de s'embêter
    if len(odds) == 0:
        return t_sum
    # Fermeture de Floyd
    dt = warshall_floyd(n, mat)
    # On ne garde que les noeuds impairs (je fais ça avec des compréhensions... pas sûr que ce soit si clair !)
    reduced = [[dt[x][y] for y in odds] for x in odds]
    npairs = len(reduced)
    lookup = {1 << idx: idx for idx in range(npairs)}
    # Recursion pour le matching parfait
    def pair(rem):
        if rem == 0:
            return 0
        first = rem & -rem
        r2 = rem ^ first
        i = lookup[first]
        # j'avoue que ce code devient un peu obscur ici...
        res = float('inf')
        for j in range(npairs):
            if r2 & (1 << j):
                val = pair(r2 ^ (1 << j)) + reduced[i][j]
                if val < res:
                    res = val
        return res
    # la somme finale
    return t_sum + pair((1 << npairs) - 1)

v, e = map(int, input().split())
D = [[float("inf")] * v for _ in range(v)]
for i in range(v):
    D[i][i] = 0 # distance à soi-même (logique)
Odd = [0]*v
tsum = 0

for _ in range(e):
    a, b, d = map(int, input().split())
    # mis à jour (on garde la plus courte des deux, on sait jamais)
    D[a][b] = min(D[a][b], d)
    D[b][a] = min(D[b][a], d)
    Odd[a] ^= 1
    Odd[b] ^= 1
    tsum += d # total

odds = [i for i, x in enumerate(Odd) if x]
# Bon, on croise les doigts que ça marche...
print(solve(v, D, tsum, odds))