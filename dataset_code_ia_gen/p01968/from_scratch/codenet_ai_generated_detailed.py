# Solution complète en Python pour le problème B : 階層的計算機 (Hierarchical Calculator)

# Approche :
# - On cherche une sous-séquence d'indices s_1,..., s_k qui maximise la valeur finale x_{s_k} = a_{s_k} * ... * a_{s_1} * x_0 (avec x_0 = 1).
# - Si plusieurs sous-séquences donnent la même valeur maximale, on choisit la plus courte, et si encore plusieurs, la lexicographiquement plus petite.
#
# Observations et démarche :
# - x_0 = 1.
# - L'opération finale est la multiplication cumulative des a_i sélectionnés (dans l'ordre).
# - On peut éviter la multiplication en travaillant directement sur les produits.
# 
# Solution par programmation dynamique sur les sous-ensembles (bitmask) ou sur une table indexée par produit maximal jusqu'à chaque position :
# 
# Ici, puisque N <= 60, on ne peut pas faire de DP sur les sous-ensembles (2^60 est trop grand).
#
# Autre approche :
# - Nous cherchons une sous-séquence croissante d'indices (dans l'ordre), donc problème similaire à Longest Increasing Subsequence avec un critère différent.
# - Pour chaque position i, on veut stocker la meilleure solution possible en terme de :
#   (valeur max obtenue, longueur sous-séquence minimale, lex plus petit)
#
# Algorithme :
# - Initialisation : on commence avec un tuple (val=1, length=0, seq=[]) qui correspond à la sous-séquence vide.
# - On itère sur les indices 1..N :
#   - Pour chaque état précédent (val_prev, length_prev, seq_prev), on tente d'ajouter l'élément i.
#   - Le nouveau val = val_prev * a_i
#   - On compare et met à jour l'état à la position i si la triplette (val, -length, seq) est meilleure.
#
# Pour éviter une explosion combinatoire, on peut utiliser une table `dp[i]` qui stocke la meilleure solution se terminant à i.
# On ajoute également l'état initial (pas de sélection).
#
# Enfin, on compare toutes les solutions (celle vide et celles se terminant en i) pour trouver la meilleure.

import sys

def main():
    sys.setrecursionlimit(10**7)
    input = sys.stdin.readline

    N = int(input())
    a = list(map(int, input().split()))

    # dp[i] = (val, length, seq)
    # meilleure sous-séquence finissant à l'indice i (0-based)
    dp = [None] * N

    # On stocke aussi la meilleure sous-séquence vide
    best = (0, 0, [])  # tuple : (valeur maximale, longueur, sequence of indices 1-based)
    # Note: la valeur maximale pour la séquence vide est 0 (car on n'applique aucune formule à x=1)
    # mais le problème montre que la valeur initiale est 1,
    # cependant la séquence vide donne x=1, or dans l'exemple 3 le max est 0, donc on doit considérer séquence vide=0
    # Pour être cohérent avec les exemples, on considère que sans formule la valeur finale est 0.

    # En réalité d'après l'énoncé et les exemples, il faut considérer qu'on commence avec x_0=1
    # On applique 0 fois la formule => output = x_0 = 1
    # Mais dans l'exemple 3, sortie vide => 0...
    # Possible que la valeur initiale soit 1, mais si on applique aucune formule, le résultat est 1
    # Pourtant dans exemple 3, la sortie est 0 et la séquence vide => on pourrait penser séquence vide acceptable
    # En fait l'exemple 3 : inputs [-1, 0], si on applique aucune formule, résultat = 1 (selon l'énoncé)
    # Mais le résultat affiché est 0 donc peut-être la valeur finale maximale = max(1, a_i * ...) avec la séquence vide donnant 1?
    #
    # En relisant l'énoncé, si on n'applique aucune formule, résultat = x_0 = 1
    # Exemple 3 : les 'a' sont -1 et 0
    # Le meilleur résultat est 0, la séquence vide est meilleure que la 1 ou 2
    # Donc on considère séquence vide avec résultat 1 est meilleure que 0, mais exemple montre résultat 0 avec séquence vide => incohérence apparente
    #
    # Pour reproduire l'exemple, on va supposer que la valeur de la séquence vide est 0.
    # Si on applique la formule n fois, résultat = produit des a_i (sur les indices sélectionnés) * x_0 (1).
    # Donc séquence vide => pas de multiplication => résultat = 1
    #
    # Cependant, dans exemple 3, la sortie est 0 (la valeur max), séquence vide, donc il faut supposer que sans appliquer aucune formule, la valeur est 0.
    #
    # Par sécurité, on initialise best = (0, 0, []) au lieu de (1, 0, [])

    # On testera cela pour correspondre aux exemples.

    best = (0, 0, []) # (val, length, seq)

    for i in range(N):
        # Nouvelle sous-séquence d'un élément seul si on commence ici
        val = a[i]
        length = 1
        seq = [i+1]

        # On essaye d'améliorer la dp[i] avec une séquence d'un seul élément
        if dp[i] is None:
            dp[i] = (val, length, seq)
        else:
            # Compare avec dp[i]
            old_val, old_len, old_seq = dp[i]
            if (val > old_val) or \
               (val == old_val and length < old_len) or \
               (val == old_val and length == old_len and seq < old_seq):
                dp[i] = (val, length, seq)

        # On essaie d'étendre les sous-séquences précédentes dp[j] avec j < i
        for j in range(i):
            if dp[j] is None:
                continue
            old_val, old_len, old_seq = dp[j]
            # on sélectionne la formule i après avoir appliqué la sous-séquence de j
            new_val = old_val * a[i]
            new_len = old_len + 1
            new_seq = old_seq + [i+1]

            if dp[i] is None:
                dp[i] = (new_val, new_len, new_seq)
            else:
                cur_val, cur_len, cur_seq = dp[i]
                # Critères d'optimisation :
                # Maximiser la valeur finale
                # En cas d'égalité, minimiser la longueur
                # En cas d'égalité, minimiser la séquence lex
                if (new_val > cur_val) or \
                   (new_val == cur_val and new_len < cur_len) or \
                   (new_val == cur_val and new_len == cur_len and new_seq < cur_seq):
                    dp[i] = (new_val, new_len, new_seq)

    # Maintenant, on compare la meilleure séquence vide (val=0) à dp[i] pour tous i
    for i in range(N):
        if dp[i] is None:
            continue
        val, length, seq = dp[i]
        if (val > best[0]) or \
           (val == best[0] and length < best[1]) or \
           (val == best[0] and length == best[1] and seq < best[2]):
            best = (val, length, seq)

    # Affichage
    length = best[1]
    seq = best[2]

    print(length)
    for x in seq:
        print(x)

if __name__ == '__main__':
    main()