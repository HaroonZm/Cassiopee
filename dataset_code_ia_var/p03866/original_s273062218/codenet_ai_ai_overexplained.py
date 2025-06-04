#from collections import deque,defaultdict

# Définition d'une fonction lambda pour afficher sans saut de ligne
printn = lambda x: print(x, end='')

# Définition d'une fonction lambda pour lire un entier depuis l'entrée standard
inn = lambda : int(input())

# Définition d'une fonction lambda pour lire une liste d'entiers séparés par des espaces
inl = lambda: list(map(int, input().split()))

# Définition d'une fonction lambda pour lire plusieurs entiers séparés par des espaces (forme générateur)
inm = lambda: map(int, input().split())

# Définition d'une fonction lambda pour lire une chaîne, suppression des espaces à gauche et à droite
ins = lambda : input().strip()

# Variable booléenne servant à activer/désactiver le mode debug (débogage)
DBG = True # Mettre False pour désactiver les impressions de débogage

# Variable représentant un très grand nombre, utilisée ici comme 'infini'
BIG = 10**18

# Variable constante pour moduler les calculs, souvent utilisée dans les contextes de programmation compétitive
R = 10**9 + 7

# Autre valeur possible pour R (décommenter pour changer la valeur)
#R = 998244353

# Définition d'une fonction pour afficher lors du débogage si DBG est True
def ddprint(x):
    if DBG:
        print(x)

# Import de fonctions mathématiques : sqrt pour racine carrée, heappush/heappop pour la file de priorité
from math import sqrt
from heapq import heappush, heappop

# Fonction qui calcule la distance euclidienne entre 2 points (x1, y1) et (x2, y2)
def pdist(x1, y1, x2, y2):
    # La distance euclidienne se calcule comme la racine carrée de la somme des carrés des différences de coordonnées
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Lecture des coordonnées du point de départ (xs, ys) et d'arrivée (xt, yt)
xs, ys, xt, yt = inm()

# Lecture du nombre de cercles présents
n = inn()

# Initialisation d'une liste qui contiendra les informations sur les cercles (x, y, r)
cir = []
for i in range(n):
    x, y, r = inm()  # Lecture des coordonnées et du rayon de chaque cercle
    cir.append((x, y, r))  # Ajout des informations du cercle dans la liste

# Création d'une matrice distante (tableau 2D) pour assurer les distances entre chacun des n cercles + départ + arrivée
# Il y a n+2 "sommets" : les n cercles, le point de départ (index n), et le point d'arrivée (index n+1)
dst = [[0] * (n + 2) for i in range(n + 2)]  # Initialisation d'une matrice remplie de 0

# Calcul de la distance directe entre le départ et l'arrivée et l'assigner dans la matrice de distance
# dst[n][n+1] : départ -> arrivée ; dst[n+1][n] : arrivée -> départ (symétrique)
dst[n][n+1] = dst[n+1][n] = pdist(xs, ys, xt, yt)

# Remplissage de la matrice de distances avec les distances nécessaires
# On traite les liens entre le départ/l'arrivée et chaque cercle, puis entre chaque paire de cercles
for i in range(n):
    x, y, r = cir[i]  # Récupération des coordonnées et rayon du cercle i
    # Distance du départ (n) au cercle i, moins son rayon (sauf si négatif: on prend 0)
    dst[n][i] = dst[i][n] = max(0.0, pdist(xs, ys, x, y) - r)
    # Distance de l'arrivée (n+1) au cercle i, moins son rayon
    dst[n+1][i] = dst[i][n+1] = max(0.0, pdist(xt, yt, x, y) - r)
    # Pour chaque paire de cercles distincts (i,j), calculer la distance entre leurs bords (en enlevant les 2 rayons)
    for j in range(i + 1, n):  # On évite les doublons en parcourant uniquement (i+1,n)
        xx, yy, rr = cir[j]  # Coordonnées et rayon du cercle j
        # Calculer la distance euclidienne centre à centre, puis on enlève les rayons des deux cercles pour avoir bord à bord
        # On met 0 si les cercles se touchent ou se chevauchent
        dst[j][i] = dst[i][j] = max(0.0, pdist(xx, yy, x, y) - rr - r)

# (Option de debug) Afficher la matrice de distances si jamais on veut vérifier sa correction
if False and DBG:
    for i in range(n + 2):
        ddprint(dst[i])

# Initialisation d'une liste de coûts pour garder trace du coût minimal pour chaque sommet
# Ici, on initialise tous les sommets à une valeur "infinie" (BIG), il y a (n+2) sommets
cost = [float(BIG)] * (n + 2)

# Initialisation d'une file de priorité avec (0.0, n) : coût 0.0 au sommet "départ" (index n)
q = [(0.0, n)]

# Algorithme de Dijkstra classique pour trouver le plus court chemin depuis le départ
while len(q) > 0:  # Tant qu'il y a des sommets à traiter dans la file
    d, p = heappop(q)  # Récupérer le sommet avec la plus faible distance courante (distance d, sommet p)
    # ddprint(f"{d=} {p=}")  # Affichage de debug optionnel
    if cost[p] <= d:  # Si le coût du sommet p n'est pas meilleur que le coût trouvé, on saute
        continue
    cost[p] = d  # Sinon, on met à jour ce coût minimal trouvé pour p
    # On parcourt tous les voisins possibles (tous les sommets) pour mettre à jour les coûts
    for v in range(n + 2):
        # Calculer la nouvelle distance potentielle en passant par p pour atteindre v
        newdist = d + dst[p][v]
        # Si v n'est pas p et que cette distance est meilleure (plus petite), on met à jour
        if v != p and newdist < cost[v]:
            heappush(q, (newdist, v))  # On ajoute ce sommet v dans la file de priorité à traiter

# Affichage du coût minimal pour atteindre le sommet "arrivée" (index n+1)
print(cost[n+1])