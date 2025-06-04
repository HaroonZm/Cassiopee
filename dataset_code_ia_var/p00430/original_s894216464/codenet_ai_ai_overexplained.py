def solve():
    # Initialisation d'une liste vide pour stocker les solutions finales.
    # Chaque élément de cette liste sera une chaîne représentant une décomposition trouvée.
    answers = []

    # Définition de la fonction récursive 'square' qui va générer toutes les décompositions possibles.
    # Paramètres :
    # ans   : liste des entiers déjà choisis pour constituer la somme.
    # rest  : valeur restante à atteindre pour compléter la somme souhaitée.
    # limit : valeur maximale qui peut être ajoutée à la liste 'ans' (pour garantir l'ordre non croissant).
    def square(ans, rest, limit):
        # Si la valeur restante à atteindre est 0, cela signifie que la somme de la liste 'ans'
        # est égale à la cible initiale. Nous avons alors trouvé une solution valide.
        if rest == 0:
            # On convertit chaque entier de la liste 'ans' en chaîne de caractères,
            # puis on les joint avec des espaces pour former une solution complète.
            # Enfin, on ajoute cette solution à la liste 'answers'.
            answers.append(' '.join(map(str, ans)))
        else:
            # Parcours de toutes les valeurs possibles pour l\'entier suivant à ajouter à la liste 'ans'.
            # On commence à 'rest', car on ne veut pas dépasser la somme cible,
            # et on crée des solutions avec des entiers strictement positifs.
            # On va jusqu'à 1 (inclus) en décrémentant à chaque itération.
            for i in range(rest, 0, -1):
                # On vérifie si la valeur courante 'i' dépasse la valeur 'limit'.
                # Si c'est le cas, on saute cette itération pour respecter l'ordre non croissant.
                if i > limit:
                    continue
                # Appel récursif à 'square' avec :
                # - une nouvelle liste composée de tous les éléments de 'ans' suivi de 'i' (ans + [i]).
                # - la nouvelle valeur à atteindre, qui est 'rest' diminué de 'i'.
                # - la nouvelle limite qui vaut 'i' (pour maintenir l'ordre non croissant).
                square(ans + [i], rest - i, i)

    # On importe le module 'sys' pour accéder à 'sys.stdin', qui permet de lire des données en entrée standard.
    import sys

    # Parcours de chaque nombre entier fourni par l'utilisateur via l'entrée standard.
    # Le 'map' applique la conversion en int pour chaque ligne entrée.
    for n in map(int, sys.stdin):
        # Si le nombre lu est 0, cela signifie qu'il faut arrêter le traitement.
        if n == 0:
            break
        # On appelle la fonction 'square' en partant de :
        # - une liste vide (aucun nombre choisi au début),
        # - la valeur du nombre lu ('rest' = n),
        # - la limite initiale qui vaut aussi 'n' (aucune restriction).
        square([], n, n)

    # Une fois toutes les solutions générées et stockées dans 'answers',
    # On les affiche toutes, chacune sur une ligne distincte.
    print('\n'.join(answers))

# Appel de la fonction principale pour exécuter le programme.
solve()