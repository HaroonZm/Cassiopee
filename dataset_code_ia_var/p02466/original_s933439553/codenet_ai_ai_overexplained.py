# Demande à l'utilisateur de saisir un nombre entier et le convertit depuis une chaîne de caractères vers un entier avec 'int'
n = int(input())  # nombre d'éléments dans la première liste

# Demande à l'utilisateur de saisir une ligne de nombres séparés par des espaces, scinde la chaîne en une liste de chaînes
# puis utilise 'map' pour convertir chaque élément de la liste en un entier, et enfin 'list' pour créer une liste d'entiers
alist = list(map(int, input().split()))  # première liste d'entiers

# Demande à l'utilisateur de saisir un nombre entier et le convertit en entier, tout comme la première entrée
m = int(input())  # nombre d'éléments dans la deuxième liste

# Demande à l'utilisateur de saisir une ligne de nombres séparés par des espaces, scinde la chaîne, puis convertit chaque valeur en entier, et crée la liste
blist = list(map(int, input().split()))  # deuxième liste d'entiers

# Convertit la première liste 'alist' en ensemble (set) pour ne garder que les éléments uniques (car un set ne contient pas de doublons)
# Idem pour la deuxième liste 'blist'
# L'opérateur '^' (symmetric difference) entre deux ensembles retourne un nouvel ensemble avec les éléments présents
# dans l'un OU l'autre, mais pas dans les deux (c'est-à-dire l'union des différences de chaque côté)
anslist = set(alist) ^ set(blist)  # éléments uniques à chaque liste, sans les éléments communs

# Convertit l'ensemble résultat 'anslist' en liste (car on ne peut pas trier un ensemble directement)
anslist = list(anslist)

# Trie la liste 'anslist' dans l'ordre croissant, car le tri rend la sortie plus lisible et ordonnée
anslist.sort()

# Parcourt chaque élément de la liste triée 'anslist' un par un, en commençant au début et en finissant à la fin
for ans in anslist:
    # Affiche chaque élément unique d'une liste ou de l'autre, sur une ligne séparée
    print(ans)