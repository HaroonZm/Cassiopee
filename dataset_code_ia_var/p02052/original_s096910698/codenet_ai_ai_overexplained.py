# Demander à l'utilisateur de saisir deux entiers séparés par un espace, représentant la hauteur (H) et la largeur (W) de la grille.
# La fonction input() lit une ligne entrée par l'utilisateur.
# split() sépare la ligne en une liste de chaînes, à l'endroit des espaces.
# map(int, ...) convertit chaque chaîne en entier.
# Enfin, H et W reçoivent ces deux valeurs.
H, W = map(int, input().split())

# Initialisation de la grille.
# Utilisation d'une compréhension de liste pour lire H lignes de saisie.
# À chaque itération, input() lit une ligne de la grille.
# list(input()) convertit chaque ligne en liste de caractères.
# MAP est alors une liste de listes de caractères représentant la grille.
MAP = [list(input()) for i in range(H)]

# Création d'une liste vide pour stocker les positions des caractères 'B' trouvés dans la grille.
BLIST = []

# Parcourir toutes les lignes de la grille (de 0 à H-1).
for i in range(H):
    # Parcourir toutes les colonnes de la grille (de 0 à W-1).
    for j in range(W):
        # Vérifier si le caractère à la position (i, j) est 'B'.
        if MAP[i][j] == "B":
            # Si c'est le cas, ajouter la position [i, j] à la liste BLIST.
            BLIST.append([i, j])

# Trier maintenant la liste BLIST en utilisant comme clé la somme des indices de ligne et de colonne.
# key=lambda x: x[0]+x[1] désigne une fonction qui renvoie la somme de la ligne (x[0]) et de la colonne (x[1]) pour chaque position x dans BLIST.
# Le tri se fait du plus petit au plus grand selon cette somme.
BLIST.sort(key=lambda x: x[0] + x[1])

# Après le tri, le premier (BLIST[0]) et dernier (BLIST[-1]) éléments de la liste sont ceux qui maximisent la différence de la somme (ligne+colonne).
# On calcule la distance de Manhattan (somme des valeurs absolues des différences des lignes et des colonnes) entre ces deux positions.
ANS = abs(BLIST[0][0] - BLIST[-1][0]) + abs(BLIST[0][1] - BLIST[-1][1])

# On trie maintenant à nouveau la liste BLIST, mais cette fois en utilisant comme clé la différence (ligne-colonne).
BLIST.sort(key=lambda x: x[0] - x[1])

# On calcule de nouveau la distance de Manhattan entre la première et la dernière position après ce tri.
# Si cette nouvelle distance est supérieure à la précédente, on met à jour ANS pour qu'il contienne la plus grande valeur calculée.
ANS = max(ANS, abs(BLIST[0][0] - BLIST[-1][0]) + abs(BLIST[0][1] - BLIST[-1][1]))

# Afficher le résultat final, qui est la plus grande distance de Manhattan trouvée entre deux 'B' de la grille selon les deux tris testés.
print(ANS)