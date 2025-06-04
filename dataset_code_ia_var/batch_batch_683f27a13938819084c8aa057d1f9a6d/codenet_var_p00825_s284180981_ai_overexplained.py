import heapq  # Importation du module heapq qui fournit une implémentation de la file de priorité (min-heap) en Python

# Définition de la classe MinCostFlow pour résoudre des problèmes de flot à coût minimal dans un graphe orienté avec capacités et coûts sur les arêtes
class MinCostFlow:
    # Définition de la classe interne Edge pour représenter une arête du graphe
    class Edge:
        # Initialisation d'une arête avec le sommet de destination 'to', la capacité 'cap', l'indice de l'arête inverse 'rev', et le coût 'cost'
        def __init__(self, to, cap, rev, cost):
            self.to = to              # Noeud de destination de l'arête
            self.cap = cap            # Capacité résiduelle de l'arête, c'est-à-dire le nombre d’unités de flot pouvant circuler dans cette arête
            self.rev = rev            # Indice de l’arête inverse dans la liste des arêtes du noeud de destination
            self.cost = cost          # Coût unitaire pour utiliser cette arête

    # Initialisation d’un objet MinCostFlow avec V sommets (numérotés de 0 à V-1)
    def __init__(self, V):
        self.V = V                                   # Nombre total de sommets dans le graphe
        self.E = [[] for _ in range(V)]              # Liste d'adjacence pour représenter les arêtes du graphe. self.E[u] va contenir toutes les arêtes partant du sommet u

    # Fonction pour ajouter une arête du sommet 'fr' vers le sommet 'to' avec capacité 'cap' et coût 'cost'
    # Ajoute aussi l’arête inverse (pour maintenir le flot résiduel)
    def add_edge(self, fr, to, cap, cost):
        # Ajout de l’arête directe
        self.E[fr].append(self.Edge(to, cap, len(self.E[to]), cost))
        # Ajout de l’arête résiduelle (arête inverse), de capacité nulle et de coût opposé à l’original
        self.E[to].append(self.Edge(fr, 0, len(self.E[fr]) - 1, -cost))

    # Méthode pour trouver le coût minimal nécessaire pour envoyer 'f' unités de flot du sommet 'source' jusqu'au sommet 'sink'
    # INF : valeur suffisamment grande pour être considérée comme "infini", utilisée pour l'initialisation des distances
    def run(self, source, sink, f, INF=10**5):
        res = 0                                  # Variable pour stocker le coût total accumulé du flot envoyé
        h = [0] * self.V                         # Tableau des potentiels pour chaque sommet, utilisé pour éliminer les cycles négatifs lors des relâchements
        prevv = [0] * self.V                     # prevv[v] sera utilisé pour retrouver le sommet précédent sur le chemin optimal vers v
        preve = [0] * self.V                     # preve[v] servira à retrouver l’indice de l’arête empruntée pour arriver à v depuis prevv[v]

        # Répéter jusqu’à ce qu’il n’y ait plus de flot à envoyer (c’est-à-dire, f == 0)
        while f > 0:
            # Initialisation du tableau des distances à l’infini (vecteur pour stocker la distance minimale estimée du 'source' à chaque sommet)
            dist = [INF] * self.V
            dist[source] = 0                     # La distance du sommet 'source' à lui-même est 0

            # File de priorité (min-heap), utilisée pour déterminer quel sommet traiter ensuite (choisit toujours celui avec la plus petite distance temporaire)
            pque = []                            # Chaque élément est un tuple (distance_negative, sommet)
            heapq.heappush(pque, (0, source))    # Ajoute le sommet source à la file avec distance nulle

            # Dijkstra modifié (utilise les potentiels / relèvements pour garantir l’absence de cycles de coût négatif)
            while pque:
                # Extraction du sommet avec la plus petite distance tempérée
                cost, v = heapq.heappop(pque)    # cost est l’opposé du coût (utilisation du min-heap comme max-heap, on le rend positif ensuite)
                cost = -cost

                # Si la distance enregistrée pour v est déjà meilleure, on saute
                if dist[v] < cost:
                    continue

                # Parcourt toutes les arêtes partant de v
                for i, e in enumerate(self.E[v]):
                    # On ne considère que les arêtes qui ont encore une capacité résiduelle
                    # Teste si le relèvement via v améliorera la distance à e.to
                    if e.cap > 0 and dist[v] - h[e.to] < dist[e.to] - e.cost - h[v]:
                        # On met à jour la distance à e.to avec le coût réel corrigé par les potentiels
                        dist[e.to] = dist[v] + e.cost + h[v] - h[e.to]
                        prevv[e.to] = v           # On mémorise le sommet précédent pour reconstituer le chemin plus tard
                        preve[e.to] = i           # On mémorise l’indice de l’arête utilisée depuis v
                        heapq.heappush(pque, (-dist[e.to], e.to)) # On ajoute e.to à la file de priorité (en mettant le coût en négatif pour le min-heap)

            # Si la distance jusqu’au sommet sink est toujours INF, il n’existe plus de chemin permettant d’augmenter le flot
            if dist[sink] == INF:
                return -1                        # On signale l’impossibilité d’envoyer le flot demandé

            # Mise à jour des potentiels h[] pour garantir la validité des relèvements futurs
            for v in range(self.V):
                h[v] += dist[v]

            # Recherche du chemin tracé pour déterminer le flot maximum d qui peut y être envoyé
            d = f                               # d sera le flot limité par les capacités minimales du chemin trouvé
            v = sink                            # On commence à partir du sink et on retrace jusqu'à la source
            while v != source:
                # On limite d à la capacité résiduelle minimale de toutes les arêtes du chemin
                d = min(d, self.E[prevv[v]][preve[v]].cap)
                v = prevv[v]

            f -= d                              # On diminue le flot restant à envoyer
            res += d * h[sink]                  # On ajoute le coût du flot envoyé au total résultant

            # On met à jour les capacités du graphe pour refléter le flot acheminé (chemin de flot augmenté)
            v = sink
            while v != source:
                # On diminue la capacité résiduelle de l’arête du chemin
                self.E[prevv[v]][preve[v]].cap -= d
                # On augmente la capacité résiduelle de l’arête inverse (réalisation du flot résiduel)
                self.E[v][self.E[prevv[v]][preve[v]].rev].cap += d
                v = prevv[v]

        return res                              # Retourne le coût total du flot envoyé

