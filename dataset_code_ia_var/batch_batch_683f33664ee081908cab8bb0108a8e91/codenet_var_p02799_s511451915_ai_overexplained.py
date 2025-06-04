import sys  # On importe le module sys pour accéder à stdin et exit

input = sys.stdin.readline  # On redéfinit input pour lire une ligne optimisée depuis l'entrée standard

# Lecture des deux premiers entiers depuis l'entrée standard.
# 'N' est le nombre de sommets (ou de noeuds), et 'M' est le nombre d'arêtes du graphe.
N, M = map(int, input().split())

# Lecture d'une liste d'entiers de longueur N correspondant à des valeurs pour chaque sommet.
# Utilisation de map pour convertir chaque élément lu dans input().split() en int.
D = list(map(int, input().split()))

# Lecture des M arêtes du graphe. Chaque arête est saisie comme un couple de sommets (x, y).
# On utilise 'sorted' pour garantir que l'arête est stockée dans l'ordre croissant (important pour utiliser comme clé).
# On crée M tuples (arêtes), stockés dans une liste EDGE.
EDGE = [tuple(sorted(map(int, input().split()))) for i in range(M)]

# On initialise un dictionnaire pour associer chaque arête à un index unique (de 0 à M-1).
DICE = dict()
for i in range(M):
    # La clé est l'arête elle-même (tuple de deux entiers) et la valeur est son indice d'apparition.
    DICE[EDGE[i]] = i

# Construction de la liste d'adjacence pour représenter le graphe. 
# E[i] contiendra la liste des sommets adjacents au sommet i.
# On utilise N+1 pour que les indices aillent de 1 à N (l'index 0 ne sera pas utilisé).
E = [[] for i in range(N + 1)]
for x, y in EDGE:
    # Pour chaque arête (x, y), on ajoute y à la liste des voisins de x et réciproquement.
    E[x].append(y)
    E[y].append(x)

# On crée une liste de tuples contenant les valeurs de D (les dés) et leur position originale.
# enumerate(D) va donner (index, valeur). On ajoute 1 à l'index car nos sommets commencent à 1.
P = [(x, ind + 1) for ind, x in enumerate(D)]
# On trie P par valeur (valeur du dé) croissante.
P.sort()

# On rajoute un zéro devant D pour que D[1] soit le dé pour le sommet 1, etc.
D = [0] + D

# On initialise une liste DECIDED pour marquer le "couleur" ou l'état de chaque sommet.
# Elle contient des chaînes vides au départ; DECIDED[i] vaudra typiquement "B" ou "W" plus tard.
DECIDED = [""] * (N + 1)

# DIS est une liste qui enregistrera les valeurs associées à chaque arête, initialisées à -1.
DIS = [-1] * M

# On parcourt tous les sommets dans l'ordre croissant de la valeur du dé.
for x, po in P:
    flag = 0  # Ce flag servira à savoir s'il y a au moins un voisin déjà colorié.

    # On parcourt tous les voisins du sommet po.
    for to in E[po]:
        # Si un voisin de po est déjà colorié ("B" ou "W"), on note le flag.
        if DECIDED[to] != "":
            flag = 1
            break  # On n'a pas besoin d'en chercher d'autres.

    # Si po n'a aucun voisin déjà colorié :
    if flag == 0:
        # Pour chaque voisin non colorié de po :
        for to in E[po]:
            # Si le dé du voisin to est égal à x (celui de po)
            if D[to] == x:
                # On attribue à DIS pour cette arête la valeur x.
                DIS[DICE[tuple(sorted([po, to]))]] = x
                # On décide arbitrairement une coloration : po en "B" (noir), to en "W" (blanc)
                DECIDED[po] = "B"
                DECIDED[to] = "W"
                break  # On sort de la boucle
        else:
            # Si aucun voisin n'a pu être affecté correctement, on affiche -1 et on termine le programme.
            print(-1)
            sys.exit()
    else:
        # Cas où au moins un voisin de po a déjà été colorié :
        for to in E[po]:
            # Si le voisin to est colorié, mais pas po, on donne à po la couleur opposée à celle de to.
            if DECIDED[to] != "" and DECIDED[po] == "":
                # Si le voisin est "B" (noir), po sera "W" (blanc), et vice versa.
                if DECIDED[to] == "B":
                    DECIDED[po] = "W"
                else:
                    DECIDED[po] = "B"
                # On assigne à DIS pour cette arête la valeur x.
                DIS[DICE[tuple(sorted([po, to]))]] = x
                break
            # Si le voisin to est colorié, po aussi, et ils ont la même couleur :
            elif DECIDED[to] != "" and DECIDED[po] == DECIDED[to]:
                # Si x est plus petit ou égal à D[to], on ne fait rien pour cette itération.
                if x <= D[to]:
                    continue
                # Sinon, on met le décalage (x - D[to]) sur cette arête.
                DIS[DICE[tuple(sorted([po, to]))]] = x - D[to]
                break
            # Si les deux sont déjà colorés et ont une couleur différente :
            elif DECIDED[to] != "" and DECIDED[po] != DECIDED[to]:
                # Si x est <= D[to], rien à faire pour cette arête.
                if x <= D[to]:
                    continue
                # Sinon, on attribue x à cette arête.
                DIS[DICE[tuple(sorted([po, to]))]] = x
                break

# Après l'affectation des couleurs et des valeurs d'arêtes, on affiche le résultat :
# On affiche la suite des couleurs décidées pour chaque sommet (sauf l'indice 0, inutilisé).
print("".join(DECIDED[1:]))

# Pour chaque arête, on affiche la valeur correspondante dans DIS :
# Si aucune valeur n'a été assignée (toujours à -1), on affiche 10^9.
for d in DIS:
    if d == -1:
        print(10 ** 9)
    else:
        print(d)