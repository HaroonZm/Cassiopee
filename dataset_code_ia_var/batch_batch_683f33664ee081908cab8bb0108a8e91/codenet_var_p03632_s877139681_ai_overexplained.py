# Demande à l'utilisateur d'entrer quatre entiers séparés par des espaces. La fonction input() récupère la saisie de l'utilisateur sous forme de chaîne de caractères,
# puis split() divise la chaîne en une liste de sous-chaînes selon les espaces. La fonction map(int, ...) convertit chaque sous-chaîne en entier.
# Enfin, les quatre entiers ainsi obtenus sont assignés respectivement aux variables a, b, c, et d.
a, b, c, d = map(int, input().split())

# Initialise une variable ans à 0.
# Cette variable va servir de compteur pour compter le nombre d'éléments communs entre deux intervalles numériques.
ans = 0

# La fonction range(a, b + 1) génère un intervalle d'entiers commençant depuis la valeur a (incluse)
# jusqu'à la valeur b incluse (range s'arrête à b+1, car la borne supérieure est exclusive).
# Cet intervalle représente tous les entiers possibles dans le premier segment [a, b].
al = range(a, b + 1)

# De façon similaire, on crée une seconde plage d'entiers de c à d inclus avec range(c, d + 1).
# Cela représente tous les entiers possibles dans le second segment [c, d].
bo = range(c, d + 1)

# La boucle for parcourt chaque valeur l dans la plage al (c'est-à-dire pour chaque entier entre a et b inclus).
for l in al:
    # La condition if vérifie si la valeur l est également présente dans la plage bo, c'est-à-dire si l est aussi un élément de [c, d].
    # L'opérateur "in" teste l'appartenance d'un élément à une séquence (ici à une plage d'entiers).
    if l in bo:
        # Si la condition est vérifiée, le compteur ans est incrémenté de 1.
        # Cela signifie qu'on a trouvé un entier appartenant à la fois aux deux intervalles.
        ans += 1

# Après avoir parcouru tous les éléments de [a, b], on vérifie si le compteur ans est strictement supérieur à 0,
# c'est-à-dire s'il existe au moins un entier commun aux deux segments.
if ans > 0:
    # Si c'est le cas, on affiche ans - 1.
    # Cela correspond à la taille de l'intersection des deux segments, car il y a ans éléments communs,
    # mais les bornes étant inclusives des deux côtés, on retire 1 pour obtenir la longueur du segment d'intersection.
    print(ans - 1)
else:
    # Si ans n'est pas supérieur à 0, cela signifie qu'il n'y a pas d'élément commun entre les deux segments.
    # Dans ce cas, on affiche 0 conformément à l'exigence.
    print(0)