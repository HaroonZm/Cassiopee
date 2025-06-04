# Demande à l'utilisateur de saisir un entier (le nombre de requêtes ou d'opérations à effectuer)
q = int(input())

# Initialise un ensemble vide pour stocker des valeurs uniques
se = set()

# Boucle tant que le nombre de requêtes n'est pas nul (autrement dit, pour chaque requête)
while q:
    # On décrémente le compteur de requêtes de 1 à chaque itération de la boucle
    q -= 1

    # On lit une ligne de l'entrée standard (typiquement au clavier)
    # On découpe cette entrée en morceaux sur les espaces et on convertit chaque morceau en entier
    # op va contenir la première valeur entière (qui détermine l'opération à effectuer : 0 ou 1)
    # x va contenir la seconde valeur entière (l'élément concerné par l'opération)
    op, x = map(int, input().split())

    # Si la valeur de op est non nulle (c'est-à-dire différente de 0)
    if op:
        # On vérifie si x est déjà présent dans l'ensemble se
        # L'expression 'x in se' retourne True si x est dans se, sinon False
        # L'opérateur + convertit le booléen en entier : True devient 1, False devient 0
        # On affiche donc 1 si x est déjà présent dans se, sinon 0
        print(+(x in se))
    else:
        # Si op vaut 0, on doit ajouter x à l'ensemble se
        se.add(x)  # Ajout de x à l'ensemble se ; aucun effet si x s'y trouve déjà, car les ensembles sont faits pour contenir des éléments uniques

        # On affiche la longueur (le nombre d'éléments) de l'ensemble se après l'ajout (len(se) retourne ce nombre)
        print(len(se))