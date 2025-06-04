# On entre dans une boucle infinie qui ne s'arrêtera que si une condition particulière est remplie.
while 1:
    # Demander à l'utilisateur de saisir une valeur via l'entrée standard, c'est-à-dire le clavier.
    # La fonction input() récupère l'entrée de l'utilisateur sous forme de chaîne de caractères.
    n = input()
    
    # Cette ligne vérifie si la valeur de n est égale à zéro.
    # Si c'est le cas, la boucle se termine grâce à l'instruction break, ce qui arrête l'exécution de la boucle while.
    if n == 0:
        break

    # Création d'une liste nommée s.
    # Pour chaque i compris entre 0 et n-1 (où n est la valeur entrée précédemment),
    # on effectue l'opération suivante :
    # 1. Demander à l'utilisateur d'entrer une ligne via raw_input() (chaîne de caractères).
    # 2. Diviser cette chaîne en sous-chaînes séparées par des espaces grâce à split().
    # 3. Convertir chaque sous-chaîne en entier via map(int, ...).
    # Le résultat est une liste de n listes d'entiers.
    s = [map(int, raw_input().split()) for i in range(n)]

    # Création d'un ensemble (set) nommé sh.
    # Pour chaque i compris entre 0 et n-1 :
    #   - On prend la ligne s[i] (une liste d'entiers).
    #   - On recherche la valeur minimale de cette ligne avec min().
    #   - On construit un set contenant toutes les valeurs minimales de chaque ligne.
    sh = set([min(s[i]) for i in range(n)])

    # Création d'un autre ensemble (set) nommé tl.
    # Pour chaque i compris entre 0 et n-1 (chaque colonne) :
    #   - On construit une liste contenant pour chaque j la valeur s[j][i] (c'est-à-dire l'élément dans la colonne i pour la ligne j).
    #   - On recherche la valeur maximale de cette colonne avec max().
    #   - On construit un set contenant toutes les valeurs maximales de chaque colonne.
    tl = set([max([s[j][i] for j in range(n)]) for i in range(n)])

    # On recherche l'intersection entre les deux ensembles sh et tl,
    # c'est-à-dire les éléments qui sont présents à la fois dans les deux ensembles.
    # (sh & tl) donne l'intersection des ensembles.
    # On convertit le résultat en liste avec list().
    # Si la longueur de cette liste est strictement supérieure à 0, 
    # cela veut dire qu'il existe au moins un élément commun,
    # et on affiche le premier élément de cette liste avec [0].
    # Sinon, si l'intersection est vide, on affiche 0.
    print list(sh & tl)[0] if len(sh & tl) > 0 else 0