from heapq import heappop as pop  # Importe la fonction heappop du module heapq et la renomme en pop pour faciliter son utilisation
from heapq import heappush as push  # Importe la fonction heappush du module heapq et la renomme en push

INF = 10 ** 18  # Définit une constante représentant une "infinie" distance (un très grand nombre)

class edge:
    # Classe représentant une arête (edge) dans un graphe, c'est-à-dire une connexion entre deux sommets (noeuds)
    def __init__(self, to, cost):
        # Le constructeur prend deux paramètres :
        #   to : le sommet (noeud) de destination de l'arête
        #   cost : le coût (longueur, poids) de l'arête
        self.to = to    # Stocke l'identifiant du sommet de destination de l'arête
        self.cost = cost  # Stocke le coût, le poids ou la longueur de l'arête

# Lecture du nombre de sommets (N), du nombre d'arêtes (M) et du nombre de sommets de départ (K) à partir de l'entrée standard
N, M, K = map(int, input().split())

# Initialise le graphe sous forme de liste d'adjacence :
# G est une liste où chaque élément est une liste des arêtes sortantes à partir du sommet i
G = [[] for i in range(N)]
# Par exemple, G[2] contiendra toutes les arêtes partant du sommet 2.

# Initialise la liste des plus courtes distances trouvées depuis les nœuds de départ :
# d[i] contiendra la distance la plus courte trouvée entre le ou les sommets de départ et le sommet i
d = [INF for i in range(N)]  # Initialise toutes les distances à l'infini, car elles sont inconnues au départ

def dijkstra(lst):
    # Fonction qui implémente l'algorithme de Dijkstra pour trouver les plus courts chemins depuis un ou plusieurs sommets de départ
    # lst : liste contenant les indices des sommets de départ
    
    que = []  # Initialise la file de priorité (implémentée comme un tas binaire min-heap)

    # Met à jour la distance de chaque sommet de départ (leur distance à eux-mêmes est zéro)
    for s in lst:
        d[s] = 0  # La distance du sommet de départ s à lui-même est 0
        push(que, (0, s))  # Ajoute ce sommet à la file de priorité avec la distance 0

    # Boucle principale de Dijkstra : on traite les sommets par ordre croissant de leur distance depuis la source
    while len(que):  # Continue tant qu'il y a des sommets à traiter dans la file
        p = pop(que)  # Retire et récupère le sommet ayant la plus petite distance connue (priorité minimale)
        v = p[1]      # Récupère l'identifiant du sommet à traiter
        # Si la distance connue est déjà meilleure que celle dans la file, on saute la suite
        if d[v] < p[0]:
            continue
        # Pour chaque arête sortant du sommet v
        for i in range(len(G[v])):
            e = G[v][i]  # Récupère la i-ème arête sortante depuis v
            # Si la distance pour atteindre le sommet e.to via v est plus courte que celle qu'on connaît actuellement,
            # alors on met à jour cette distance
            if d[e.to] > d[v] + e.cost:
                d[e.to] = d[v] + e.cost  # Mets à jour la plus courte distance trouvée pour atteindre e.to
                push(que, (d[e.to], e.to))  # Ajoute e.to à la file de priorité avec sa nouvelle distance

# Lecture des arêtes du graphe
for i in range(M):
    s, t, c = map(int, input().split())  # s et t : extrémités de l'arête, c : coût
    s -= 1  # On convertit s en indice commençant à 0 (python utilise les indices à partir de 0)
    t -= 1  # Idem pour t
    # Ajoute l'arête s->t de coût c et l'arête t->s de coût c (graphe non orienté)
    G[s].append(edge(t, c))
    G[t].append(edge(s, c))

# Lecture des K sommets de départ (positions initiales), les indices sont décalés pour correspondre au 0-based indexing
lst = [int(input()) - 1 for i in range(K)]

# Exécution de Dijkstra pour tous les sommets de départ à la fois
dijkstra(lst)

# Initialisation d'une liste pour stocker des valeurs de réponses
anss = []
append = anss.append  # On garde un raccourci vers la méthode append pour une utilisation plus rapide dans la boucle

# Le but de la boucle suivante est de calculer pour chaque arête, une certaine valeur basée sur les distances de part et d'autre de l'arête
for i in range(N):  # Pour chaque sommet
    for e in G[i]:  # Pour chaque arête partant de ce sommet
        # Calcule la somme d[i] + d[e.to] + e.cost : somme des plus courts chemins jusqu'à chaque extrémité de l'arête, plus le coût de traversée de l'arête
        x = d[i] + d[e.to] + e.cost
        # Si cette somme x est impaire, alors (x // 2) arrondirait vers le bas, donc on rajoute 1 pour arrondir vers le haut
        if x % 2:
            append(x // 2 + 1)
        else:
            append(x // 2)  # Sinon, on prend la moitié exacte

# Affiche la plus grande valeur calculée parmi toutes celles insérées dans anss
print(max(anss))