# Boucle principale du programme : le script accepte plusieurs problèmes jusqu’à ce qu’il reçoive un N nul
while True:
    N = int(input())             # Lecture du nombre N d'intervalles (réservations ou tâches, dépendant du contexte du problème)
    if not N:                    # Si N égal à 0, on sort de la boucle principale (fin du programme)
        break

    V = 366                      # Nombre total de sommets du graphe (représente les jours de l’année plus un sommet supplémentaire)
    mcf = MinCostFlow(V)         # Création d’un objet MinCostFlow pour un graphe avec V sommets

    # Ajout d’arêtes entre chaque jour consécutif, de capacité 2 et coût 0
    for i in range(V - 1):
        mcf.add_edge(i, i + 1, 2, 0)  # On modélise deux "places" disponibles chaque jour sans coût

    # Lecture des N intervalles et ajout de leurs arêtes correspondantes dans le graphe
    for _ in range(N):
        s, t, c = map(int, input().split()) # s: jour de début, t: jour de fin, c: "bénéfice" ou coût associé à cette réservation/tâche
        # On ajoute une arête du jour s-1 (début-1, car indexé depuis 0) jusqu’au jour t, capacité 1, coût -c (pour maximiser les bénéfices via le coût minimal)
        mcf.add_edge(s - 1, t, 1, -c)

    # Exécution de l’algorithme de flot à coût minimal : on veut envoyer 2 unités de flot du jour 0 au jour 365
    result = mcf.run(0, V - 1, 2, 10**9)  # On utilise une valeur INF très grande pour être sûr de ne pas limiter inutilement les distances
    print(-result)                        # On affiche l’opposé du coût retourné, ce qui correspond à la maximisation du bénéfice total (puisqu’on a ajouté les coûts en négatif)