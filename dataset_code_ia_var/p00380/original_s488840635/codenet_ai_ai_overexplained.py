# Demande à l'utilisateur d'entrer une valeur entière, c'est-à-dire le nombre d'éléments dans la liste 'a_lst'.
n = int(input())

# Prend une ligne d'entrée utilisateur, la découpe en une séquence de chaînes séparées par des espaces,
# convertit chaque chaîne en un entier, puis crée une liste à partir de ces entiers.
# Ainsi, 'a_lst' devient une liste d'entiers de taille n que l'utilisateur vient de saisir.
a_lst = list(map(int, input().split()))

# Demande à l'utilisateur d'entrer un entier qui représente le nombre de requêtes ou d'opérations à traiter.
q = int(input())

# Pour chaque requête parmi les 'q' requêtes :
#   - lit une ligne
#   - sépare la ligne en différentes chaînes selon les espaces
#   - convertit ces chaînes en entiers
#   - rassemble ces entiers dans un tuple (afin de garder la structure x, y, typique d'une requête de swap)
# Enfin, la liste 'query' contient 'q' tuples d'entiers, représentant toutes les requêtes.
query = [tuple(map(int, input().split())) for _ in range(q)]

# Crée une nouvelle liste 'comp' qui contient les éléments de 'a_lst' triés dans l'ordre croissant.
# Cette liste sert de référence pour savoir où chaque élément doit se trouver pour que la liste soit triée.
comp = sorted(a_lst)

# Pour chaque indice i de 0 à n-1, compare l'élément a_lst[i] avec comp[i].
# Si les éléments aux mêmes positions diffèrent, cela signifie que la liste n'est pas encore triée.
# La compréhension de liste [a_lst[i] != comp[i] for i in range(n)] génère une liste de booléens.
# En valeurs Python, True vaut 1, False vaut 0, donc la somme donne le nombre de positions mal triées.
diff = sum([a_lst[i] != comp[i] for i in range(n)])

# Vérifie si 'diff' est égal à zéro, c'est-à-dire que toutes les positions de la liste 'a_lst' sont correctes.
if diff == 0:
    # Si c'est le cas, la liste est déjà triée. Imprime 0 pour indiquer qu'aucune opération n'est nécessaire.
    print(0)
else:
    # Si la liste n'est pas ordonnée, il faut traiter les requêtes une à une.
    # Pour chaque requête, on utilise sa position 'i' dans la boucle.
    for i in range(q):
        # Décompose la requête en deux valeurs 'x' et 'y'.
        x, y = query[i]

        # Comme la plupart des langages de programmation et la logique humaine commencent à compter à partir de 1,
        # mais que Python utilise des indices de tableau à partir de 0, on soustrait 1 de chaque indice.
        x -= 1
        y -= 1

        # Mise à jour de la variable 'diff' (le nombre de mauvaises positions).
        # L'idée est de compenser les effets potentiels de l'échange envisagé entre les positions 'x' et 'y' :
        #   - Soustrait le nombre de bonnes positions qui vont se retrouver mauvaises à cause de l'échange,
        #   - et ajoute celles qui seront corrigées par cet échange.
        # Les quatre comparaisons sont faites AVANT l'échange car la variable diff doit capturer
        # le changement d'état entre le pré- et post-échange.
        diff -= (a_lst[x] == comp[y]) + (a_lst[y] == comp[x]) - (a_lst[x] == comp[x]) - (a_lst[y] == comp[y])

        # Après la mise à jour de 'diff', vérifie à nouveau si la liste est triée (diff == 0).
        if diff == 0:
            # Si elle l'est, imprime le numéro de la requête (indice de boucle + 1, pour un comptage humain).
            print(i + 1)
            # Le mot-clé break permet d'arrêter la boucle prématurément car la condition est atteinte.
            break

        # Procède à l'échange réel des éléments dans la liste 'a_lst' aux indices x et y.
        # Cela permet de traiter la prochaine requête sur l'état mis à jour de la liste.
        a_lst[y], a_lst[x] = a_lst[x], a_lst[y]
    else:
        # Si la boucle n'a jamais rencontré 'diff == 0' pendant toutes les requêtes (donc break n'a jamais été atteint),
        # le bloc else relié à la boucle for entre en jeu pour indiquer qu'il était impossible de trier la liste.
        print(-1)