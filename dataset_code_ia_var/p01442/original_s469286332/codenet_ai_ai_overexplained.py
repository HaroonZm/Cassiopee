from heapq import heappush, heappop  # Importation des fonctions pour gérer une file de priorité (tas binaire)
import sys  # Importation du module système pour lire et écrire depuis/vers la console
readline = sys.stdin.readline  # Création d'une variable de raccourci vers la fonction pour lire une ligne de l'entrée standard
write = sys.stdout.write  # Création d'une variable de raccourci vers la fonction pour écrire sur la sortie standard

# Définition d'une liste de tuples qui représentent les déplacements possibles :
# (-1,0): Déplacement vers le haut, (0,-1): gauche, (1,0): bas, (0,1): droite
dd = ((-1, 0), (0, -1), (1, 0), (0, 1))

def solve():
    # Lecture et transformation en entiers du nombre de lignes H, de colonnes W, et de la longueur N de la chaîne S
    H, W, N = map(int, readline().split())
    # Si la hauteur est nulle, cela indique la fin des données et la fonction retourne False pour arrêter le programme principal
    if H == 0:
        return False
    # Lecture de la chaîne de commandes de déplacement (gauche/droite)
    S = readline().strip()
    # Création d'une matrice H x W initialisée à 0, qui représentera la grille : 0 = vide, 1 = mur
    C = [[0]*W for i in range(H)]
    # Initialisation des coordonnées de départ (sx, sy) et d'arrivée (gx, gy)
    sx = sy = gx = gy = 0
    for i in range(H):  # Parcours de chaque ligne de la grille
        s = readline().strip()  # Lecture de la ligne courante
        for j, c in enumerate(s):  # Parcours de chaque caractère avec son indice
            if c in '#.':  # Si le caractère est un mur ou un espace libre
                # Conversion du caractère en booléen : c == '#' sera True (mur), sinon False (case libre)
                C[i][j] = (c == '#')
            elif c == 'S':  # Si la case est la position de départ
                sx = j  # Stockage de la position en x (colonne)
                sy = i  # Stockage de la position en y (ligne)
            else:  # Ici la case est censée être la position d'arrivée (tout caractère autre que '#', '.', 'S')
                gx = j  # Stockage de la position d'arrivée en x
                gy = i  # Stockage de la position d'arrivée en y
    # Création d'une liste S0 de taille N+1 initialisée à 1.
    # S0[k] contiendra la direction du joueur après k commandes ('L' ou 'R')
    # La direction suit l'ordre : 0=haut, 1=gauche, 2=bas, 3=droite (voir 'dd'), on commence en direction 1.
    S0 = [1]*(N+1)
    cur = 1  # cur est la direction courante, initialisée à 1 (gauche)
    for i in range(N):  # Simulation des mouvements à partir de la chaîne S
        if S[i] == 'L':  # Tournant à gauche
            cur = (cur - 1) % 4  # On enlève 1 à la direction, modulo 4 pour rester entre 0 et 3
        else:  # Sinon, donc 'R' (droite), on ajoute 1
            cur = (cur + 1) % 4
        S0[i+1] = cur  # Enregistrez la direction courante après le mouvement i+1
    # On prépare un tableau d contenant pour chaque direction le prochain changement de direction à venir (indice dans S)
    d = [N+1]*4  # Initialisation par défaut (N+1 : dépasse le dernier indice de S)
    D = [None]*(N+1)  # D[i] contiendra une copie de d à l'étape i
    # On parcourt S à l'envers afin de déterminer pour chaque position dans S et pour chaque direction,
    # à quel index on subit un prochain changement de cette direction
    for i in range(N, -1, -1):  # De N à 0 inclus (ordre décroissant)
        d[S0[i]] = i  # Le prochain changement pour la direction S0[i] se passe à l'étape i
        D[i] = d[:]  # On stocke une copie de d (pour éviter les effets de bords)
    # T est la grille des coûts : T[y][x] contient pour chaque case le plus petit coût connu pour y arriver
    # (ici, le coup correspond à l'indice dans S où l'on arrive dans la case)
    T = [[N+1]*W for i in range(H)]  # Initialisation à N+1 (impossible, car indices de S vont jusqu'à N)
    T[sy][sx] = 0  # Le coût pour atteindre la case de départ est 0 (départ sans mouvement)
    que = [(0, sx, sy)]  # Initialisation d'une file de priorité (tas) avec un seul élément : (coût, x, y)
    # On implémente ici une variante de Dijkstra pour trouver le plus court chemin selon la dynamique imposée par S
    while que:
        # heappop retire et retourne le plus petit élément du heap (ici, le plus petit coût de parcours)
        cost, x, y = heappop(que)
        if T[y][x] < cost:  # Si on a déjà trouvé un meilleur coût pour atteindre cette case, on l'ignore
            continue
        d = D[cost]  # On récupère l'information sur le prochain changement de direction pour ce coût
        for k in range(4):  # Parcourt toutes les directions possibles
            dx, dy = dd[k]  # Récupération du déplacement en x et y pour la direction k
            n_cost = d[k]  # Calcul du nouvel indice de commande où l'on aura cette direction
            nx = x + dx  # Calcul de la nouvelle position x, après déplacement
            ny = y + dy  # Calcul de la nouvelle position y, après déplacement
            # On vérifie que la nouvelle position est dans la grille ET que ce n'est pas un mur
            if not 0 <= nx < W or not 0 <= ny < H or C[ny][nx]:
                continue  # Si hors grille ou sur un mur, on ne fait rien
            if n_cost < T[ny][nx]:  # Si l'on trouve un coût plus petit pour atteindre (nx, ny)
                T[ny][nx] = n_cost  # On met à jour le coût minimal pour cette case
                heappush(que, (n_cost, nx, ny))  # On insère la nouvelle option dans la file de priorité
    # Après avoir exploré tout le tas, on vérifie si la case (gx, gy) est atteignable à un coût <= N (enchainement des commandes)
    # Si oui, on imprime "Yes", sinon "No"
    print("Yes" if T[gy][gx] < N+1 else "No")
    return True  # On retourne True pour continuer la boucle principale

# Boucle principale pour traiter plusieurs cas jusqu'à rencontrer une hauteur nulle (H==0)
while solve():
    ...  # L'opérateur "..." (ellipsis) n'a pas d'effet ici, il sert de passe-partout (no-op)