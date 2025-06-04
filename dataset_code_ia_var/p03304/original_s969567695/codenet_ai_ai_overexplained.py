# Demander à l'utilisateur de saisir trois entiers séparés par des espaces et les assigner
# aux variables n, m et d après les avoir convertis en entiers.
n, m, d = map(int, input().split())

# Calculer la valeur (n - d), qui va servir pour vérifier une condition et pour des calculs.
# Cela représente la différence entre n et d.
diff = n - d

# Calculer la valeur (1 + d), qui sera aussi utilisée dans la comparaison de conditions.
min_val = 1 + d

# Vérifier si la différence (n - d) est inférieure à (1 + d).
if diff < min_val:
    # Si la condition est vraie, calculer une expression "ex" :
    # - Multiplier diff par 2
    # - Diviser le résultat par n au carré (n ** 2)
    # Cela pourrait par exemple représenter une probabilité ou une moyenne pondérée.
    ex = (2 * diff) / (n ** 2)
    # Multiplier l'expression "ex" par (m - 1) pour obtenir le résultat final "ans".
    ans = ex * (m - 1)
# Si la condition précédente n'est pas vérifiée, exécuter le bloc else
else:
    # Calculer "ex" exactement comme précédemment :
    # - Multiplier la différence diff par 2 (pour doubler)
    # - Diviser par n au carré, pour normaliser par rapport à n.
    ex = 2 * diff / (n ** 2)
    # Vérifier si d est égal à 0.
    if d == 0:
        # Si d vaut 0, calculer ans différemment :
        # - Multiplier ex par (m - 1)
        # - Puis diviser par 2 (équivaut à prendre la moitié du résultat précédent).
        ans = ex * (m - 1) / 2
    else:
        # Si d n'est pas zéro, alors ans est simplement ex multiplié par (m - 1)
        ans = ex * (m - 1)

# Afficher la valeur finale de ans à l'utilisateur.
# Il s'agit d'un nombre à virgule flottante représentant le résultat du calcul précédent.
print(ans)