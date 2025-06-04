# AOJ 1050 The Last Dungeon
# Python3 2018.7.7 bal4u
# Version avec des commentaires extrêmement détaillés

import math        # Importation du module math pour les fonctions mathématiques telles que sqrt et hypot
import heapq       # Importation du module heapq pour l'utilisation de la file de priorité (priority queue)

EPS = 1e-8         # Constante utilisée pour comparer des nombres flottants, permet de gérer les imprécisions
pp0 = [0j, 4+0j, 4+4j, 4j] # Définition de la forme d'un carré avec les coins sous forme de nombres complexes

def EQ(a, b):
    """
    Fonction pour vérifier si deux valeurs flottantes sont 'également proches', 
    c'est-à-dire que leur différence est inférieure à EPS (tolérance).
    Cela prend en compte les erreurs d'arrondi en virgule flottante.
    """
    return abs(a - b) < EPS

def PPeQ(a, b):
    """
    Fonction pour vérifier si deux points complexes (donc dans le plan complexe) sont égaux
    en utilisant la fonction EQ pour comparer séparément leur partie réelle et imaginaire.
    """
    return EQ(a.real, b.real) and EQ(a.imag, b.imag)

def dcmp(x):
    """
    Fonction pour comparer le signe d'un nombre, retourne :
    - 0 si x est considéré comme nul (comparé à 0 en complex avec PPeQ)
    - -1 si x est négatif ou nul
    - 1 si x est strictement positif
    """
    if PPeQ(x, 0): # Si x est (presque) zéro
        return 0
    return -1 if x <= 0 else 1 # Condition ternaire pour déterminer le signe de x

def cross(a, b):
    """
    Calcul du produit vectoriel 2D de deux vecteurs représentés comme complexes.
    Le produit vectoriel mesure l'aire du parallélogramme formé par (0,a) et (0,b).
    La formule est det([[a.real, a.imag], [b.real, b.imag]]) = a.real*b.imag - a.imag*b.real
    """
    return a.real * b.imag - a.imag * b.real

def vabs(a):
    """
    Fonction pour calculer la norme (longueur) d'un vecteur complexe a.
    Utilise math.hypot pour plus de précision numérique que sqrt(re*re + im*im).
    """
    return math.hypot(a.real, a.imag)

def crossPointS2P(seg, bs, be):
    """
    Calcul du point d'intersection entre un segment (seg) et une droite passant par bs et be.
    Utilise le produit vectoriel pour déterminer les coefficients d'interpolation.
    Retourne le point complexe d'intersection.
    """
    a1 = cross(be - bs, seg[0] - bs) # Produit vectoriel pour le premier point du segment
    a2 = cross(be - bs, seg[1] - bs) # Produit vectoriel pour le deuxième point du segment
    # Calcul de l'interpolé linéaire pour trouver l'intersection sur la droite
    return complex(
        (seg[0].real * a2 - seg[1].real * a1) / (a2 - a1),
        (seg[0].imag * a2 - seg[1].imag * a1) / (a2 - a1)
    )

def bisector(a, b):
    """
    Calcule la médiatrice (droite perpendiculaire passant par le milieu) entre deux points complexes a, b.
    Si les y sont égaux, la médiatrice sera verticale.
    Renvoie deux points qui définissent une droite dans le plan.
    Pour générer 'loin' dans l'un ou l'autre sens, on multiplie par 100.
    """
    ax, ay = (a.real + b.real)/2, (a.imag + b.imag)/2 # Calcul du milieu
    if EQ(a.imag, b.imag): # Si les ordonnées sont égales, médiatrice verticale
        return [
            complex(ax, ay),
            complex(ax, ay + (b.real - a.real) * 100) # Second point "loin" sur la médiatrice
        ]
    # Sinon, utiliser une grande différence horizontale comme direction
    t = ax - (b.imag - a.imag) * 100
    # Calcul du second point "loin" sur la médiatrice
    return [
        complex(ax, ay),
        complex(
            t,
            (ax - t) * (b.real - a.real) / (b.imag - a.imag) + ay
        )
    ]

def convex_cut(seg, p):
    """
    Coupe un polygone convexe par une droite (définie par seg) et garde uniquement les points à gauche de la droite.
    'p' est une liste de points complexes décrivant le polygone (en sens positif).
    On utilise le produit vectoriel pour déterminer de quel côté chaque point du polygone se situe.
    On ajoute aussi les points d'intersection aux nouveaux sommets si le segment coupe une arête.
    """
    ans = []                # Liste des nouveaux sommets du polygone 'coupé'
    n = len(p)              # Nombre de sommets du polygone
    for i in range(n):
        d1 = dcmp(cross(seg[1] - seg[0], p[i] - seg[0])) # Signe pour p[i]
        # Déterminer le prochain sommet, en faisant le tour (p[0] après p[n-1])
        t = p[0] if i+1 == n else p[i+1]
        d2 = dcmp(cross(seg[1] - seg[0], t - seg[0]))    # Signe pour le prochain sommet
        if d1 >= 0:
            ans.append(p[i])          # Garder le sommet courant s'il est à gauche (ou dessus) de la droite
        if d1 * d2 < 0:               # Si les sommets sont de part et d'autre de la droite
            ans.append(crossPointS2P(seg, p[i], t)) # Ajouter le point d'intersection
    return ans                        # Retourner la nouvelle liste de sommets du polygone

