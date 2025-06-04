# Demander à l'utilisateur d'entrer un entier, qui sera la taille de la liste S
n = int(input()) # n stocke le nombre d'éléments dans S

# Demander à l'utilisateur d'entrer une suite d'entiers séparés par des espaces, ces entiers sont lus comme une seule chaîne de caractères
S = input().split() # split() sépare la chaîne en une liste de chaînes selon les espaces

# Parcourir chaque chaîne de la liste S et la convertir explicitement en entier, stockant le résultat dans une nouvelle liste S
S = [int(s) for s in S] # Utilisation d'une list comprehension pour convertir chaque élément en int

# Demander à l'utilisateur d'entrer un entier, qui sera le nombre d'éléments dans la liste T
q = int(input())

# Demander à l'utilisateur une séquence d'entiers séparés par des espaces, qui sera convertie en une liste de chaînes
T = input().split()

# Parcourir chaque chaîne de la liste T et la convertir explicitement en entier, stockant le résultat dans une nouvelle liste T
T = [int(t) for t in T]

# Définition d'une fonction de recherche linéaire qui cherche un élément 'key' dans la liste S
# Cette fonction retourne 1 si 'key' est trouvé dans la liste S, 0 sinon
def lineresearch(key):
    # Déclaration d'une variable entière i, initialisée à zéro, pour servir d'indice de parcours de la liste S
    i = 0
    # La boucle while continue tant que l'élément à l'index i de S n'est pas égal à la clé recherchée
    while S[i] != key:
        # Incrémenter i de 1 à chaque itération pour avancer dans la liste S
        i = i + 1
        # Vérifie si l'indice i est égal à n (longueur initiale de S)
        if i == n:
            # Si oui, cela signifie qu'on a atteint la fin de la partie utile de S sans trouver la clé
            # Retourner 0 pour indiquer que la clé n'a pas été trouvée
            return 0
    # Si la boucle se termine parce que S[i] == key, retourner 1 pour indiquer que la clé a été trouvée
    return 1

# Initialiser le compteur de résultats, c'est-à-dire le nombre de fois où des éléments de T sont trouvés dans S
count = 0

# Boucle sur tous les indices de 0 à q-1, traitant chaque élément de T à la fois
for i in range(q):
    # Ajouter un élément arbitraire (ici 0) à la fin de la liste S pour s'assurer que S soit assez grand
    S.append(0)
    # Remplacer le dernier élément ajouté dans S par la valeur actuelle de T (c'est la technique du sentinelle)
    S[n] = T[i]  # Met à jour l'élément à l'indice n (qui était initialement hors de S, maintenant nouveau)
    # Appeler la fonction de recherche linéaire sur la nouvelle valeur ajoutée (sentinelle T[i])
    # Ajouter le résultat (0 ou 1) au compteur count
    count += lineresearch(S[n])
# Afficher la valeur finale de count qui correspond au nombre d'éléments de T trouvés dans S
print(count)