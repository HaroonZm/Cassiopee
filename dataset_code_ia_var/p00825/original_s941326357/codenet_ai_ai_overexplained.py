import heapq   # Importe le module heapq, utilisé pour créer une file de priorité (priority queue)
import sys     # Importe le module sys, utilisé pour accéder à des fonctions système comme la version de Python

# Vérification de la version de Python. Si la version principale ('major') est '2'
if sys.version[0] == '2':
    # Redéfinit range en xrange (qui était plus efficace en Python 2) et input en raw_input (pour compatibilité)
    range, input = xrange, raw_input

# Définition de la classe MinCostFlow qui permet de résoudre le problème de flot de coût minimal
class MinCostFlow:
    # Classe interne Edge, représentant une arête dans le graphe
    class Edge:
        # Fonction d'initialisation (constructeur) de la classe Edge
        def __init__(self, to, cap, rev, cost):
            # 'to' : sommet d'arrivée de l'arête
            # 'cap': capacité résiduelle de l'arête
            # 'rev': index de l'arête résiduelle dans le graphe opposé
            # 'cost': coût (pondération) associé au passage de cette arête
            self.to = to
            self.cap = cap
            self.rev = rev
            self.cost = cost

    # Initialisation de la classe MinCostFlow
    def __init__(self, V):
        # 'V' : nombre total de sommets dans le graphe
        self.V = V
        # Création d'une liste d'adjacence 'E' pour mémoriser toutes les arêtes (= listes d'Edge pour chaque sommet)
        self.E = [[] for _ in range(V)]

    # Fonction pour ajouter une arête orientée du sommet 'fr' vers 'to' avec capacité 'cap' et coût 'cost'
    def add_edge(self, fr, to, cap, cost):
        # Ajout de l'arête directe
        #   - va du sommet 'fr' vers 'to'
        #   - capacité 'cap'
        #   - l'indice de l'arête reverse (dans self.E[to]) est la longueur actuelle de la liste self.E[to]
        #   - coût de passage 'cost'
        self.E[fr].append(self.Edge(to, cap, len(self.E[to]), cost))
        # Ajout d'une arête résiduelle (reverse) de 'to' vers 'fr'
        #   - capacité 0 (il n'existe pas dans le graphe original), mais sert pour le flot résiduel
        #   - l'indice reverse est len(self.E[fr]) - 1 pour pointer vers l'arête directe ajoutée juste avant
        #   - coût négatif de l'arête directe (pour les annulations)
        self.E[to].append(self.Edge(fr, 0, len(self.E[fr]) - 1, -cost))

    # Fonction principale pour trouver le flot de coût minimum du sommet 'source' à 'sink' pour un flot 'f'
    # 'INF' représente un coût ou une distance infinie (pour l'initialisation)
    def run(self, source, sink, f, INF=10**5):
        res = 0  # Résultat final du coût total
        # h : Potentiel de chaque sommet (pour réduire les coûts négatifs)
        # prevv : tableau pour mémoriser le précédent sommet dans le chemin optimal
        # preve : tableau pour mémoriser l'indice de l'arête choisie dans le chemin optimal
        h = [0] * self.V
        prevv = [0] * self.V
        preve = [0] * self.V
        # Tant qu'il reste du flot à pousser
        while (f > 0):
            pque = []  # File de priorité (priority queue) pour le plus court chemin (Dijkstra modifié)
            # dist : tableau des distances (coût minimal pour atteindre chaque sommet depuis la source)
            dist = [INF] * self.V
            dist[source] = 0  # La distance pour atteindre la source depuis la source est 0
            # On met la source dans la priority queue, avec priorité 0
            heapq.heappush(pque, (0, source))
            # Boucle du Dijkstra pour chercher le chemin de coût minimal
            while pque:
                cost, v = heapq.heappop(pque)  # Extraction du sommet ayant le plus petit coût actuel
                cost = -cost  # Correction car on inverse ici pour un max-heap (à cause de la négation d'enqueue)
                # Si la distance stockée est déjà meilleure que le coût trouvé, on passe ce sommet
                if dist[v] < cost:
                    continue
                # Parcours de toutes les arêtes à partir du sommet courant
                for i, e in enumerate(self.E[v]):
                    # Si l'arête a encore une capacité résiduelle
                    if e.cap > 0 and dist[v] - h[e.to] < dist[e.to] - e.cost - h[v]:
                        # Calcul du coût pour atteindre e.to à partir de v, en prenant en compte les potentiels h[]
                        dist[e.to] = dist[v] + e.cost + h[v] - h[e.to]
                        prevv[e.to] = v  # On mémorise le sommet courant comme précédent
                        preve[e.to] = i  # On mémorise l'indice de l'arête utilisé
                        # On ajoute le sommet voisin dans la pile de priorité, avec son coût (nécessaire d'inverser signe)
                        heapq.heappush(pque, (-dist[e.to], e.to))
            # Si la distance pour atteindre le puits (sink) est encore infinie, il n'y a plus de chemin, donc échec
            if dist[sink] == INF:
                return -1  # On retourne une valeur spéciale pour indiquer l'échec
            # Mise à jour des potentiels pour chaque sommet, augmentation par la plus courte distance trouvée
            for v in range(self.V):
                h[v] += dist[v]
            # Recherche du minimum de capacité résiduelle sur le chemin trouvé (pour déterminer combien de flot on pousse)
            d = f  # d : quantité de flot que l'on va pousser
            v = sink
            while v != source:
                # On cherche la plus petite capacité sur le chemin, car on ne peut pas pousser plus que ça
                d = min(d, self.E[prevv[v]][preve[v]].cap)
                v = prevv[v]
            f -= d  # On enlève de la demande le flot que l'on vient de pousser
            res += d * h[sink]  # On ajoute au coût total : quantité de flot poussée * coût total du chemin
            v = sink
            # Mise à jour effective du graphe résiduel : on retire le flot des arêtes parcourues et on ajoute sur les reverses
            while v != source:
                self.E[prevv[v]][preve[v]].cap -= d  # On réduit la capacité sur l'arête principale
                self.E[v][self.E[prevv[v]][preve[v]].rev].cap += d  # On augmente la capacité de retour (reverse)
                v = prevv[v]  # On remonte d'un étage dans le chemin
        return res  # On renvoie le coût total du flot poussé

# Boucle principale du programme
while True:
    N = int(input())  # Lecture d'un entier N (représente probablement le nombre de demandes ou réservations)
    if not N:  # Si N vaut 0, on termine la boucle principale
        break
    V = 366  # Nombre total de sommets dans le graphe (ici, 366 pour tenir compte des 365 jours + sommet extra)
    mcf = MinCostFlow(V)  # Création d'une instance de MinCostFlow avec V sommets
    # Ajout d'arêtes de capacité deux (2) entre chaque jour consécutif, coût nul (peut représenter disponibilité)
    for i in range(V - 1):
        mcf.add_edge(i, i + 1, 2, 0)
    # Pour chaque demande d'utilisateur (N fois)
    for _ in range(N):
        s, t, c = map(int, input().split())  # Lecture de trois entiers : début (s), fin (t), coût (c)
        # Ajout d'une arête du jour s-1 au jour t, capacité 1 (une réservation), coût négatif (pour maximiser le gain)
        mcf.add_edge(s - 1, t, 1, -c)
    # Résolution du problème de flot de coût min du jour 0 au dernier jour, pour 2 unités de flot (peut-être 2 ressources)
    # - On inverse le coût pour avoir la maximisation des gains
    print(-mcf.run(0, V - 1, 2, 10 ** 9))  # Affichage du résultat (le moins négatif -> maximisation)