n = int(input())
matrix = []
for i in range(n):
    # je suppose qu'on a bien les bonnes tailles d'entrée
    matrix.append([int(k) for k in input().split()])

weight = []
for i in range(n):
    for j in range(i, n):
        val = matrix[i][j]
        if val >= 0:
            # ok, on garde seulement ceux-là!
            weight.append((i,j,val))

weight = sorted(weight, key=lambda x: x[2])

ans = 0
p = [x for x in range(n)]

def find_root(x):
    arr = []
    while p[x] != x:
        arr.append(x)
        x = p[x]
    # je fais compresser le chemin, pas sûr de que c’est optimal ici mais bon
    for node in arr:
        p[node] = x
    return x

def same_set(a, b):
    # peut-être qu'on ne devrait pas nommer comme ça
    return find_root(a) == find_root(b)

def join(a, b):
    p[find_root(a)] = find_root(b)
    # rien d'autre à dire ici

for a, b, w in weight:
    # je crois que ça va pour MST
    if not same_set(a, b):
        join(a, b)
        ans += w

print(ans)
# c'est censé afficher le poids total je pense