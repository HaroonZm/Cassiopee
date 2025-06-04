# Demander à l'utilisateur d'entrer trois valeurs séparées par des espaces dans une seule ligne.
# Ces valeurs sont supposées correspondre à la largeur (w), la hauteur (h) du cadre, et un caractère (a).
# La fonction input() attend que l'utilisateur saisisse la ligne et appuie sur Entrée.
# La méthode split() sépare la chaîne reçue à chaque espace, produisant une liste de trois éléments.
w, h, a = input().split()

# Convertir la largeur (w) et la hauteur (h) de chaînes de caractères en entiers.
# Ainsi, w représente la largeur totale du cadre et h sa hauteur totale.
w, h = int(w), int(h)

# Lancer une boucle for pour répéter un bloc de code h fois, afin de créer chaque ligne du cadre.
# La variable i prendra successivement les valeurs de 0 jusqu'à h-1 (inclus).
for i in range(h):
    # Vérifier si la ligne courante (i) est la première (i == 0) ou la dernière (i == h - 1).
    # On crée un ensemble contenant 0 et h-1, puis on teste si i en fait partie.
    if i in {0, h - 1}:
        # Si c'est la première ou la dernière ligne, imprimer le contour supérieur ou inférieur du cadre.
        # Le cadre commence par "+", puis affiche (w - 2) fois le caractère "-", puis se termine par "+".
        # Le nombre (w - 2) correspond à la portion de la ligne située entre les coins gauche et droit.
        print("+" + "-" * (w - 2) + "+")
    else:
        # Si la ligne courante n'est ni la première ni la dernière :
        # Vérifier si c'est la ligne du centre, destinée à afficher le caractère (a).
        # On compare i et h // 2 (division entière de la hauteur par 2).
        if i == h // 2:
            # Si c'est la ligne centrale :
            # Le cadre débute par "|".
            # Afficher ((w - 2) // 2) points "." à gauche du caractère a.
            # Ajouter le caractère a au centre.
            # Puis ((w - 2) // 2) points à droite du caractère a.
            # Enfin, terminer la ligne par "|".
            print(
                "|" +                             # Bord gauche du cadre
                "." * ((w - 2) // 2) +            # Points à gauche du caractère central
                a +                              # Le caractère à afficher
                "." * ((w - 2) // 2) +            # Points à droite du caractère central
                "|"                               # Bord droit du cadre
            )
        else:
            # Pour toutes les autres lignes internes :
            # Commencer par le bord gauche du cadre "|".
            # Afficher (w - 2) points ".", soit tout l'espace entre les bords.
            # Terminer avec le bord droit "|".
            print("|" + "." * (w - 2) + "|")