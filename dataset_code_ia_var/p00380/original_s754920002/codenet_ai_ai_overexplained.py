import sys  # Importe le module sys, qui fournit des fonctions spécifiques au système d'exploitation, notamment la gestion des entrées/sorties, des arguments de ligne de commande, etc.

readline = sys.stdin.readline  # Assigne à la variable 'readline' la méthode 'readline' de 'sys.stdin', pour lire efficacement les entrées ligne par ligne depuis l'entrée standard (par exemple, lors de l'utilisation de pipes ou de redirections en ligne de commande).

N = int(readline())  # Lit une ligne depuis l'entrée standard, la convertit en entier et l'affecte à la variable N. Cela représente probablement le nombre d'éléments dans le tableau à traiter.

*A, = map(int, readline().split())  # Lit une autre ligne depuis l'entrée standard, la découpe en morceaux (en se basant sur les espaces), convertit chaque morceau en entier avec map(int, ...), puis affecte la liste entière à la variable A. Le * avant A dans l'affectation indique que tous les résultats sont packés dans une liste.

C = A[:]  # Crée une copie superficielle (shallow copy) de la liste A et l'affecte à la nouvelle variable C. Cela garantit que C est indépendant de A : toute modification de C ne changera pas A, et vice-versa.

C.sort()  # Trie la liste C en place, c'est-à-dire que C devient maintenant une version triée (par ordre croissant) des mêmes éléments que dans A.

MOD = 4253024257  # Définit une constante entière MOD avec une valeur élevée, utilisée pour effectuer des opérations de modulo afin d'éviter les débordements de nombres entiers dans certains calculs.

base = 3  # Définit la base utilisée pour le calcul de puissances, souvent utilisé dans le contexte de hashage polynomial ou de calculs combinatoires pour donner un poids à chaque terme.

B = [0]*N  # Initialise une nouvelle liste B de longueur N, remplie initialement de zéros. B sera utilisée pour stocker des puissances successives de 'base' modulo MOD.

v = 1  # Initialise la variable v à 1, représentant la première puissance (base^0) lors du calcul des puissances successives.

P = Q = 0  # Initialise deux variables P et Q à 0. Ces variables serviront à stocker les "polynômes pondérés" pour les tableaux A et C, respectivement.

# Début de la boucle pour remplir B et calculer P et Q.
for i in range(N):  # Pour chaque indice i de 0 à N-1 :
    B[i] = v  # La i-ème case de B reçoit la valeur courante de v (c'est-à-dire base^i mod MOD).
    P += v * A[i]  # Ajoute à P le produit de v (poids de position) par l'élément courant dans A.
    Q += v * C[i]  # Ajoute à Q le produit de v par l'élément courant dans C (trié).
    v = v * base % MOD  # Met à jour v : il devient la puissance suivante de la base, modulo MOD pour contrôler la taille.

if P == Q:  # Vérifie si la combinaison pondérée (hash pondéré) du tableau original A est identique à celle du tableau trié C.
    print(0)  # Si c'est le cas, cela signifie que le tableau A est déjà "équivalent" à C selon ce critère.
    exit(0)  # Le programme s'arrête ici immédiatement, car aucune transformation n'est nécessaire.

# Si les valeurs pondérées diffèrent, il faut tenter de rendre A "équivalent" à C à l'aide d'opérations supplémentaires.

for i in range(int(readline())):  # Boucle autant de fois que le nombre d'opérations supplémentaires indiqué sur la ligne suivante lue depuis l'entrée. À chaque itération, i prend les valeurs de 0 à (nombre d'opérations - 1).
    x, y = map(int, readline().split())  # Lit une ligne avec deux nombres, les convertit en int et les affecte à x et y. Ces deux entiers représentent les indices (1-based) pour une opération de permutation.
    x -= 1; y -= 1  # Convertit x et y de 1-based à 0-based (les indices Python commencent à 0).
    p = A[x]  # Sauvegarde l'élément à l'indice x du tableau A dans la variable p.
    q = A[y]  # Sauvegarde l'élément à l'indice y du tableau A dans la variable q.
    r = B[y] - B[x]  # Calcule la différence des poids B entre l'indice y et l'indice x, la stocke dans r.
    # Met à jour la somme pondérée P en tenant compte de la permutation :
    # On ajoute (r*p) et on enlève (r*q) : cela compense l'effet de la permutation sur le "hash".
    P += r * p - r * q
    if P == Q:  # Après cette opération, vérifie si on a atteint l'équivalence pondérée.
        print(i+1)  # Affiche le nombre d'opérations (1-based) nécessaires pour atteindre l'équivalence.
        break  # Sort de la boucle for car l'objectif est atteint.
    A[x], A[y] = q, p  # Échange effectivement les éléments A[x] et A[y]. Permet de garder A cohérent pour les prochaines opérations.
else:
    print(-1)  # Si la boucle se termine sans trouver P == Q, affiche -1, indiquant que l'objectif n'a pas pu être atteint même après toutes les opérations.