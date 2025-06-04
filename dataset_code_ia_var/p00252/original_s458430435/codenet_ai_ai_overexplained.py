# Demander à l'utilisateur de saisir trois nombres séparés par des espaces
# La fonction input() lit une ligne de texte depuis l'entrée standard (typiquement le clavier)
# La méthode split() découpe cette chaîne en une liste de sous-chaînes (ici, les nombres saisis) selon les espaces
# La fonction map(int, ...) applique la fonction int() à chaque élément de la liste produite par split(), c'est-à-dire convertit chaque chaîne de caractères en entier
# Les trois premiers résultats de ce mapping sont ensuite assignés aux variables b1, b2 et b3 via un unpacking multiple
b1, b2, b3 = map(int, input().split())

# Vérification du premier bit
# On teste si la variable b1 est égale à 1
if b1 == 1:
    # Si b1 vaut 1, on vérifie le deuxième bit b2
    # Ici, on entre dans ce bloc seulement si b1 == 1
    if b2 == 1:
        # Si b2 vaut aussi 1, on considère que la condition est remplie pour ouvrir, donc on affiche 'Open'
        print('Open')
    else:
        # Si b2 ne vaut pas 1, c'est-à-dire qu'il vaut 0 ou autre, on considère que la condition n'est pas remplie
        # On affiche alors 'Close'
        print('Close')
else:
    # Si b1 ne vaut pas 1 (c'est-à-dire qu'il vaut 0 ou autre chiffre), on entre dans ce bloc
    # On vérifie alors la valeur du deuxième bit b2
    if b2 == 0:
        # Si b2 vaut 0, on vérifie maintenant la valeur du troisième bit b3
        if b3 == 1:
            # Si b3 vaut 1, la combinaison des conditions est suffisante pour afficher 'Open'
            print('Open')
        else:
            # Si b3 ne vaut pas 1 (0 ou autre), on n'affiche pas 'Open' mais 'Close'
            print('Close')
    else:
        # Si b2 ne vaut pas 0 (c'est-à-dire qu'il vaut 1 ou autre), on affiche directement 'Close'
        print('Close')