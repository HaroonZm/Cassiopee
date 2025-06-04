# Lecture de trois entiers séparés par des espaces depuis l'entrée standard
# map(int, input().split()) : 
#   - input() lit une ligne de texte saisie par l'utilisateur
#   - split() sépare la chaîne en une liste de chaînes selon les espaces
#   - map(int, ...) convertit chaque chaîne en un entier
#   - Les trois premiers entiers lus sont stockés dans n, h, et w respectivement
n, h, w = map(int, input().split())

# Lecture d'une autre ligne d'entiers qui sera transformée en une liste d'entiers
# x contiendra n entiers représentant les déplacements pour chaque ligne
x = list(map(int, input().split()))

# Calcul du nombre total de cases sur toute la largeur (toutes les lignes confondues)
# n est le nombre de lignes, w la largeur de chaque ligne, donc n*w est le total de cases "wide"
wide_total = n * w

# Création d'une liste booléenne de taille wide_total, initialement à False
# Chaque élément représente si la case correspondante est "couverte" ou non
wide_cover = [False] * wide_total

# Boucle sur chaque ligne (de 0 à n-1)
for i in range(n):
    # Vérifie si l'indice de la ligne (i+1) est impair
    # (i+1)%2==1 signifie que la ligne est considérée impaire en numérotation humaine (commence à 1)
    if (i + 1) % 2 == 1:
        # Parcourt les indices correspondant à la largeur w sur cette ligne,
        # décalés de x[i] vers la droite : début à i * w + x[i]
        # L'intervalle va de (i*w + x[i]) inclus à (i*w + x[i] + w) exclus
        for j in range(i * w + x[i], i * w + x[i] + w):
            # Marque la case j comme couverte (True)
            wide_cover[j] = True
    else:
        # Sinon, pour les lignes paires, décale de x[i] vers la gauche : début à i * w - x[i]
        # L'intervalle va de (i*w - x[i]) inclus à (i*w - x[i] + w) exclus
        for j in range(i * w - x[i], i * w - x[i] + w):
            # Marque la case j comme couverte
            wide_cover[j] = True

# Compteur pour compter le nombre de cases non couvertes
cnt = 0

# Parcourt chaque valeur booléenne de wide_cover
for c in wide_cover:
    # Si la case n'a pas été couverte (c est False)
    if c == False:
        # Incrémente le compteur de cases non couvertes
        cnt += 1

# Multiplie le nombre de cases non couvertes par h (la "hauteur", probablement liée à une dimension verticale)
# Affiche le résultat final
print(cnt * h)