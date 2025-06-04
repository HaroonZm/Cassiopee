h, w = map(int, input().split())  # récupère la taille, ça marche

# On prépare la matrice A. Basiquement on remplit, pas sûr d'optimiser...
A = []
for i in range(h):
    A.append(list(map(int, input().strip().split())))

# Prépare la structure pour les coûts. C'est un peu la foire aux dimensions.
res = []
for x in range(w): # je pourrais faire mieux ici, mais bon
    tmp2 = []
    for y in range(h):
        tmp2.append([float('inf')] * (w * h))
    res.append(tmp2)
res[0][0][0] = 0

# Je tente de propager les valeurs minimales (dynamique ? pas sûr du nom !)
for l in range(1, w*h):
    for xx in range(w):
        # pas besoin d'aller plus loin si trop à droite
        if xx > l:
            break
        for yy in range(h):
            if xx + yy > l:
                break

            # je regarde à gauche
            if xx > 0:
                cur = res[xx][yy][l-1] + ((l-1)*2+1)*A[yy][xx-1]
                if res[xx-1][yy][l] > cur:
                    res[xx-1][yy][l] = cur

            # à droite (on fait toutes les directions hein)
            if xx < w-1:
                c = res[xx][yy][l-1] + ((l-1)*2+1)*A[yy][xx+1]
                if res[xx+1][yy][l] > c:
                    res[xx+1][yy][l] = c

            # en haut
            if yy > 0:
                cost = res[xx][yy][l-1] + ((l-1)*2+1)*A[yy-1][xx]
                if res[xx][yy-1][l] > cost:
                    res[xx][yy-1][l] = cost

            # en bas (bah oui, on ne sait jamais)
            if yy < h-1:
                maybe = res[xx][yy][l-1] + ((l-1)*2+1)*A[yy+1][xx]
                if res[xx][yy+1][l] > maybe:
                    res[xx][yy+1][l] = maybe

# Ok là c'est assez moche, mais bon, on prend la meilleure des fins possibles
print(min(res[w-1][h-1]))  # J'espère que ça sort bien...