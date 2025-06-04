from bisect import bisect  # Le module 'bisect' fournit des fonctions pour travailler efficacement avec des listes triées.

# Lecture de l'entrée utilisateur : l'utilisateur saisit un entier n via le clavier.
n = int(input())  # Conversion de la chaîne de caractères lue en entier et affectation à la variable n.

# Lecture des n paires d'entiers.
P = [list(map(int, input().split())) for i in range(n)]
# Explication détaillée de cette ligne :
# - 'input()' lit une ligne saisie par l'utilisateur, qui doit contenir deux entiers séparés par un espace.
# - 'input().split()' sépare cette ligne en une liste de chaînes (mots), par défaut sur les espaces.
# - 'map(int, ...)' convertit chaque chaîne en entier.
# - 'list(...)' convertit le résultat du map en liste de deux éléments : [a, b].
# - Cette expression est répétée n fois, donc on obtient une liste de n sous-listes de 2 entiers.

M = 10**5 + 1  # Définition d'une constante. 10**5 équivaut à 100000, donc M vaut 100001.

# Définition de la fonction 'policy1' qui prend en entrée une liste P de paires d'entiers.
def policy1(P):
    # Création d'une liste A contenant le premier élément de chaque paire de P.
    A = [a for a, b in P]
    # Création d'une liste B contenant le second élément de chaque paire de P.
    B = [b for a, b in P]
    # Tri de la liste A dans l'ordre croissant.
    A.sort()
    # Tri de la liste B dans l'ordre croissant.
    B.sort()
    ans = 1  # Initialisation de la variable 'ans' à 1. Cette variable stockera le résultat final (le maximum cherché).

    # Parcours de chaque paire (a, b) dans la liste P.
    for a, b in P:
        # Recherche de la position d'insertion de 'a' dans la liste triée B.
        left = bisect(B, a)
        # 'bisect' retourne l'indice où 'a' pourrait être inséré pour maintenir l'ordre trié.
        # Cela permet de compter efficacement combien d'éléments de B sont inférieurs ou égaux à 'a'.

        # Recherche de la position d'insertion de 'b-1' dans la liste triée A.
        right = n - bisect(A, b - 1)
        # Ici on soustrait l'indice obtenu à 'n' (taille de la liste) pour obtenir le nombre d'éléments dans A supérieurs à 'b-1'.

        # On met à jour la valeur de 'ans' si le nouveau calcul (n - (left + right)) est supérieur à la valeur précédente.
        ans = max(ans, n - (left + right))

    return ans  # Retourne la valeur maximale calculée.


# Définition de la fonction 'policy2' qui prend en entrée une liste P de paires d'entiers.
def policy2(P):
    # Création d'une liste D de taille M remplie de zéros.
    # D'agit comme d'un tableau de comptage pour chaque entier de 0 à M-1.
    D = [0] * M

    # Remplissage du tableau D d'après chaque paire (a, b) de P.
    for a, b in P:
        D[a] += 1  # Incrémentation : indique qu'une séquence commence à l'indice 'a'.
        D[b] -= 1  # Décrémentation : indique qu'une séquence se termine juste avant l'indice 'b'.

    # Calcul du préfixe cumulatif de D pour déterminer, pour chaque position, combien de séquences sont actives.
    for i in range(1, M):
        D[i] += D[i - 1]
        # Pour chaque i de 1 à M-1, on ajoute la valeur précédente à la valeur courante.
        # Cela rend, à chaque position i, le nombre total d'intervalles couvrant i.

    # Retourne la valeur maximale trouvée dans le tableau D.
    return max(D)

# Appel des deux fonctions définies précédemment et affichage des résultats sur une seule ligne,
# séparés par un espace, grâce à la fonction 'print'.
print(policy1(P), policy2(P))
# Cela affiche d'abord le résultat de policy1(P), puis celui de policy2(P), sur la même ligne.