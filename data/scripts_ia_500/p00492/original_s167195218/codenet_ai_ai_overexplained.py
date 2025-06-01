import sys
# Modifie la limite maximale de récursivité du programme.
# Par défaut, Python limite le nombre d'appels récursifs pour éviter un dépassement de pile.
# Ici, on l'augmente à 100000 pour permettre des appels récursifs profonds sans erreur.
sys.setrecursionlimit(100000)

# Lit une ligne d'entrée standard, attendue contenir deux nombres séparés par un espace.
# La fonction input() lit une chaîne de caractères.
# La fonction split() fractionne cette chaîne en une liste de sous-chaînes selon les espaces.
# La fonction map(int, ...) convertit chaque sous-chaîne en entier.
# L'affectation multiple permet d'assigner ces deux entiers à W (largeur) et H (hauteur).
W, H = map(int, input().split())

# Initialise la variable m qui sera une liste de listes (matrice).
# Pour chaque ligne verticale y allant de 0 à H-1, on lit une ligne d'entrée :
# - input() lit la ligne.
# - split() la découpe en éléments.
# - map(int, ...) convertit ces éléments en entiers.
# - list() convertit l'itérable résultant en liste d'entiers.
# Le résultat est une liste de H lignes, chacune contenant W entiers.
m = [list(map(int, input().split())) for i in range(H)]

# Définition des différences de coordonnées pour les déplacements possibles.
# dx est une liste contenant deux listes internes,
# correspondant aux déplacements horizontaux selon la parité de la ligne y :
# - pour une ligne paire (y % 2 == 0), on utilise dx[0]
# - pour une ligne impaire, on utilise dx[1]
# dy contient les déplacements verticaux correspondants, communs aux deux cas.
# Ceci correspond probablement aux mouvements sur une grille hexagonale ou particulière.
dx = [[1, 1, 1, 0, -1, 0], [0, 1, 0, -1, -1, -1]]
dy = [-1, 0, 1, 1, 0, -1]

# Définition d'une fonction récursive nommée dfs (depth-first search : parcours en profondeur).
# Cette fonction explore la matrice à partir d'une cellule (x, y).
def dfs(x, y):
    # Vérifie si la valeur dans la cellule (y, x) n'est pas zéro.
    # La matrice m est indexée m[y][x], car les listes internes représentent les lignes.
    # Si la cellule n'a pas la valeur 0, l'exploration en profondeur échoue ici (retourne immédiatement).
    if m[y][x] != 0:
        return
    # Sinon, on marque la cellule visitée en changeant sa valeur en 2.
    m[y][x] = 2
    # On parcourt tous les voisins possibles (xx, yy) calculés en combinant dx et dy.
    # zip(dx[y % 2], dy) associe chaque déplacement horizontal à un déplacement vertical.
    # y % 2 sert à choisir entre les deux listes dx (en fonction de si y est pair ou impair).
    for xx, yy in zip(dx[y % 2], dy):
        # Calcule les coordonnées du voisin correspondant.
        tx, ty = x + xx, y + yy
        # Vérifie que les coordonnées du voisin sont dans les limites de la matrice.
        if 0 <= tx < W and 0 <= ty < H:
            # Appel récursif de dfs pour visiter le voisin si c'est possible.
            dfs(tx, ty)

# Parcours des colonnes sur la première ligne (y=0) et la dernière ligne (y=H-1).
# Appelle dfs pour explorer les régions connectées aux bords supérieur et inférieur.
for x in range(W):
    dfs(x, 0)
    dfs(x, H - 1)

# Parcours des lignes sur la première colonne (x=0) et la dernière colonne (x=W-1).
# Appelle dfs pour explorer les régions connectées aux bords gauche et droit.
for y in range(H):
    dfs(0, y)
    dfs(W - 1, y)

# Importation de la fonction product depuis le module itertools.
# product(range(W), range(H)) crée un produit cartésien permettant de parcourir
# toutes les paires possibles (x, y) où x est dans [0, W-1] et y dans [0, H-1].
from itertools import product

# Initialisation d'un compteur n à zéro.
# Ce compteur va probablement servir à compter quelque chose en relation avec les cellules.
n = 0

# Boucle double imbriquée simulée par product pour parcourir toutes les coordonnées possible dans la grille.
for x, y in product(range(W), range(H)):
    # Si la valeur dans la cellule courante n'est pas égale à 1, on continue à la prochaine itération.
    # Cela signifie que seules les cellules à valeur 1 sont considérées pour la suite.
    if m[y][x] != 1:
        continue
    # Stocke dans fn la valeur actuelle de n (peut servir à mémoriser l'état avant test).
    fn = n
    # Pour chaque voisin défini par la combinaison des décalages dx/dy selon la parité de y.
    for xx, yy in zip(dx[y % 2], dy):
        # Calcule les coordonnées du voisin.
        tx, ty = x + xx, y + yy
        # Vérifie si le voisin est à l'intérieur des limites.
        if 0 <= tx < W and 0 <= ty < H:
            # Si la cellule voisine a la valeur 2, on incrémente n de un.
            # La valeur 2 correspond probablement aux cellules visités reliées aux bords.
            if m[ty][tx] == 2:
                n += 1
        else:
            # Si le voisin est hors limites, on incrémente également n.
            n += 1

# Affiche la valeur finale du compteur n.
print(n)