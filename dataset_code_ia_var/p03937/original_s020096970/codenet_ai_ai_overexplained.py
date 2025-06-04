# Demander à l'utilisateur de saisir deux nombres séparés par un espace, qui correspondent à la hauteur (h) et la largeur (w) de la grille
# La fonction input() lit l'entrée utilisateur sous forme de chaîne de caractères (string)
# La méthode split() sépare la chaîne en une liste de sous-chaînes selon les espaces
# La fonction map(int, ...) convertit chaque sous-chaîne en entier (int)
# Enfin, la fonction list(...) crée une liste à partir de l'objet map
h, w = list(map(int, input().split()))

# Initialisation d'une liste vide qui contiendra chaque ligne de la grille
# Pour chaque valeur de i de 0 à h-1 (c'est-à-dire h fois), on fait :
# - input() lit une ligne de la grille sous forme de chaîne de caractères
# - list() transforme cette chaîne en une liste de caractères
# Le résultat est une liste de listes de caractères, représentant la grille entière
a = [list(input()) for i in range(h)]

# Initialisation d'un compteur à 0
# Ce compteur va permettre de compter le nombre total de caractères '#' présents dans la grille
cnt = 0

# Boucle sur chaque ligne de la grille
for i in range(h):  # i prend toutes les valeurs de 0 jusqu'à h-1 inclus
    # Boucle sur chaque colonne de la ligne courante
    for j in range(w):  # j prend toutes les valeurs de 0 jusqu'à w-1 inclus
        # Vérifier si le caractère à la position (i, j) dans la grille est le caractère '#'
        if a[i][j] == '#':
            # Si oui, on incrémente le compteur de 1
            cnt += 1

# À la sortie des deux boucles, cnt contient le nombre total de '#' dans toute la grille

# Vérification de la condition spécifique du problème :
# On teste si le nombre de '#' est exactement égal à (h + w) - 1
# (Cela correspond typiquement à un chemin unique allant du coin supérieur gauche au coin inférieur droit
# en ne se déplaçant qu'à droite ou vers le bas)
if cnt == (h + w) - 1:
    # Si la condition est satisfaite, on affiche "Possible"
    print("Possible")
else:
    # Sinon, on affiche "Impossible"
    print("Impossible")