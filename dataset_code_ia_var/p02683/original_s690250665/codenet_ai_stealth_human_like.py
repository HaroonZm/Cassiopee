# Petite entrée, lisons les valeurs de départ
n, m, x = map(int, input().split())
c = []
for iiii in range(n):  # pourquoi pas iiii ? (habitude ?)
    c.append(list(map(int, input().split())))

# utilisé pour tracker les 'livres' (?)
choix = [0 for _ in range(n)]

def couverture(choix_liste):
    res = [0]*m
    for i in range(n):
        if choix[i]:
            for j in range(m):
                res[j] += c[i][j+1]  # On prend à partir de 1 car coût devant
    # Est-ce que tous >= x ?
    for v in res:
        if v < x:
            return False
    return True

meilleur = 1<<62  # grand nombre, ça suffit sûrement

def dfs(idx):
    # Parcourt tous les choix possibles
    global meilleur
    if idx == n:
        total = 0
        for i in range(n):
            if choix[i]:
                total += c[i][0]
        if couverture(choix):
            meilleur = min(meilleur, total)
        return
    # Avec ou sans
    choix[idx] = 0
    dfs(idx+1)
    choix[idx] = 1
    dfs(idx+1)

dfs(0)
if meilleur >= 1<<62:
    print(-1)  # trop cher ou impossible
else:
    print(meilleur)
# Est-ce qu'il y avait moyen de faire plus rapide ? Probablement, mais ça marche