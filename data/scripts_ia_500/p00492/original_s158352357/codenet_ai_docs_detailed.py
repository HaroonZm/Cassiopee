import sys

# Augmente la limite maximale de récursion afin de permettre des recherches profondes dans la grille
sys.setrecursionlimit(1000000)

# Constante représentant un mur dans la grille
WALL = 100

# Lecture des dimensions de la grille : largeur (w) et hauteur (h)
w, h = map(int, input().split())

# Construction de la grille avec un "brouillard" de murs (WALL) sur les bords
# Chaque ligne de la grille est lue et entourée de murs à gauche et à droite
lst = [[WALL] + list(map(int, input().split())) + [WALL] for i in range(h)]
# Ajout d'une ligne de murs en haut
lst.insert(0, [WALL] * (w + 2))
# Ajout d'une ligne de murs en bas
lst.append([WALL] * (w + 2))

# Matrice pour garder la trace des états visités lors de la recherche
# 0 : non visité, 1 : en cours de visite, 2 : terrain avec valeur 1, 3 : mur
visited = [[0] * (w + 2) for _ in range(h + 2)]

# Liste temporaire pour stocker les coordonnées visités dans la recherche récursive
hold = []
app = hold.append  # Raccourci pour ajouter des éléments à hold

def search(x, y):
    """
    Recherche récursive qui explore une région connectée à partir de la position (x, y).
    Utilise un système d'état pour marquer les cellules visitées :
    - 3 : mur (imperméable)
    - 2 : cellule avec valeur 1 (obstacle)
    - 1 : cellule vide explorée pendant la recherche
    
    Cette fonction identifie si la zone connectée contient un mur ou un obstacle,
    et remplit la liste 'hold' avec toutes les cellules visitées pour pouvoir ensuite les marquer.

    Args:
        x (int): Coordonnée verticale dans la grille.
        y (int): Coordonnée horizontale dans la grille.

    Returns:
        int: Un code représentant l'état trouvé dans la région :
             3 si un mur est rencontré,
             2 si un obstacle (valeur 1) est rencontré,
             0 sinon (région vide).
    """
    # Si la cellule est un mur, marquer et retourner 3
    if lst[x][y] == WALL:
        visited[x][y] = 3
        return 3

    # Si la cellule contient un obstacle (valeur 1), marquer et retourner 2
    if lst[x][y] == 1:
        visited[x][y] = 2
        return 2

    # Marquer la cellule comme visitée (en cours)
    visited[x][y] = 1
    # Ajouter la cellule à la liste hold pour traitement ultérieur
    app((x, y))

    # Définir les positions voisines selon la parité de la ligne (hexagonal décalé)
    if not x % 2:
        # lignes paires
        pairs = [
            (x - 1, y - 1), (x - 1, y),
            (x, y - 1), (x, y + 1),
            (x + 1, y - 1), (x + 1, y)
        ]
    else:
        # lignes impaires
        pairs = [
            (x - 1, y), (x - 1, y + 1),
            (x, y - 1), (x, y + 1),
            (x + 1, y), (x + 1, y + 1)
        ]
    
    # Variable pour stocker le code d'état le plus élevé rencontré autour
    ret = 0
    for t in pairs:
        tx, ty = t[0], t[1]
        v = visited[tx][ty]
        a = 0
        if not v:
            # Si voisin non visité, appel récursif
            a = search(tx, ty)
        elif v == 3:
            a = 3
        elif v == 2:
            a = 2
        # On conserve l'état 'maximal' trouvé parmi les voisins
        if a > ret:
            ret = a
    return ret

def main():
    """
    Fonction principale qui exécute l'algorithme complet :
    1. Parcourt la grille pour trouver et explorer toutes les régions vides non visitées.
    2. Marque les régions explorées avec leur état (mur/obstacle/vide).
    3. Calcule le nombre d'arêtes bordant les murs ou bords de la grille.

    Affiche le résultat final, correspondant au nombre total d'arêtes qui
    bordent un mur ou un espace vide directement adjacent à un obstacle ou mur.
    """
    # Exploration de toute la grille à partir de chaque cellule vide non visitée
    for x in range(1, h + 1):
        for y in range(1, w + 1):
            # Ne lancer une recherche que si la cellule est vide (0) et non visitée
            if not visited[x][y] and not lst[x][y]:
                stat = search(x, y)  # Lancer la recherche depuis la position
                # Marquer tous les points visités dans hold avec le statut de la région
                for point in hold:
                    visited[point[0]][point[1]] = stat
                hold.clear()

    # Compteur des arêtes adjacentes à au moins un mur ou une zone extérieure
    ans = 0
    for x in range(1, h + 1):
        for y in range(1, w + 1):
            # On s'intéresse seulement aux cellules non vides (1 ou autre)
            if lst[x][y]:
                # Définition des voisins selon la parité de la ligne (hexagonal décalé)
                if not x % 2:
                    pairs = [
                        (x - 1, y - 1), (x - 1, y),
                        (x, y - 1), (x, y + 1),
                        (x + 1, y - 1), (x + 1, y)
                    ]
                else:
                    pairs = [
                        (x - 1, y), (x - 1, y + 1),
                        (x, y - 1), (x, y + 1),
                        (x + 1, y), (x + 1, y + 1)
                    ]
                # Compter les arêtes donnant sur un mur ou sur une région non visitée / mur
                for t in pairs:
                    tx, ty = t[0], t[1]
                    if (visited[tx][ty] in [0, 3]) and (lst[tx][ty] in [WALL, 0]):
                        ans += 1

    # Affichage du total des arêtes détectées
    print(ans)

# Exécution de la fonction principale
main()