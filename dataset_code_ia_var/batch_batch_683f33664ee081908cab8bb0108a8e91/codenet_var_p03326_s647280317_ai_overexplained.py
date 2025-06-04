# Lecture de deux entiers à partir de l'entrée standard, séparés par un espace.
# Ces deux entiers sont respectivement stockés dans les variables n et m.
# n représente généralement le nombre de listes à lire, m le nombre d'éléments à sélectionner ultérieurement.
n, m = map(int, input().split())

# Création d'une liste appelée "cake" qui va contenir n éléments.
# Chaque élément de cette liste est lui-même une liste de trois entiers, obtenue en lisant une ligne de l'entrée standard,
# en la découpant avec split(), en convertissant chaque morceau en entier (map(int, ...)), puis en fabriquant une liste.
cake = [list(map(int, input().split())) for _ in range(n)]

# Création d'une liste nommée "cakes" qui va contenir 8 sous-listes vides.
# L'opération [[] for _ in range(8)] utilise une compréhension de liste pour créer 8 listes vides distinctes,
# une pour chaque combinaison de signes +/- dans les calculs qui suivent (2^3 = 8).
cakes = [[] for _ in range(8)]

# Boucle sur chaque élément "c" de la liste cake.
# Chaque "c" est une liste de 3 entiers : c[0], c[1], c[2].
for c in cake:
    # Pour chaque combinaison de signes possible sur les 3 éléments, on calcule la somme correspondante :
    # Par exemple, c[0]+c[1]+c[2], c[0]+c[1]-c[2], etc.
    # On ajoute le résultat à la sous-liste appropriée de la liste "cakes".
    cakes[0].append(c[0] + c[1] + c[2])       # Cas où tous les éléments sont additionnés positivement.
    cakes[1].append(c[0] + c[1] - c[2])       # Cas où le troisième élément est soustrait.
    cakes[2].append(c[0] - c[1] + c[2])       # Cas où le deuxième élément est soustrait.
    cakes[3].append(c[0] - c[1] - c[2])       # Cas où le deuxième et le troisième éléments sont soustraits.
    cakes[4].append(-c[0] + c[1] + c[2])      # Cas où le premier élément est soustrait.
    cakes[5].append(-c[0] + c[1] - c[2])      # Cas où le premier et le troisième éléments sont soustraits.
    cakes[6].append(-c[0] - c[1] + c[2])      # Cas où le premier et le deuxième éléments sont soustraits.
    cakes[7].append(-c[0] - c[1] - c[2])      # Cas où tous les éléments sont soustraits.

# Pour chaque sous-liste de "cakes" (il y en a 8), on trie les éléments dans l'ordre décroissant (reverse=True).
# Cela permettra d'accéder facilement aux m plus grands éléments par la suite.
for c in cakes:
    c.sort(reverse=True)

# Initialisation de la variable "ans" à 0.
# Cette variable servira à enregistrer la somme maximale trouvée.
ans = 0

# Parcours des 8 combinaisons (0 à 7) :
for i in range(8):
    # Pour chaque sous-liste cakes[i], on prend les m premiers éléments (grâce au tri).
    # sum(cakes[i][:m]) calcule la somme des m plus grands éléments.
    # On utilise max() pour conserver la plus grande somme rencontrée dans "ans".
    ans = max(ans, sum(cakes[i][:m]))

# Affichage de la valeur finale trouvée, c'est-à-dire la somme maximale possible.
print(ans)