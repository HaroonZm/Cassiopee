import sys  # Importation du module sys qui permet d'accéder à certaines variables et fonctions liées au système, notamment ici sys.stdin

# La boucle for itère sur chaque ligne disponible dans l'entrée standard (stdin).
# sys.stdin est un objet fichier qui permet de lire l'entrée standard ligne par ligne, souvent l'entrée clavier ou redirection de fichier.
for line in sys.stdin:
    # On lit une ligne à la fois, cette ligne est une chaîne de caractères (string).
    # La méthode split() découpe cette chaîne en une liste de sous-chaînes (list of strings),
    # en se basant par défaut sur les espaces (whitespace) comme séparateurs.
    # On suppose que chaque ligne contient deux valeurs séparées par un espace.
    [p, q] = line.split()  # Le résultat est une liste de deux éléments attribués successivement aux variables p et q.

    # Conversion de la chaîne p en nombre flottant (float), c'est-à-dire un nombre à virgule flottante.
    # Cela permet de faire des comparaisons numériques ou des opérations mathématiques.
    a = float(p)

    # Même conversion pour q en nombre flottant, stocké dans b.
    b = float(q)

    # On entre dans une série de conditions if...elif...else pour classer les valeurs numériques (a, b).
    # Le symbole & est un opérateur "et" bit-à-bit, utilisé ici pour combiner deux expressions booléennes.
    # Cependant, en Python, pour des expressions booléennes il est recommandé d'utiliser "and" au lieu de "&" pour la lisibilité.
    # Chaque condition vérifie que a est inférieur à une valeur seuil ET que b est inférieur à un autre seuil.

    if (a < 35.5) & (b < 71.0):
        # Si les deux conditions sont vraies, on affiche la chaîne 'AAA' sur la sortie standard.
        print('AAA')
    elif (a < 37.5) & (b < 77.0):
        # Sinon, si cette autre paire de conditions est remplie, on affiche 'AA'.
        print('AA')
    elif (a < 40.0) & (b < 83.0):
        # Sinon, si a < 40.0 et b < 83.0, on affiche 'A'.
        print('A')
    elif (a < 43.0) & (b < 89.0):
        # Sinon, si a < 43.0 et b < 89.0, on affiche 'B'.
        print('B')
    elif (a < 50.0) & (b < 105.0):
        # Sinon, si a < 50.0 et b < 105.0, on affiche 'C'.
        print('C')
    elif (a < 55.0) & (b < 116.0):
        # Sinon, si a < 55.0 et b < 116.0, on affiche 'D'.
        print('D')
    elif (a < 70.0) & (b < 148.0):
        # Sinon, si a < 70.0 et b < 148.0, on affiche 'E'.
        print('E')
    else:
        # Enfin, si aucune des conditions précédentes n'a été remplie, on affiche 'NA' (Not Applicable ou Non attribué).
        print('NA')