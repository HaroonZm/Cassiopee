# Importation du module deque de la bibliothèque collections.
# deque (double-ended queue) permet d'utiliser une file à double entrée efficiente pour ajouter et retirer des éléments des deux côtés.
from collections import deque

# Initialisation d'une liste contenant les 4 directions adjacentes : 
# (-1, 0) vers la gauche, (0, -1) vers le haut, (1, 0) vers la droite, (0, 1) vers le bas.
# Cette liste sera utilisée pour parcourir les cases voisines d'une grille.
dd = [(-1, 0), (0, -1), (1, 0), (0, 1)]

# Boucle principale infinie permettant de traiter plusieurs cas jusqu'à la saisie d'une condition d'arrêt explicite.
while 1:
    # Lecture des dimensions largeur (w) et hauteur (h) de la grille depuis l'entrée standard.
    # map(int, ...) convertit les valeurs lues en entiers.
    w, h = map(int, raw_input().split())
    
    # Si les deux valeurs sont nulles, cela indique un cas d'arrêt, donc on quitte la boucle avec break.
    if w == h == 0:
        break

    # Lecture de la grille P ligne par ligne.
    # Chaque ligne de la grille est lue comme une chaîne de caractères (par raw_input()), transformée en liste de caractères.
    # Cela crée une grille bidimensionnelle P de h lignes, où chaque ligne a w colonnes.
    P = [list(raw_input()) for i in xrange(h)]
    
    # Création d'une grille L parallèle à P, de dimensions h (lignes) x w (colonnes).
    # Chaque case est initialisée à None. L servira à enregistrer les numéros de composantes connexes.
    L = [[None]*w for i in xrange(h)]

    # Initialisation d'un objet deque vide pour les parcours en largeur (BFS).
    deq = deque()
    
    # Initialisation d'un compteur de composantes connexes (cnt) à zéro.
    cnt = 0
    
    # Déclaration de différentes listes vides qui stockeront des informations sur chaque composante :
    # g : liste de ensembles représentant les connexions entre composantes
    # XL et XR : coordonnées extrêmes horizontales (min et max) par composante, pour les contacts au sol
    # M : somme pondérée des abscisses, utilisée pour des vérifications de stabilité
    # C : nombre total de points dans la composante (surface)
    g = []
    XL = []
    XR = []
    M = []
    C = []
    
    # Parcours de toute la grille pour identifier chaque composante connexe en profondeur.
    for i in xrange(h):  # Parcourt chaque ligne de la grille
        for j in xrange(w):  # Parcourt chaque colonne de la grille
            # Vérifie si la case actuelle contient un point ('.' signifie vide).
            # Si c'est vide, il n'y a rien à traiter pour la composante, on passe au suivant.
            if P[i][j] is '.':
                continue
            # Si la case n'a pas encore été marquée comme appartenant à une composante (donc None) :
            if L[i][j] is None:
                # p prend la valeur du caractère à cette position (identifie à quelle composante on va appartenir)
                p = P[i][j]
                # Ajoute la position courante (colonne j, ligne i) à la file/deque pour débuter un BFS
                deq.append((j, i))
                # Marque dans L cette position comme appartenant à la composante numéro cnt.
                L[i][j] = cnt
                # Cas particulier : si la case est sur la dernière ligne ou satisfait une condition de contact avec le sol
                # xl et xr reçoivent la valeur j (indiquent les bornes horizontales initiales de contact sol pour cette composante)
                if i == h-1 or p != P[i+1][j] != '.':
                    xl = xr = j
                else:
                    # Dans le cas contraire, on initialise xl au maximum (w) et xr au minimum (-1), valeurs extrêmes.
                    xl = w
                    xr = -1
                # s stocke la première valeur de la somme pondérée des abscisses, initialisée à 2+j.
                s = 2 + j
                # BFS à partir de la case courante, pour explorer toute la composante connexe
                while deq:
                    # Retire la case la plus ancienne ajoutée à la file pour exploration (file FIFO)
                    x, y = deq.popleft()
                    # Parcours les 4 directions pour explorer les voisins immédiats de la case actuelle
                    for dx, dy in dd:
                        nx = x + dx  # Calcul de la nouvelle colonne (abscisse)
                        ny = y + dy  # Calcul de la nouvelle ligne (ordonnée)
                        # Vérifie si les coordonnées du voisin sont dans la grille 
                        # et que la valeur est égale à p (même composante) 
                        # et que la case n'a pas déjà été marquée (pas encore visitée)
                        if 0 <= nx < w and 0 <= ny < h and p == P[ny][nx] and L[ny][nx] is None:
                            # Ajoute le voisin à la file d'exploration
                            deq.append((nx, ny))
                            # Marque le voisin comme appartenant à la composante actuelle
                            L[ny][nx] = cnt
                            # Ajoute la colonne du voisin à la somme pondérée des abscisses
                            s += nx
                            # Si la case voisine est sur la ligne la plus basse OU en contact avec une autre composante/séparation (différent p && pas '.')
                            if ny == h-1 or p != P[ny+1][nx] != '.':
                                # On met à jour xl et xr avec la nouvelle position horizontale
                                xl = min(xl, nx)
                                xr = max(xr, nx)
                # Après avoir visité toute la composante connexe :
                cnt += 1  # Incrémente le nombre de composantes déjà trouvées
                g.append(set())  # Ajoute un ensemble vide pour enregistrer les connexions de cette composante
                M.append(s)      # Enregistre la somme pondérée des abscisses pour la composante
                C.append(4)      # Ajoute un nombre de points initial de 4 (à affiner selon la logique, peut être modifié par la suite)
                XL.append(xl)    # Enregistre la borne gauche horizontale de contact sol
                XR.append(xr+1)  # Enregistre la borne droite, +1 pour rendre l'intervalle demi-ouvert
            # Si la case actuelle n'est PAS sur la première ligne (i != 0) :
            if i:
                # Si la composante de la case actuelle est différente de celle du dessus,
                # et que celle du dessus existe (différent de None),
                # et que la composante du dessus n'est pas déjà enregistrée comme voisine de la composante actuelle
                if L[i][j] != L[i-1][j] != None and L[i-1][j] not in g[L[i][j]]:
                    # Ajoute la composante du dessus dans l'ensemble des connexions de la composante courante.
                    g[L[i][j]].add(L[i-1][j])
                    # Additionne la somme pondérée des abscisses et le nombre de points de la composante du dessus
                    M[L[i][j]] += M[L[i-1][j]]
                    C[L[i][j]] += C[L[i-1][j]]

    # Vérification de la stabilité de chaque composante, une par une
    for i in xrange(cnt):
        # Teste la condition de stabilité : si la somme pondérée des abscisses multipliée par le nombre de points est bien comprise 
        # entre l'extrémité gauche multipliée par le nombre de points et l'extrémité droite multipliée par le nombre de points
        if not XL[i] * C[i] < M[i] < XR[i] * C[i]:
            # Si la condition n'est pas satisfaite, on affiche "UNSTABLE" et on interrompt la vérification
            print "UNSTABLE"
            break
    else:
        # La clause else du for : si aucune composante n'a violé la condition de stabilité, alors la structure est "STABLE"
        print "STABLE"