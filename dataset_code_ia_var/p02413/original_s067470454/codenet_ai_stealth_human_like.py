# ok, bon, on commence par demander les dimensions
rows, cols = map(int, input().split())

# Ensuite on lit les lignes, ouais un peu bourrin mais ça fait le taf
matrice = []
for ligne in range(rows):
    # j'ai eu la flemme d'utiliser la pythonesque compréhension de liste ici
    mat = list(map(int, input().split()))
    matrice.append(mat)

# Pour chaque ligne, on ajoute la somme au bout
for i in range(rows):
    total = 0
    for j in range(cols):
        total += matrice[i][j]
    matrice[i].append(total)  # on pourrait faire sum(matrice[i]) mais bof

# Maintenant on fait les totaux de colonne (y compris la colonne d'après)
totaux_colonnes = []
for col in range(cols+1):
    s = 0
    for ligne in range(rows):
        s = s + matrice[ligne][col]
    totaux_colonnes.append(s)

# à la fin on colle les totaux des colonnes comme une nouvelle ligne
matrice.append(totaux_colonnes)

# J'affiche tout ça avec des espaces, sauf à droite (plus ou moins propre)
for i in range(rows+1):
    for j in range(cols+1):
        print(matrice[i][j], end = '' if j==cols else ' ')
    print()  # bah voilà, saut de ligne, tout marche ?