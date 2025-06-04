# Demander à l'utilisateur une entrée au clavier et la stocker dans la variable d'entrée.
# La valeur entrée doit contenir trois éléments séparés par des espaces : la largeur (W), la hauteur (H) et un caractère (c).
# Exemple d'entrée : "5 3 *"
W, H, c = input().split()

# Convertir les variables W et H, qui sont des chaînes de caractères après l'utilisation de split(), en entiers.
W = int(W)  # Largeur de la structure à dessiner
H = int(H)  # Hauteur de la structure à dessiner

# Boucle externe pour chaque ligne de la structure. La variable i représente l'index de la ligne en cours.
for i in range(H):  # the loop will iterate from 0 up to (H-1) inclusively
    # Boucle interne pour chaque colonne de la structure. La variable j représente l'index de la colonne en cours.
    for j in range(W):  # the loop will iterate from 0 up to (W-1) inclusively

        # Cette condition vérifie si la position actuelle (j, i) se trouve à un des coins du rectangle.
        # Les coins sont : (0,0) en haut à gauche, (0,H-1) en bas à gauche,
        # (W-1,0) en haut à droite, et (W-1,H-1) en bas à droite.
        if (j, i) == (0, 0) or (j, i) == (0, H - 1) or (j, i) == (W - 1, 0) or (j, i) == (W - 1, H - 1):
            # Afficher le caractère '+' pour les coins, sans retour à la ligne.
            print('+', end='')
        # Cette condition vérifie si la colonne courante est la première (j == 0) ou la dernière (j == W - 1).
        # Mais on n'entre ici que si on n'est pas à un coin (sinon la condition ci-dessus se déclenche).
        elif j in (0, W - 1):
            # Afficher le caractère '|' pour les bords verticaux, sans retour à la ligne.
            print('|', end='')
        # Cette condition vérifie si la ligne courante est la première (i == 0) ou la dernière (i == H - 1).
        # Mais on n'entre ici que si on n'est pas à un coin.
        elif i in (0, H - 1):
            # Afficher le caractère '-' pour les bords horizontaux, sans retour à la ligne.
            print('-', end='')
        # Cette condition teste si la position courante est le centre du rectangle (approximatif si dimensions paires).
        elif (j, i) == ((W - 1) // 2, (H - 1) // 2):
            # Afficher le caractère choisi c à la position centrale.
            print(c, end='')
        # Si aucune condition précédente n'est vérifiée.
        else:
            # Afficher un point '.' pour le reste des positions (l'intérieur sans le centre), sans retour à la ligne.
            print('.', end='')

    # Une fois qu'on a traité toutes les colonnes d'une ligne, passer à la ligne suivante.
    print()