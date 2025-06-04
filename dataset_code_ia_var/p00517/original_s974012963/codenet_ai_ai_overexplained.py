# Ce programme résout un problème où il faut calculer la distance totale parcourue entre des points sur une grille,
# en tenant compte de la direction des mouvements.

# Lecture des entrées : lire trois entiers à partir de l'entrée standard.
# L'utilisateur doit entrer les valeurs séparées par des espaces.
# W représente la largeur de la grille (non utilisée par la suite),
# H représente la hauteur de la grille (non utilisée non plus),
# N est le nombre de points que nous devons traiter ensuite.
W, H, N = map(int, input().split())

# Création d'une liste 'XY' qui va stocker 'N' sous-listes.
# Chaque sous-liste contient deux entiers, correspondant aux coordonnées x et y d'un point.
# On utilise une liste de compréhension pour remplir 'XY'.
# Pour chaque valeur 'i' de 0 jusqu'à N-1 :
#   - On lit une ligne d'entrée, la découpe en éléments séparés par des espaces,
#   - On convertit ces éléments en entiers,
#   - On regroupe ces entiers dans une sous-liste.
XY = [list(map(int, input().split())) for i in range(N)]

# Initialisation de la variable ans qui servira à accumuler la distance totale parcourue.
ans = 0

# Boucle principale : on parcourt chaque point de la liste 'XY' grâce à l'indice 'i'.
for i in range(N):
    # Si 'i' vaut 0, cela signifie qu'on traite le tout premier point de la séquence.
    if i == 0:
        # On affecte aux variables sx et sy les coordonnées x et y du premier point.
        sx, sy = XY[0]
    else:
        # Pour tous les points après le premier, on veut calculer la distance entre le dernier point visité
        # (coordonnées sx et sy) et le nouveau point vers lequel on va se déplacer (coordonnées gx et gy).
        gx, gy = XY[i]
        
        # Calcul de la différence horizontale (dx) entre la destination et la source.
        dx = gx - sx
        # Calcul de la différence verticale (dy) entre la destination et la source.
        dy = gy - sy
        
        # On examine le produit dx*dy afin de déterminer si les deux différences sont de même signe (ou l'une vaut zéro).
        # - Si c'est le cas (produit >= 0), le déplacement peut se faire en diagonale puis éventuellement horizontalement ou verticalement.
        if dx * dy >= 0:
            # Dans ce cas, le nombre minimal d'étapes correspond au maximum de la valeur absolue de dx et dy.
            ans += max(abs(dx), abs(dy))
        else:
            # Sinon, il faut se déplacer horizontalement puis verticalement (ou inversement), donc on additionne les valeurs absolues.
            ans += (abs(dx) + abs(dy))
        # Mise à jour des coordonnées de la source avec celles du point actuel,
        # afin de pouvoir calculer la prochaine distance lors de la prochaine itération.
        sx, sy = gx, gy

# Affichage de la distance totale accumulée, c'est la réponse attendue.
print(ans)