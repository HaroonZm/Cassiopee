import sys  # On importe le module sys pour accéder à l'entrée standard (stdin)
input = sys.stdin.readline  # On redéfinit input pour une lecture rapide des lignes sur l'entrée standard

# On lit les 7 premiers entiers sur une seule ligne à l'entrée standard, séparés par des espaces.
# map(int, ...) convertit chaque élément (au format chaîne) en entier.
# X, Y, Z sont respectivement les nombres de stations S, de stations C, de stations U
# N est le nombre de stations de type S que l'on va lire ensuite
# M est le nombre de stations de type C que l'on va lire ensuite
# S est l'indice de la station S de départ
# T est l'indice de la station C d'arrivée
X, Y, Z, N, M, S, T = map(int, input().split())

# On construit la liste des stations S :
# On ajoute comme 0ème élément une station fictive [0,0,0]
# Ensuite, on ajoute chaque station lue parmi les N suivantes en lisant trois entiers sur chaque ligne
# On y ajoute également un index i+1 (pour les identifier plus tard) ainsi que la marque 0 qui indique leur type S
CS = [[0,0,0]] + [list(map(int, input().split())) + [i+1] + [0] for i in range(N)]

# Même procédé pour les stations C :
# On a une station fictive [0,0,0] en tête
# On ajoute pour chacune des M stations, un identifiant i+1 et la marque 1 qui indique le type C
CC = [[0,0,0]] + [list(map(int, input().split())) + [i+1] + [1] for i in range(M)]

# Préparation de listes d'adjacence pour accéder rapidement d'une station à une autre selon les restrictions

# CS_SLIST : Pour chaque index x de 1 à X, liste des stations S accessibles par leur coordonnée x (dimension S)
CS_SLIST = [[] for i in range(X+1)]  # +1 car on utilise des indices à partir de 1, on laisse l'indice 0 vide
# CS_CLIST : Pour chaque index y de 1 à Y, liste des stations S accessibles par leur coordonnée y (dimension C)
CS_CLIST = [[] for i in range(Y+1)]
# CC_CLIST : Pour chaque index y de 1 à Y, liste des stations C accessibles par leur coordonnée x (dimension C)
CC_CLIST = [[] for i in range(Y+1)]
# CC_ULIST : Pour chaque index z de 1 à Z, liste des stations C accessibles par leur coordonnée y (dimension U)
CC_ULIST = [[] for i in range(Z+1)]

# On peuple les listes précédentes pour les stations S (sauf la station fictive [0,0,0])
# On ignore le marqueur type (dernier élément _) dans l'étape ci-dessous
for x, y, z, _ in CS[1:]:
    CS_SLIST[x].append(z)  # On enregistre pour l'indice x (dimension S) le numéro de la station S (z)
    CS_CLIST[y].append(z)  # On enregistre pour l'indice y (dimension C) le numéro de la station S (z)

# Idem pour les stations C
for x, y, z, _ in CC[1:]:
    CC_CLIST[x].append(z)  # Pour l'indice x (dimension C), on liste les stations C identifiées par z
    CC_ULIST[y].append(z)  # Pour l'indice y (dimension U), on liste les stations C identifiées par z

# On importe la bibliothèque heapq pour utiliser une file à priorité (min-heap) efficace
import heapq

# On définit des listes pour stocker la distance minimale (ou coût minimal) pour accéder à chaque station S et C
# Initialement, tous les coûts sont très élevés, "1<<30" est une constante très grande (équivalent à l'infini dans ce contexte)
MINCOST_CS = [1<<30] * (N+1)  # Pour chaque station S, contiendra le coût minimum pour y accéder
MINCOST_CC = [1<<30] * (M+1)  # Pour chaque station C, contiendra le coût minimum pour y accéder

# Le coût pour atteindre la station de départ (S) est 0, car on commence ici
MINCOST_CS[S] = 0

# On crée la file à priorité en insérant au départ la station S
# [0] + CS[S] : 0 est le coût initial, puis on ajoute la description de la station S de départ
Q = [[0] + CS[S]]  # Format : [coût, x, y, z, id, type]

# On prépare des listes pour marquer si une station de chaque type a déjà été "visitée"
# USES : stations S, USEC : stations C, USEU : stations U
USES = [0] * (X+1)  # Pour le type S (indices 1..X), 1 si déjà utilisé
USEC = [0] * (Y+1)  # Pour le type C (indices 1..Y)
USEU = [0] * (Z+1)  # Pour le type U (indices 1..Z)

# Boucle principale d'exploration (recherche de type Dijkstra sur un graphe implicite)
while Q:
    # On récupère le prochain élément de coût minimum dans la file à priorité
    cost, x, y, z, cs = heapq.heappop(Q)
    # cs est le marqueur de type : 0 pour S, 1 pour C

    if cs == 0:  # Si la station courante est de type S

        # On regarde si on a déjà utilisé cette station S de la dimension S (x)
        if USES[x] == 0:
            USES[x] = 1  # On la marque comme utilisée

            # Pour chaque station S partageant la même coordonnée x (dimension S)
            for to in CS_SLIST[x]:
                # Si le coût pour atteindre 'to' est amélioré, on met à jour et on insère dans la file
                if MINCOST_CS[to] > cost + 1:
                    MINCOST_CS[to] = cost + 1
                    # On empile la station S cible dans la file à priorité
                    heapq.heappush(Q, [cost + 1] + CS[to])

        # Même chose pour la coordonnée y (dimension C)
        if USEC[y] == 0:
            USEC[y] = 1  # On la marque comme utilisée

            # On explore les stations S partageant la même coordonnée y
            for to in CS_CLIST[y]:
                if MINCOST_CS[to] > cost + 1:
                    MINCOST_CS[to] = cost + 1
                    heapq.heappush(Q, [cost + 1] + CS[to])

            # On explore également les stations C partageant la même coordonnée y
            for to in CC_CLIST[y]:
                if MINCOST_CC[to] > cost + 1:
                    MINCOST_CC[to] = cost + 1
                    heapq.heappush(Q, [cost + 1] + CC[to])

    else:  # Si la station courante est de type C

        # On regarde si on a déjà utilisé cette station U de la dimension U (y)
        if USEU[y] == 0:
            USEU[y] = 1  # On la marque comme utilisée

            # Pour chaque station C partageant la même coordonnée y (dimension U)
            for to in CC_ULIST[y]:
                if MINCOST_CC[to] > cost + 1:
                    MINCOST_CC[to] = cost + 1
                    heapq.heappush(Q, [cost + 1] + CC[to])

        # Même chose pour la coordonnée x (dimension C)
        if USEC[x] == 0:
            USEC[x] = 1  # On la marque comme utilisée

            # On explore les stations S partageant la même coordonnée x (dimension C)
            for to in CS_CLIST[x]:
                if MINCOST_CS[to] > cost + 1:
                    MINCOST_CS[to] = cost + 1
                    heapq.heappush(Q, [cost + 1] + CS[to])

            # On explore également les stations C partageant la coordonnée x
            for to in CC_CLIST[x]:
                if MINCOST_CC[to] > cost + 1:
                    MINCOST_CC[to] = cost + 1
                    heapq.heappush(Q, [cost + 1] + CC[to])

# Lorsque la boucle est terminée, on doit afficher le coût minimal pour atteindre la station C d'indice T
# Si le coût est toujours "infini", cela veut dire qu'il n'existe pas de chemin et on affiche -1
if MINCOST_CC[T] == 1 << 30:
    print(-1)  # Pas de chemin possible
else:
    print(MINCOST_CC[T])  # On affiche le coût minimum pour atteindre T