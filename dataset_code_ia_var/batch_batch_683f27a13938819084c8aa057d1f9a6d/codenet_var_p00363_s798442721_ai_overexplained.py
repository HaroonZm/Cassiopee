# Demander à l'utilisateur une entrée au clavier. Cette entrée doit contenir trois valeurs séparées par des espaces.
# La première valeur correspondra à la largeur (w) du rectangle,
# la deuxième à la hauteur (h) du rectangle,
# la troisième sera le caractère central (c) à afficher au milieu du rectangle.
w, h, c = input().split(" ")

# Les valeurs récupérées précédemment sont lues comme des chaînes de caractères (str).
# Il faut donc les convertir en entiers pour w et h, car on les utilisera dans des calculs numériques.
w = int(w)
h = int(h)

# Affichage de la première ligne du rectangle.
# Le rectangle commence par le caractère '+', puis une ligne horizontale composée de tirets '-'.
# Le nombre de tirets est égal à (w - 2), car la largeur totale inclut les coins gauche et droit représentés par des '+'.
# On termine la ligne par un autre '+'.
print("+" + "-" * (w - 2) + "+")

# On utilise une boucle pour afficher les lignes du milieu du rectangle.
# La boucle doit s'exécuter pour chaque rangée intérieure, donc du haut (après la première ligne) au bas (avant la dernière ligne).
# Le nombre de lignes intérieures est (h - 2) parce que la première et la dernière ligne sont déjà traitées séparément.
for i in range(h - 2):
    # Pour chaque ligne intérieure, il faut vérifier si c'est la ligne médiane, celle qui affichera le caractère central.
    # La condition "i*2 == h-3" détermine la ligne à centrer.
    # Le calcul "i*2 == h-3" permet d'atteindre le milieu de la plage de la boucle.
    if i * 2 == h - 3:
        # Si c'est la ligne médiane, il faut centrer le caractère c.
        # On commence la ligne avec un '|', bord gauche du rectangle.
        # On calcule combien de points '.' il faut à gauche et à droite du caractère c.
        # (w - 3) est le nombre de caractères entre les deux '|' moins le caractère c lui-même.
        # On divise par deux pour équilibrer les points de chaque côté.
        # Si la largeur est impaire, il restera toujours un point supplémentaire à gauche.
        print("|" + "." * ((w - 3) // 2) + c + "." * ((w - 3) // 2) + "|")
    else:
        # Si on n'est pas sur la ligne médiane, on affiche une ligne ordinaire,
        # qui commence par '|', puis une série de points '.' (w - 2) fois,
        # puis on termine avec un '|'.
        print("|" + "." * (w - 2) + "|")

# Après toutes les lignes intérieures, on affiche la dernière ligne du rectangle.
# Cette ligne est semblable à la première : un '+', des tirets '-', et un autre '+'.
# Le nombre de tirets est encore (w - 2) pour respecter la largeur totale.
print("+" + "-" * (w - 2) + "+")