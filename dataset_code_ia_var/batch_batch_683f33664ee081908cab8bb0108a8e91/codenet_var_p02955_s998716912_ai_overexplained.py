from itertools import accumulate  # Importation de la fonction accumulate pour générer des sommes cumulées

# Lecture de toutes les données d'entrée depuis l'entrée standard, puis conversion de chaque élément en entier grâce à map(int, ...)
N, K, *A = map(int, open(0).read().split())
# N : nombre d'éléments du tableau A
# K : nombre maximum de modifications autorisées
# A : tableau des entiers ; le * signifie que tout ce qui reste après N et K va dans la liste A


def check(d):
    # Cette fonction retourne True si, en utilisant au plus K opérations, on peut rendre tous les éléments de A divisibles par d
    # Elle vérifie cela en considérant les restes modulo d de chaque élément de A

    # Calcul du reste de chaque élément de A lorsqu'il est divisé par d
    r = sorted([v % d for v in A])
    # On trie les restes dans l'ordre croissant pour rendre les calculs ultérieurs plus simples

    # Calcul des valeurs nécessaires pour que chaque reste atteigne d (par soustraction du reste à d)
    r_inv = [d - v for v in r]

    # Création d'une liste contenant 0 suivi des sommes cumulées des restes.
    # Cela veut dire que r_cs[i] est la somme des i premiers restes (de 0 à i-1)
    r_cs = [0] + list(accumulate(r))

    # Calcul de la somme cumulée des "complements" (r_inv) en partant de la fin du tableau
    # La fonction accumulate opère normalement de gauche à droite, donc on inverse la liste, puis on l'accumule,
    # puis on la réinverse pour obtenir les sommes de droite à gauche
    r_inv_cs = list(accumulate(r_inv[::-1]))[::-1] + [0]
    # On ajoute [0] à la fin pour avoir une taille compatible avec r_cs

    ret = False  # Variable qui va retenir si une configuration valide a été trouvée

    # Boucle sur toutes les façons possibles de répartir les modifications entre augmenter et diminuer les éléments
    for i in range(N + 1):
        flg1 = r_cs[i] <= K  # Est-ce qu'on peut ramener les i premiers restes à 0 avec au plus K opérations ?
        flg2 = r_cs[i] == r_inv_cs[i]  # Est-ce que les augmentations et diminutions nécessaires sont égales ?
        # Si les deux conditions sont remplies, cela signifie qu’il est possible avec K ou moins de modifications de tout rendre divisible par d
        ret = (flg1 and flg2) or ret  # On conserve True si jamais au moins une itération vérifie les deux conditions

    return ret  # Retourne True si au moins une configuration est valide, sinon False


M = sum(A)  # Somme totale des éléments du tableau A (utilisée pour déterminer les diviseurs possibles)
ans = 0  # Variable pour stocker la plus grande valeur de d trouvée

# On souhaite trouver le plus grand diviseur de M pour lequel check(d) retourne True
# On parcourt tous les diviseurs potentiels de M de la plus grande à la plus petite valeur possible

for i in reversed(range(1, int(M ** 0.5) + 1)):
    # La boucle va de la racine carrée de M jusqu'à 1, ce qui permet de ne vérifier chaque diviseur que deux fois au maximum

    if M % i == 0:  # Si i est un diviseur de M
        if check(i):  # On vérifie si on peut rendre tous les éléments divisibles par i en au plus K opérations
            ans = max(ans, i)  # Si oui, on met à jour la réponse si i est supérieur à la valeur actuelle

    # (M // i) donne l'autre diviseur complémentaire
    if M % (M // i) == 0:  # Si (M // i) est un diviseur de M
        # Ici, on vérifie si le diviseur complémentaire donne un meilleur résultat
        if check(M // i):
            ans = max(ans, M // i)  # Mise à jour si besoin

# À la fin de la boucle, ans contient le plus grand diviseur de M pour lequel tous les éléments de A peuvent devenir multiples de ans en au plus K modifications
print(ans)  # Affichage du résultat final