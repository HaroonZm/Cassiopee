# Demander à l'utilisateur d'entrer une valeur entière qui sera la taille des listes à manipuler.
# La fonction input() lit l'entrée utilisateur sous forme de chaîne de caractères.
# La fonction int() convertit cette chaîne en un entier.
N = int(input())

# Initialiser une liste A contenant deux sous-listes de taille N, chacune remplie de zéros.
# La syntaxe [0]*N crée une liste de N zéros.
# L'expression [ [0]*N for _ in range(2) ] crée deux telles listes et les place dans la liste A.
A = [[0]*N for _ in range(2)]

# Remplir la première sous-liste de A avec N entiers donnés par l'utilisateur :
# input() lit la ligne entière entrée par l'utilisateur sous forme de chaîne.
# split() sépare la chaîne en une liste de sous-chaînes selon les espaces.
# map(int, ...) convertit chaque sous-chaîne en entier.
# list(...) transforme le map en liste réelle.
A[0] = list(map(int, input().split()))

# De même, remplir la seconde sous-liste de A avec N entiers fournis par l'utilisateur.
A[1] = list(map(int, input().split()))

# Initialiser la variable ans qui contiendra la réponse maximale à 0.
ans = 0

# Parcourir tous les indices possibles de 0 jusqu'à N-1 (inclus)
for i in range(N):
    # Initialiser une variable temporaire temp à 0. Cette variable stockera la somme calculée
    # pour la valeur actuelle de i.
    temp = 0
    
    # Première boucle : additionner les éléments de la première ligne de A depuis l'indice 0 jusqu'à i (inclus).
    # range(i+1) génère les indices 0, 1, ..., i.
    for j in range(i+1):
        # Ajouter à temp la valeur de l'élément A[0][j].
        temp += A[0][j]
    
    # Deuxième boucle : additionner certains éléments de la deuxième ligne de A.
    # L'objectif est de sommer les N - i derniers éléments de la deuxième liste.
    # range(N-i) génère N-i entiers de 0 à N-i-1.
    for j in range(N-i):
        # Utiliser un indice négatif pour accéder aux éléments depuis la fin de la liste.
        # -1 donne le dernier élément, -2 l'avant-dernier, etc.
        temp += A[1][-(j+1)]
    
    # Mettre à jour la réponse ans : si le temp calculé est plus grand que ans, alors
    # remplacer ans par temp. Sinon, ans reste inchangé.
    # La fonction max() renvoie la plus grande des deux valeurs passées en argument.
    ans = max(ans, temp)

# Afficher la valeur finale de ans avec la fonction print().
print(ans)