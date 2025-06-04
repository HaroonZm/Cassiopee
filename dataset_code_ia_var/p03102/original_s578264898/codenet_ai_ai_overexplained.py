# Demande à l'utilisateur de saisir trois entiers séparés par des espaces.
# Utilise la fonction input() qui retourne une chaîne de caractères.
# split() découpe la chaîne en une liste de sous-chaînes en utilisant l'espace comme séparateur.
# map(int, ...) convertit chaque sous-chaîne en entier.
# list(...) transforme l'objet map en une liste de trois entiers : n, m et c.
n, m, c = list(map(int, input().split()))

# Demande à l'utilisateur de saisir m entiers séparés par des espaces.
# Cela correspond au vecteur b qui sera multiplié à chaque ligne de la matrice a.
# Même procédé: input() capture l'entrée, split() découpe, map(int, ...) convertit, list(...) crée la liste finale.
b = list(map(int, input().split()))

# Initialise une liste vide qui contiendra toutes les sous-listes (lignes) de la matrice a.
a = []

# Boucle qui s'exécutera n fois, car il y a n lignes dans la matrice a.
for i in range(n):
    # Demande à l'utilisateur de saisir m entiers pour la i-ème ligne de la matrice.
    # Même procédé que précédemment: input(), split(), map(int, ...), list(...).
    a1 = list(map(int, input().split()))
    # Ajoute la liste a1 nouvellement créée (correspondant à une ligne de la matrice) à la liste a.
    a.append(a1)

# Initialise la variable sum à 0.
# Cette variable comptera combien de fois une certaine condition est respectée (voir plus loin).
sum = 0

# Boucle pour parcourir chaque ligne de la matrice a.
# 'i' sert d'indice pour accéder à chaque sous-liste de a.
for i in range(n):
    # Initialise la variable t à 0 pour chaque ligne.
    # t servira à accumuler le résultat d'un calcul de produit scalaire plus une constante.
    t = 0
    # Boucle pour parcourir chaque élément de la ligne i de la matrice (qui est a[i]).
    # 'j' sert d'indice pour accéder à chaque élément de la ligne.
    for j in range(m):
        # Multiplie le j-ème élément de la i-ème ligne de la matrice (a[i][j])
        # avec le j-ème élément du vecteur b, puis ajoute le résultat à t.
        t += a[i][j] * b[j]
    # Ajoute la constante c au total accumulé dans t.
    t += c
    # Vérifie si t est strictement supérieur à 0.
    if t > 0:
        # Si c'est le cas, incrémente la variable sum de 1.
        sum += 1

# Affiche la valeur finale de sum.
# Cela correspond au nombre de lignes de la matrice a pour lesquelles le calcul donne un résultat strictement positif.
print(sum)