import sys  # Importe le module sys qui permet d'utiliser des fonctions liées au système d'exploitation

# Modifie la limite par défaut de récursion.
# Par défaut, la profondeur maximale d'appels récursifs en Python est assez faible (~1000).
# On l'augmente ici à 10 puissance 7, soit 10 000 000, ce qui peut être utile pour des appels récursifs profonds dans certains problèmes.
sys.setrecursionlimit(10 ** 7)

# Définition d'une constante entière appelée MOD qui sert à prendre le résultat modulo cette valeur dans divers calculs,
# souvent pour éviter le dépassement de capacité des entiers lors de calculs avec de très grands nombres.
MOD = 10 ** 9 + 7  # 1 000 000 007 est un nombre premier utilisé fréquemment en programmation compétitive

# Lecture d'une entrée utilisateur, attendue comme une chaîne de caractères qui représente un entier N
# La fonction int() convertit cette chaîne de caractères en nombre entier.
N = int(input())

# Création d'une liste A de N éléments, chaque élément étant un tuple d'entiers.
# Pour chaque ligne (il y en a N), on lit une ligne de l'entrée standard, on la découpe en morceaux selon les espaces,
# on convertit chaque morceau en entier grâce à map(int, ...), puis on met tout dans un tuple.
# Cela forme une liste de tuples appelée A.
A = [tuple(map(int, input().split())) for _ in range(N)]

# Création d'une liste dp destinée à contenir des résultats intermédiaires (mémorisation ou mémoïsation pour l'optimisation dynamique).
# Sa taille est 2 puissance N, ce qui correspond à tous les sous-ensembles possibles des N éléments (présents ou absents, codés par bits).
# Chaque case est initialisée à -1 pour signifier qu'aucun résultat n'y est encore stocké.
dp = [-1] * (1 << N)

# On fixe la dernière case, dont l'indice est (1 << N) - 1, c'est-à-dire le nombre où tous les N bits de poids faibles sont à 1,
# c'est-à-dire l'ensemble où TOUS les éléments ont déjà été pris. Dans ce cas, il n'y a qu'une façon de "ne rien faire de plus", donc valeur 1.
dp[(1 << N) - 1] = 1

# Définition d'une fonction nommée dfs (pour "depth-first search", recherche en profondeur),
# prenant en paramètre 'group' (entier représentant l'ensemble actuel d'éléments déjà utilisés grâce à son écriture binaire)
# et 'count', un compteur représentant combien d'affectations/étapes on a déjà faites (souvent l'indice de la ligne actuelle dans A).
def dfs(group, count):
    # Si le résultat de dp[group] n'est pas -1, cela signifie que l'on a déjà calculé le résultat pour cet argument.
    # Dans ce cas, on retourne tout de suite la valeur mémorisée pour éviter de le recalculer (mémoïsation).
    if dp[group] != -1:
        return dp[group]
    # On initialise une variable entière res à 0 pour garder la somme des résultats des branches valides du DFS à partir d'ici.
    res = 0
    # On parcourt tous les indices possibles de 0 à N-1 (correspondant aux N "personnes"/éléments/colonnes de A).
    for i in range(N):
        # On vérifie si l'i-ème bit du nombre 'group' est éteint (0), c'est-à-dire si l'i-ème élément n'a PAS ENCORE été choisi,
        # grâce à la manipulation de bits ((group >> i) & 1 vérifie le ième bit à partir de la droite).
        # On vérifie aussi si l'affectation actuelle (A[count][i]) est valide (par exemple, si elle est 1).
        if ((group >> i) & 1 == 0) and (A[count][i] == 1):
            # Si les conditions sont réunies, on ajoute le résultat du DFS récursif en rajoutant l'i-ème élément au groupe (group + (1 << i)),
            # et en augmentant count de 1 (on passe à la prochaine ligne/étape).
            res += dfs(group + (1 << i), count + 1)
    # Après avoir exploré toutes les possibilités à partir de cet état, on stocke le résultat modulo MOD dans dp[group]
    # pour éviter les dépassements de capacité et pour pouvoir le réutiliser si l'on retombe sur cet état.
    dp[group] = res % MOD
    # On retourne la valeur ainsi calculée ou récupérée.
    return dp[group]

# Appel initial à la fonction dfs en partant de l'état "aucun élément choisi" (group=0), et du compteur à 0.
# Le résultat (nombre total de façons de réaliser un appariement parfait sous contraintes) est stocké dans la variable tmp.
tmp = dfs(0, 0)

# Affichage du résultat final sur la sortie standard.
print(tmp)