# Demander à l'utilisateur de saisir deux entiers séparés par un espace, puis convertir ces chaînes en entiers
n, m = map(int, input().split())

# Créer une matrice carrée v de taille n x n
# Chaque élément de cette matrice est initialisé à 1 
# (c'est-à-dire, il y a une 'arête' possible entre tous les sommets, initialement)
v = [[1 for i in range(n)] for i in range(n)]

# Répéter cette boucle m fois, car il y a m paires à traiter
for i in range(m):
    # Lire deux entiers x et y sur la même ligne, séparés par un espace, et les convertir en int
    x, y = map(int, input().split())
    # Décrémenter les deux indices de 1 pour passer de la numérotation humaine (commençant à 1) à la numérotation Python (commençant à 0)
    x -= 1
    y -= 1

    # Vérifier si la valeur actuelle dans la matrice v à la position [x][y] (qui représente un lien entre x et y) est différente de 0
    if v[x][y]:
        # Désactiver le lien entre x et y en mettant v[x][y] et v[y][x] à 0
        v[x][y], v[y][x] = 0, 0

        # Parcourir toutes les colonnes/sommets possibles (de 0 à n-1)
        for j in range(n):
            # Si le lien entre x et j est désactivé (i.e. égal à 0)
            if v[x][j] == 0:
                # Désactiver le lien correspondant entre j et y, et réciproquement entre y et j
                v[j][y], v[y][j] = 0, 0

        # Répéter la même logique pour les liens de y cette fois
        for j in range(n):
            # Si le lien entre y et j est désactivé
            if v[y][j] == 0:
                # Désactiver le lien correspondant entre j et x, et réciproquement entre x et j
                v[j][x], v[x][j] = 0, 0
    else:
        # Si le lien entre x et y était déjà désactivé (v[x][y]==0)
        # Alors mettre à 0 tous les liens qui relient x ou y à n'importe quel autre sommet, dans les deux sens
        for j in range(n):
            v[j][x], v[x][j], v[j][y], v[y][j] = 0, 0, 0, 0

# La variable suivante va compter le nombre total de liens restants dans la matrice v
# On commence par sommer chaque élément de chaque ligne, puis on fait la somme totale de ces sommes
# Cela donne la somme de toutes les valeurs 1 restantes dans la matrice v (i.e. tous les liens encore possibles après traitements)
total_liens = sum(map(sum, v))

# On soustrait ensuite la somme de la diagonale principale (c'est-à-dire, v[i][i] pour tout i, qui représentent les auto-boucles des sommets, qui doivent être ignorées)
# Pour cela, on utilise une compréhension de liste qui prend v[i][i] pour chaque i entre 0 et n-1, puis on fait la somme de cette liste
auto_boucles = sum([v[i][i] for i in range(n)])

# On retire les auto-boucles du total pour ne garder que les arêtes "réelles"
total_liens -= auto_boucles

# Chaque lien dans la matrice a été compté deux fois (une fois en [x][y] et une fois en [y][x])
# On divise donc par 2 pour obtenir le nombre de liens uniques
resultat = total_liens // 2

# Enfin, on affiche le résultat final avec la fonction print
print(resultat)