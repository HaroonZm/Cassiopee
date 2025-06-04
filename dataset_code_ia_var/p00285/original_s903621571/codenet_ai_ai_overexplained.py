from heapq import heappush, heappop  # Importation des fonctions pour gérer une file de priorité (min-heap)

class MinCostFlow:
    INF = 10**18  # Définition d'une constante représentant une grande valeur utilisée comme "infini"

    def __init__(self, N):
        # Constructeur de la classe.
        # N : nombre de sommets dans le graphe.
        self.N = N  # Stocke le nombre de sommets
        # Initialise une liste d'adjacence vide : chaque sommet a sa propre liste d'arêtes sortantes.
        self.G = [[] for i in range(N)]

    def add_edge(self, fr, to, cap, cost):
        # Ajoute une arête dirigée du sommet 'fr' vers le sommet 'to'
        # fr : sommet de départ
        # to : sommet d'arrivée
        # cap : capacité maximale de l'arête
        # cost : coût unitaire pour transférer un flux sur cette arête

        G = self.G  # Raccourci pour la liste d'adjacence

        # Ajoute l'arête principale : 'fr' -> 'to' avec la capacité et le coût donnés.
        # Utilisation d'une liste pour stocker [destination, capacité, coût, index_arrete_inverse]
        # index_arrete_inverse : index de l'arête inverse dans G[to]
        G[fr].append([to, cap, cost, len(G[to])])

        # Ajoute aussi l'arête résiduelle inverse : 'to' -> 'fr' avec capacité 0 et coût opposé.
        # Le but est de faciliter le rétablissement du flux lors de l'algorithme.
        # len(G[fr])-1 pointe vers l'arête principale depuis la destination inverse.
        G[to].append([fr, 0, -cost, len(G[fr])-1])

    def flow(self, s, t, f):
        # Calcule le flux de coût minimum du sommet s vers t en envoyant f unités de flux.
        # s : source
        # t : puits
        # f : flux total à envoyer
        N = self.N  # Nombre de sommets
        G = self.G  # Liste d'adjacence
        INF = MinCostFlow.INF  # Constante infini localement

        res = 0  # Stocke le coût total du flux envoyé

        # Potentiels pour le recalcul des coûts réduits (pour optimiser Dijkstra)
        H = [0]*N  # Initialisé à 0 pour tous les sommets
        
        # Tableaux pour reconstituer le chemin optimal trouvé lors de chaque itération.
        prv_v = [0]*N  # prv_v[v]: sommet parent de v dans le chemin
        prv_e = [0]*N  # prv_e[v]: index de l'arête utilisée pour atteindre v depuis prv_v[v]

        # Boucle principale : tant qu'il reste du flux à envoyer
        while f:
            # Tableau des distances (coûts minimaux) à chaque sommet à partir de la source
            dist = [INF]*N  # Initialise toutes les distances à INF
            dist[s] = 0  # La distance à la source s vaut 0

            # File de priorité pour Dijkstra : stocke les couples (coût_actuel, sommet)
            que = [(0, s)]

            # Dijkstra pour trouver le chemin de coût minimum de flux résiduel disponible
            while que:
                c, v = heappop(que)  # Prend le sommet avec le coût le plus faible
                if dist[v] < c:  # Si on a déjà trouvé mieux pour ce sommet, on saute
                    continue
                # Parcourt toutes les arêtes sortantes du sommet v
                for i, (w, cap, cost, _) in enumerate(G[v]):
                    # Si la capacité résiduelle sur cette arête est nulle, on ne peut pas pousser de flux
                    # On vérifie aussi si passer par cette arête donnerait une meilleure distance via la réduction de potentiel
                    if cap > 0 and dist[w] > dist[v] + cost + H[v] - H[w]:
                        # Met à jour la distance/candidature pour w
                        dist[w] = r = dist[v] + cost + H[v] - H[w]
                        prv_v[w] = v  # Retient le parent de w = v
                        prv_e[w] = i  # Retient l'index de l'arête utilisée pour rejoindre w depuis v
                        # Ajoute ce sommet à la file de priorité pour un traitement ultérieur
                        heappush(que, (r, w))

            if dist[t] == INF:
                # Si la distance au puits reste infini, aucun chemin n'est disponible : retour -1 (échec)
                return -1

            # Met à jour les potentiels pour préparer l'itération suivante.
            for i in range(N):
                H[i] += dist[i]

            # On va maintenant pousser le flux maximal autorisé le long du chemin optimal trouvé
            d = f  # Aucune idée, on essaiera au plus le flux restant à envoyer
            v = t  # Commence à remonter le chemin du puits à la source
            while v != s:
                # Trouve la capacité résiduelle minimale rencontrée le long du chemin (le goulot d'étranglement)
                d = min(d, G[prv_v[v]][prv_e[v]][1])  # Capacité de l'arête utilisée
                v = prv_v[v]  # Remonte au sommet parent

            f -= d  # On a transféré d unités de flux, donc le flux à envoyer est réduit d'autant
            res += d * H[t]  # On paie le coût associé à ce flux vers le puits
            v = t  # Va de nouveau du puits à la source pour modifier le graphe résiduel
            while v != s:
                # Récupère l'arête utilisée pour venir en v depuis prv_v[v]
                e = G[prv_v[v]][prv_e[v]]
                e[1] -= d  # Réduit la capacité résiduelle sur cette arête (on a utilisé ce flux)
                # Met à jour l'arête inverse pour permettre le retour du flux (augmentation possible)
                G[v][e[3]][1] += d
                v = prv_v[v]  # Reprend le sommet précédent

        return res  # Retourne le coût total du flux envoyé

