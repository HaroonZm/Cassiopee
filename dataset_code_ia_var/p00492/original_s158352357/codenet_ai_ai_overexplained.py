import sys  # Importation du module sys qui fournit l'accès à certaines variables et fonctions du système

sys.setrecursionlimit(1000000)  # Modification de la limite de récursion, c'est-à-dire le nombre maximum d'appels récursifs autorisés, ici fixé à un million, pour éviter un RecursionError lors de la récursion profonde.

WALL = 100  # Définition d'une constante appelée WALL, qui aura la valeur 100 ; elle sert à représenter les bords autour de la grille, pour faciliter la gestion des cases limites.

# Lecture des dimensions de la grille : w pour la largeur (nombre de colonnes), h pour la hauteur (nombre de lignes)
w, h = map(int, input().split())

# lst servira à contenir la grille complète, entourée de murs (valeur WALL)
# On va construire chaque ligne de la grille utilisateur en insérant une valeur WALL de chaque côté, puis ajouter une ligne WALL au dessus et en dessous de la grille.
lst = []
for i in range(h):  # Pour chaque ligne de la grille (h lignes)
    # On lit une ligne de la grille, on convertit chaque valeur en int.
    row = list(map(int, input().split()))  # On lit w éléments
    # On ajoute WALL au début et à la fin de la ligne, pour créer une bordure à gauche et à droite
    lst.append([WALL] + row + [WALL])
# On ajoute une ligne de WALL complète en haut de la grille (largeur w+2 : +2 car on a ajouté un WALL de chaque côté)
lst.insert(0, [WALL] * (w + 2))
# On ajoute une ligne de WALL complète en bas de la grille
lst.append([WALL] * (w + 2))

# Création d'une matrice visited de la même taille que lst, initialisée à 0 partout.
# visited servira à marquer l'état de chaque case lors de l'exploration :
# 0 = pas encore visitée, 1 = visite en cours, 2 = découverte comme pièce fermée, 3 = connectée au mur
visited = [[0] * (w + 2) for _ in range(h + 2)]

hold = []  # Liste temporaire pour stocker les cellules d'une même composante connexe pendant la détection
app = hold.append  # Raccourci (alias) pour la méthode append sur la liste hold, pour éviter de taper hold.append à chaque fois

def search(x, y):
    """
    Fonction de recherche en profondeur (DFS) pour explorer la composante connexe contenant la case (x, y).
    Retourne :
      - 3 si cette composante touche un mur extérieur ('ouverte')
      - 2 si elle touche une case 1 ('fermée')
      Marque toutes les cases visitées en conséquence.
    """

    # Si on tombe sur un mur (valeur WALL), c'est le bord de la grille
    if lst[x][y] == WALL:
        visited[x][y] = 3  # On marque la case comme reliée à un mur extérieur
        return 3  # On renvoie 3 pour indiquer cette situation

    # Si on tombe sur une case de valeur 1 (mur intérieur)
    if lst[x][y] == 1:
        visited[x][y] = 2  # On marque la case comme fermée
        return 2  # On renvoie 2, cette case est une bordure fermée

    # Marquage de la case comme visitée pendant cette composante
    visited[x][y] = 1
    app((x, y))  # On ajoute ce couple de coordonnées (x, y) à la liste hold pour traitement ultérieur

    # On prépare la liste des voisins selon la parité de x
    if x % 2 == 0:
        # Si x est pair, les voisins dans la grille hexagonale sont listés de cette façon
        pairs = [(x - 1, y - 1), (x - 1, y), (x, y - 1), (x, y + 1), (x + 1, y - 1), (x + 1, y)]
    else:
        # Si x est impair, les voisins diffèrent
        pairs = [(x - 1, y), (x - 1, y + 1), (x, y - 1), (x, y + 1), (x + 1, y), (x + 1, y + 1)]

    ret = 0  # Variable pour retenir le maximum de statut rencontré parmi les voisins
    for t in pairs:
        tx, ty = t[0], t[1]  # tx et ty sont les coordonnées du voisin actuel
        v = visited[tx][ty]  # On regarde l'état de visite du voisin
        a = 0  # a servira à retenir le statut du voisin
        if not v:
            # Si on n'a pas encore visité cette case
            a = search(tx, ty)  # On appelle récursivement search dessus
        elif v == 3:
            # Si la case a déjà été marquée comme connectée au mur
            a = 3
        elif v == 2:
            # Si la case a déjà été marquée comme connectée à une case 1
            a = 2
        if a > ret:
            ret = a  # On garde le maximum de statut rencontré (3 priorité sur 2)
    return ret  # Retour de la fonction, indiquant le type d'espace

def main():
    """
    Fonction principale qui exécute l'ensemble du traitement, depuis l'exploration des composantes jusqu'au comptage final.
    """

    # Première phase : déterminer le statut de chaque composante connexe de cases vides (0)
    for x in range(1, h + 1):  # On parcourt chaque ligne interne de la grille (en ignorant la bordure)
        for y in range(1, w + 1):  # On parcourt chaque colonne interne de la grille
            if not visited[x][y] and not lst[x][y]:
                # Si la case n'a pas encore été visitée et que c'est une case vide (zéro)
                stat = search(x, y)  # On recherche sa composante connexe entière et on détermine son statut général
                for point in hold:  # Pour toutes les cases de cette composante
                    visited[point[0]][point[1]] = stat  # On leur attribue ce statut (2 ou 3)
                hold.clear()  # On vide la liste hold en prévision de la prochaine composante

    # Deuxième phase : comptage des contours extérieurs
    ans = 0  # Compteur total des bords exposés
    for x in range(1, h + 1):  # Pour chaque case de la grille interne (hors bordure)
        for y in range(1, w + 1):
            if lst[x][y]:
                # Si la case courante est un mur (1, ou une valeur non nulle)
                if x % 2 == 0:
                    # Détermination de la liste des voisins selon la parité de x
                    pairs = [(x - 1, y - 1), (x - 1, y), (x, y - 1), (x, y + 1), (x + 1, y - 1), (x + 1, y)]
                else:
                    pairs = [(x - 1, y), (x - 1, y + 1), (x, y - 1), (x, y + 1), (x + 1, y), (x + 1, y + 1)]
                for t in pairs:
                    tx, ty = t[0], t[1]  # Pour chaque voisin
                    # Si ce voisin est soit non visité (0), soit un mur externe (3), et que la case dans lst est un espace ou un mur externe
                    if (visited[tx][ty] in [0, 3]) and (lst[tx][ty] in [WALL, 0]):
                        ans += 1  # On incrémente le compteur (cela correspond à un bord exposé vers l'extérieur)

    print(ans)  # Affichage du résultat final : le nombre total de bords exposés

main()  # Appel de la fonction principale afin de commencer le traitement computationnel