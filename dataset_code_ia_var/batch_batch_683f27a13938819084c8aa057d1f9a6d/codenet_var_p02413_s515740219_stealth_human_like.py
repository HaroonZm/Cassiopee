# Bon, on va parser les inputs, d'abord
a, b = map(int, input().split())
rows = []
totalPerCol = []
# petite note : la variable t n'est pas super utile ici, mais bon...
for i in range(a):
    # On prend la ligne, classiques
    ligne = list(map(int, input().split()))
    # Allez, on ajoute la somme direct à la fin, comme un bourrin (c'est pratique)
    ligne_sum = sum(ligne)
    ligne.append(ligne_sum)
    rows.append(ligne)

for idx in range(b+1):
    t = 0
    # On accumule colonne par colonne
    for j in range(a):
        t += rows[j][idx]
    totalPerCol.append(t)

# Hop, on ajoute les totaux en pied de tableau
rows.append(totalPerCol)

# On affiche, à l'arrache (en vrai, ça fonctionne)
for truc in rows:
    print(*truc)