# Boucle pour gérer plusieurs cas jusqu'à la fin des entrées
while 1:
    # Lit deux entiers depuis l'entrée standard : M et W
    M, W = map(int, input().split())
    if M == W == 0:
        # Condition d'arrêt : si M et W sont tous les deux 0, on quitte la boucle
        break
    # Lit M entiers (valeurs du tableau A) - les * servent à unpacker l'itérable en une liste
    *A, = map(int, input().split())
    # Lit W entiers (valeurs du tableau B)
    *B, = map(int, input().split())

    # Création d'un graphe avec M+W+2 sommets :
    # Sommets 0 : super-source
    # Sommets 1..M : les éléments de A (comme "workers" ou "hommes")
    # Sommets M+1...M+W : les éléments de B (comme "jobs" ou "femmes")
    # Sommet M+W+1 : super-puits
    mcf = MinCostFlow(M+W+2)

    # Ajoute des arêtes de la super-source à chaque sommet A[i] (les "hommes")
    for i in range(M):
        # La capacité est 1 car chaque "homme" est associé à au plus une "femme" (ou travail, etc.)
        # Le coût est 0 car ce n'est pas un vrai mouvement dans le modèle
        mcf.add_edge(0, i+1, 1, 0)

    # Pour chaque homme (A[i]) et chaque femme (B[j]), ajoute une arête représentant le matching possible
    for i in range(M):
        for j in range(W):
            d = abs(A[i] - B[j])  # Calcule la distance absolue entre A[i] et B[j]
            # Le coût est négatif car on désire maximiser une certaine expression (dépendant de d)
            # Comme l'algorithme recherche le coût minimum, on maximise la valeur en la rendant négative.
            mcf.add_edge(i+1, M+1+j, 1, -d*(d-30)*(d-30))
            # Capacité 1 car chaque couple ne peut être formé qu'une fois

    # Ajoute des arêtes de chaque sommet B[j] (les "femmes") au super-puits
    for i in range(W):
        # Capacité 1 (chaque femme ne peut être "prise" qu'une fois), coût 0
        mcf.add_edge(M+1+i, M+W+1, 1, 0)

    # Trouve le coût du couplage parfait maximal/minimum selon les règles définies ci-dessus.
    # min(M,W) car on ne peut matcher que jusqu'à ce que l'un des deux ensembles soit épuisé
    # Le résultat doit être rendu positif donc on affiche le coût opposé (car les coûts sont négatifs)
    print(-mcf.flow(0, M+W+1, min(M, W)))