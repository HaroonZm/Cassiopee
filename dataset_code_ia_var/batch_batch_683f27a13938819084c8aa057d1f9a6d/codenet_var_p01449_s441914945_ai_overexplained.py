# Import de la classe deque du module collections
# Cela permet d'utiliser une file doublement chaînée
from collections import deque

# Lecture du nombre d'éléments N à partir de l'entrée standard de l'utilisateur.
# La fonction int() convertit la chaîne de caractères saisie en un entier.
N = int(input())

# Définition d'une constante INF qui prendra une valeur arbitrairement grande (10^9).
# Cela représentera, dans le tableau B, le fait qu'une case n'a pas encore été atteinte avec un coût moindre.
INF = 10**9

# Création d'une liste A qui contiendra les valeurs entières saisies.
# On utilise une compréhension de liste pour appeler int(input()) N fois, donc on collecte N entiers fournis en entrée.
# Ensuite, on ajoute à la fin de cette liste 6 zéros supplémentaires ([0]*6).
# Cela assure que lors de l'accès à des indices jusqu'à x+6, on ne sortira jamais des bornes de la liste (évite un IndexError).
A = [int(input()) for _ in range(N)] + [0]*6

# Création d'une liste B de taille N+6.
# Elle est initialisée avec la valeur INF (donc chaque case vaut 10^9 au départ, c'est un coût "inatteignable").
# Cette liste B stockera le coût minimal pour chaque position atteinte dans notre problème.
B = [INF]*(N+6)

# On fixe la valeur de départ (position 0) à 0 dans B[0], parce que le coût (le nombre d'étapes) pour atteindre la position 0 est 0.
B[0] = 0

# Initialisation de la file de priorité 0-1 BFS avec deque.
# Q est une deque contenant une liste à deux éléments : [0, 0].
# 0 : position de départ, 0 : coût pour y arriver.
Q = deque([[0, 0]])

# Lancement d'une boucle qui sera exécutée tant que la file deque n'est pas vide.
# Cela servira à explorer tous les états atteignables à partir de la position de départ.
while Q:
    # Pour chaque itération, on enlève (popleft) le premier élément de la deque Q.
    # x : position actuelle
    # y : coût pour atteindre cette position (nombre de coups/étapes)
    x, y = Q.popleft()

    # Si la position actuelle x est supérieure ou égale à la dernière case (N-1),
    # alors nous avons atteint (ou dépassé) la case finale, le but du jeu.
    # On affiche le coût associé (le nombre minimum d'étapes) et on quitte la boucle avec break.
    if x >= N-1:
        print(y)
        break

    # Si le coût déjà trouvé pour atteindre la position x est plus petit que le coût actuel y,
    # alors on n'a pas besoin de traiter ce chemin moins optimal : on continue sans rien faire.
    if B[x] < y:
        continue

    # Si la valeur de A[x] (la case courante) est 0 :
    # Cela signifie qu'il s'agit d'une case "normale" (pas de téléportation).
    if A[x] == 0:
        # On parcourt toutes les possibilités de se déplacer de 1 à 6 cases depuis x (comme avec un dé à 6 faces).
        for i in range(1, 7):
            # Si le coût actuel y augmenté de 1 est inférieur au coût déjà stocké pour atteindre la position x+i,
            # alors on a trouvé un chemin plus rapide pour y arriver.
            if y + 1 < B[x+i]:
                # On met à jour le coût d'arrivée à x+i avec ce nouveau coût.
                B[x+i] = y + 1
                # On ajoute ce nouvel état (position x+i avec coût y+1) à la queue Q.
                # On ajoute à droite (à la fin), car ce coup coûte 1, donc moins prioritaire que les coups à coût nul.
                Q.append([x+i, y+1])
    else:
        # Sinon (A[x] != 0), cela signifie que la case possède une "téléportation" ou un effet spécial :
        # En arrivant en x, on saute immédiatement à la case x+A[x] sans coût supplémentaire.
        # Si le coût actuel y est inférieur au coût déjà trouvé pour x+A[x], on met à jour.
        if y < B[x+A[x]]:
            # On met à jour le coût pour atteindre x+A[x], c'est-à-dire on garde le même coût y.
            B[x+A[x]] = y
            # On ajoute la combinaison [x+A[x], y] au début de la deque (appendleft)
            # car ce déplacement coûte 0 (priorité plus élevée dans la BFS 0-1).
            Q.appendleft([x+A[x], y])