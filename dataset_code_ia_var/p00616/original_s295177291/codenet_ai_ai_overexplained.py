# Commence une boucle infinie qui continuera jusqu'à ce qu'on rencontre une condition d'arrêt explicite (break).
while True:
    # Lit une ligne en entrée, la découpe en deux parties et convertit chaque partie en entier.
    # Par exemple, si l'utilisateur tape "3 2", alors n = 3 et h = 2.
    n, h = map(int, input().split())
    # Vérifie si la valeur de n est 0. Si c'est le cas, cela sert de condition d'arrêt pour notre boucle infinie.
    if n == 0:
        # Arrête complètement la boucle (sort du while True).
        break

    # Initialise un ensemble vide nommé 'hit'. Un ensemble est une structure de données qui stocke des éléments uniques seulement.
    hit = set()

    # Démarre une boucle répété 'h' fois. La variable '_' prend successivement les valeurs de 0 à h-1 mais son nom indique qu'elle n'est pas utilisée.
    for _ in range(h):
        # Lit une ligne en entrée, la découpe en trois parties. Cela représente trois chaînes de caractères.
        c, a, b = input().split()

        # Le code suivant dépend de la valeur de la chaîne de caractères c.
        # On compare c à trois valeurs possibles que sont "xy", "xz" et "yz".

        if c == "xy":
            # Si c est "xy", cela veut dire qu'on cible le plan XY à une hauteur z variable (pour toutes les valeurs possibles de z).
            # Crée un ensemble de tuples, chaque tuple étant composé de trois entiers : (a, b, z), 
            # où :
            #   int(a) est la valeur fixée pour x,
            #   int(b) est la valeur fixée pour y,
            #   z varie de 1 à n inclus (1, 2, ..., n)
            add = {(int(a), int(b), z) for z in range(1, n + 1)}

        elif c == "xz":
            # Si c est "xz", cela veut dire qu'on cible le plan XZ à une valeur y spécifique (pour toutes les valeurs possibles de y).
            # Crée un ensemble de tuples, chaque tuple ayant la forme (a, y, b), avec :
            #   int(a) fixé pour x,
            #   y variant de 1 à n inclus,
            #   int(b) fixé pour z
            add = {(int(a), y, int(b)) for y in range(1, n + 1)}

        elif c == "yz":
            # Si c est "yz", on cible le plan YZ, c'est-à-dire tous les points à une valeur x donnée (pour tous les x possibles).
            # Crée un ensemble de tuples (x, a, b), où :
            #   x varie de 1 à n inclus,
            #   int(a) est la valeur fixée pour y,
            #   int(b) est la valeur fixée pour z
            add = {(x, int(a), int(b)) for x in range(1, n + 1)}

        # Met à jour l'ensemble 'hit' avec le nouvel ensemble 'add'.
        # Ici, le symbole '|' représente l'union d'ensembles (tous les éléments présents dans 'hit', dans 'add', ou les deux).
        hit = hit | add

    # Calcul du nombre total de points possibles dans le cube, c'est-à-dire n * n * n ou n**3.
    # Soustrait le nombre d'éléments uniques de l'ensemble 'hit', c'est-à-dire, les points "touchés".
    # Affiche le résultat à l'écran.
    print(n ** 3 - len(hit))