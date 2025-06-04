# La première ligne est une boucle for qui s'exécute un certain nombre de fois.
# La fonction input() demande une entrée à l'utilisateur sous forme de texte.
# int(input()) convertit l'entrée de l'utilisateur en un nombre entier.
# range(int(input())) crée un objet itérable qui commence à 0 et s'arrête avant la valeur entière fournie.
# Le caractère de soulignement "_" est souvent utilisé comme variable jetable, indiquant que la valeur n'a pas d'importance.
for _ in range(int(input())):
    # On demande une entrée à l'utilisateur qui consiste en quatre nombres séparés par des espaces.
    # input() récupère la chaîne saisie.
    # .split() sépare la chaîne en une liste de sous-chaînes en se basant sur les espaces.
    # map(int, ...) applique la fonction int à chacun des éléments de la liste obtenue, convertissant ainsi chaque sous-chaîne en entier.
    # Cela permet de récupérer les coordonnées (x, y) du coin supérieur gauche d'un rectangle,
    # et ses dimensions w (largeur) et h (hauteur).
    x, y, w, h = map(int, input().split())
    # On initialise un compteur c à 0. 
    # Cette variable sera utilisée pour compter le nombre de points à l'intérieur du rectangle.
    c = 0
    # On lit à nouveau une valeur de l'utilisateur indiquant combien de points on va tester.
    # La conversion en entier s'effectue avec int().
    for _ in range(int(input())):
        # On lit une entrée qui contient deux valeurs, séparées par un espace, qui représentent les coordonnées d'un point.
        # map(int, input().split()) convertit ces deux valeurs en entiers.
        a, b = map(int, input().split())
        # On vérifie si le point (a, b) se situe à l'intérieur, ou sur le bord, du rectangle défini par (x, y, w, h).
        # La condition x <= a signifie que le point n'est pas à gauche du rectangle,
        # et a <= x + w signifie qu'il n'est pas à droite du rectangle (l'extrémité droite est incluse).
        # De même, y <= b signifie que le point n'est pas au-dessus du rectangle,
        # et b <= y + h signifie qu'il n'est pas en dessous.
        # Les signes <= incluent les bords du rectangle.
        if x <= a and a <= x + w and y <= b and b <= y + h:
            # Si la condition ci-dessus est vraie, le point est à l'intérieur ou sur le bord du rectangle.
            # On incrémente donc c de 1 avec l'instruction c += 1
            c += 1
    # Après avoir vérifié tous les points, on affiche le nombre total c
    # c'est-à-dire le nombre de points qui étaient à l'intérieur (ou sur le bord) du rectangle.
    print(c)