def pushBack(a, b):
    """
    Ajoute l'arête (lien) b à la liste des voisins de a si ce n'est pas déjà fait, 
    sauf dans des cas particuliers (bords supérieur et inférieur du carré 'salle').
    Cela sert à construire un graphe non orienté entre les salles.
    """
    if EQ(tbl[a].imag, 0) and EQ(tbl[b].imag, 0):
        return                       # On ne relie pas two sommets sur le bord inférieur
    if EQ(tbl[a].imag, 4) and EQ(tbl[b].imag, 4):
        return                       # Ni deux sommets sur le bord supérieur
    if b in to[a]:
        return                       # On évite les doublons
    to[a].append(b)                  # Enfin, ajouter b comme voisin de a

def dijkstra(V, to, tbl):
    """
    Algorithme de Dijkstra classique pour le plus court chemin. 
    V : nombre de sommets
    to : liste d'adjacence (voisins)
    tbl : table des coordonnées des sommets (complexes)
    La distance est le coût en 'longueur' entre les centres des salles adjacentes.
    On cherche le chemin du côté gauche (real==0) au côté droit (real==4).
    """
    visited = [0] * V                # Liste pour suivre les sommets déjà visités
    Q = []                           # Priority queue pour Dijkstra (tas binaire)
    # Initialisation : mettre dans la file tous les sommets sur le bord gauche (real == 0)
    for i in range(V):
        if EQ(tbl[i].real, 0):
            heapq.heappush(Q, (0, i, 0))  # (distance = 0, sommet i, coordonnée réelle)
            visited[i] = 1
    while Q:
        t, s, x = heapq.heappop(Q)       # Extraire le sommet de distance minimale
        if EQ(x, 4):                     # Si on arrive à droite du carré (real == 4)
            return t                     # Retourner la distance cumulée
        for e in to[s]:                  # Parcourir les voisins
            if visited[e]:               # Déjà visité, on saute
                continue
            visited[e] = 1               # On marque comme visité
            heapq.heappush(Q, (t + vabs(tbl[s] - tbl[e]), e, tbl[e].real))
            # On ajoute dans la file la distance augmentée et la coordonnée du nouvel état
    return -1                            # Si on n'a jamais atteint real==4, impossible

# ---- Programme principal (entrée/sortie et gestion du cas) ---- #

while True:
    n = int(input())                     # Lire le nombre de points (monstres)
    if n == 0:                           # Condition d'arrêt du programme
        break
    p = []                               # Liste des positions des monstres (points complexes)
    for i in range(n):
        x, y = map(float, input().split()) # Lecture des coordonnées x, y
        p.append(complex(x, y))            # Ajouter comme nombre complexe
    if n == 1:
        print("impossible")              # Un seul monstre = impossible selon l'énigme
        continue
    tbl = []                             # Liste des sommets du graphe (coordonnées complexes)
    sz = 0                               # Compteur de sommets
    to = [[] for _ in range(50)]         # Liste des voisins (pour chaque sommet), dimension arbitraire (assez grande)
    for i in range(n):                   # Pour chaque monstre/point
        po = pp0[0:]                     # On part du carré de base (copy shallow de la liste)
        for j in range(n):               # Pour chaque autre monstre
            if j == i:                   # Sauf lui-même
                continue
            seg = bisector(p[i], p[j])   # Calcule la médiatrice pour séparer la zone d'influence du monstre
            po = convex_cut(seg, po)     # Coupe la salle initiale pour réduire sa zone
        w = len(po)                      # Nombre de sommets de la salle de Voronoi
        if w <= 1:                       # Si la salle est dégénérée, on ne crée rien
            continue
        if w == 2:
            # Cas où la salle est réduite à un segment (deux points)
            a, sz = sz, sz + 1
            tbl.append(po[0])            # Ajouter le premier point
            b, sz = sz, sz + 1
            tbl.append(po[1])            # Ajouter le second point
            pushBack(a, b)               # Ajouter le lien bidirectionnel (c'est un segment)
            pushBack(b, a)
        else:
            # Cas général : salle à 3 points ou plus (polygone)
            j = sz                       # Mémoriser le premier index du bloc de sommets
            sz += w                      # Réserver w indices pour les nouveaux sommets
            tbl.extend(po)               # Ajouter tous les sommets du polygone à la liste globale
            a, c = w - 1, 1              # a : sommet précédent, c : sommet suivant
            for b in range(w):           # Pour chaque sommet du polygone
                pushBack(j + b, j + a)   # Créer un arc vers le sommet précédent
                pushBack(j + b, j + c)   # Créer un arc vers le sommet suivant
                a, c = a + 1, c + 1
                if a == w:               # On tourne autour du polygone (cycle)
                    a = 0
                if c == w:
                    c = 0
    # Ajouter des arêtes entre points de coordonnées égales (pour fusionner des coins superposés)
    for i in range(sz):
        for j in range(i + 1, sz):
            if PPeQ(tbl[i], tbl[j]):     # Si les sommets (coords) sont égaux
                pushBack(i, j)
                pushBack(j, i)
    ans = dijkstra(sz, to, tbl)          # Chercher la plus courte chaîne de salles
    print("impossible" if ans < 0 else ans) # Afficher la réponse, en format demandé