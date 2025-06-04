# Création d'une liste vide qui sera utilisée pour stocker des sous-listes
a = []  # a sera une liste contenant d'autres listes, chaque sous-liste représente une paire d'entiers

# Demande à l'utilisateur de saisir un nombre (sous forme de chaîne), puis le convertit en entier
# Ce nombre représente le nombre de lignes/paires d'entiers à saisir
for i in range(int(input())):
    # Utilisation de input() pour demander à l'utilisateur d'entrer une ligne d'entiers séparés par des espaces
    # input() retourne une chaîne de caractères  
    # split() sépare cette chaîne en morceaux (listes de chaînes) là où elle trouve des espaces
    # map(int, ...) applique la fonction int à chaque élément pour convertir chaque chaîne en entier
    # list(...) convertit le map object en une liste d'entiers
    a.append(list(map(int, input().split())))
    # append() ajoute cette liste d'entiers comme un nouvel élément à la liste principale a

# Trie la liste a en utilisant la méthode sort()
# Par défaut, sort() trie la liste en place selon l'ordre croissant, en comparant les sous-listes élément par élément
# Ici, cela veut dire qu'il trie d'abord par le premier élément de chaque sous-liste, puis par le second si égalité, etc.
a.sort()

# Boucle sur la liste a, qui est maintenant triée
# Puisque chaque élément de a est une liste de deux entiers, on peut les extraire directement dans deux variables
for i, j in a:
    # Affiche les deux entiers i et j séparés par un espace
    # print ajoute un saut de ligne par défaut à la fin de chaque appel, donc chaque paire sera sur une ligne différente
    print(i, j)