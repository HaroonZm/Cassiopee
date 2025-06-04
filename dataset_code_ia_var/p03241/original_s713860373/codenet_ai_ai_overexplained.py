import math  # Importe le module math qui fournit des fonctions mathématiques telles que sqrt (racine carrée)

# Lit une ligne du standard input (par défaut, le clavier), sépare les valeurs par des espaces, convertit chaque valeur en entier, puis assigne le premier à N et le second à M
N, M = map(int, input().split())

A = []  # Initialise une liste vide appelée A qui contiendra certains diviseurs de M

# Commence une boucle for dont la variable de boucle i commence à 1 et va jusqu'à la racine carrée de M incluse (int(math.sqrt(M)) + 1)
for i in range(1, int(math.sqrt(M)) + 1):
    if M % i == 0:  # Vérifie si i est un diviseur de M ; c'est-à-dire que M divisé par i n'a pas de reste
        if M // i >= N:  # Vérifie si le diviseur correspondant (M / i arrondi à l'entier inférieur) est supérieur ou égal à N
            A.append(i)  # Ajoute le diviseur i à la liste A
            if i >= N and M // i > i:  # Vérifie si i lui-même est supérieur ou égal à N et si l'autre diviseur (M // i) est strictement supérieur à i
                A.append(M // i)  # Ajoute ce second diviseur à la liste A

# Trie la liste A en place par ordre croissant (du plus petit au plus grand)
A.sort()

ans = A[-1]  # Récupère le plus grand élément de la liste A (c’est-à-dire le dernier après tri), et l’assigne à la variable ans

print(ans)  # Affiche la valeur de la variable ans (c’est la solution finale)