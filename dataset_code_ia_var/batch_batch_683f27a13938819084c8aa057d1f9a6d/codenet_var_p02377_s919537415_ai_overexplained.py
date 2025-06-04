import heapq  # Importation de la bibliothèque heapq qui fournit une implémentation pour créer des files de priorité (tas binaire).

class MinCostFlow:
    # La classe MinCostFlow implémente l’algorithme de flot de coût minimum dans un graphe orienté à capacité.

    class Edge:
        # Classe interne qui représente une arête dans le graphe, utilisée pour stocker les informations sur chaque connexion.
        def __init__(self, to, cap, rev, cost):
            # Constructeur pour initialiser l’objet arête.
            # 'to' : le sommet de destination de l’arête.
            # 'cap' : la capacité résiduelle de l’arête (combien de flot peut encore passer).
            # 'rev' : l’indice de l’arête inverse dans la liste d’adjacence du sommet 'to'.
            # 'cost' : le coût unitaire pour faire passer une unité de flot sur cette arête.
            self.to = to          # Attribut pour stocker le sommet de destination.
            self.cap = cap        # Attribut pour la capacité résiduelle.
            self.rev = rev        # Attribut pour l’indice de l’arête inverse.
            self.cost = cost      # Attribut pour le coût du flot sur cette arête.

    def __init__(self, n, inf=1000000007):
        # Constructeur de la classe MinCostFlow.
        # 'n' : nombre de sommets dans le graphe.
        # 'inf' : une très grande valeur représentant l’infini, pour l’initialisation des distances.
        self.n = n                         # Nombre total de sommets dans le graphe.
        self.inf = inf                     # Valeur d’infini choisie pour éviter de saturer les chemins.
        self.e = [[] for _ in range(n)]    # Liste d’adjacence : chaque entrée correspond à une liste d’arêtes sortantes du sommet.

    def add_edge(self, fr, to, cap, cost):
        # Méthode pour ajouter une arête au graphe.
        # 'fr' : sommet de départ (entier).
        # 'to' : sommet d’arrivée (entier).
        # 'cap' : capacité de l’arête.
        # 'cost' : coût unitaire pour acheminer le flot via cette arête.
        # Ajoute l’arête directe et l’arête résiduelle/inverse avec capacité nulle et coût opposé.
        self.e[fr].append(self.Edge(to, cap, len(self.e[to]), cost))            # Ajout de l’arête réelle.
        self.e[to].append(self.Edge(fr, 0, len(self.e[fr]) - 1, -cost))         # Ajout de l’arête inverse (pour flot résiduel).

    def compute(self, source, sink, f):
        # Fonction principale pour calculer le coût minimal pour envoyer 'f' unités de flot de 'source' à 'sink'.
        # 'source' : sommet de départ.
        # 'sink' : sommet d’arrivée.
        # 'f' : montant total du flot que l’on veut envoyer.
        res = 0                                   # Variable pour accumuler le coût total du flot envoyé.
        h = [0] * self.n                          # Potentiel de chaque sommet (pour éviter les cycles de coût négatif et accélérer la recherche de chemin).
        prevv = [0] * self.n                      # Tableau pour mémoriser le sommet précédent sur le chemin d’augmentation.
        preve = [0] * self.n                      # Tableau pour mémoriser l’arête utilisée pour venir à chaque sommet sur le chemin.
        while f > 0:                              # Continue tant qu’il faut encore envoyer du flot.
            pq = []                               # Initialisation d’une file de priorité pour la recherche des plus courts chemins.
            dist = [self.inf] * self.n            # Table des distances initialisée à l’infini pour tous les sommets.
            dist[source] = 0                      # La distance jusqu’à la source est nulle (point de départ).
            heapq.heappush(pq, (0, source))       # Ajout dans la file de priorité : on commence à explorer la source.
            while pq:
                # Boucle principale pour extraire le sommet de plus faible coût et détendre ses voisins.
                cost, v = heapq.heappop(pq)   # Récupère et supprime le sommet avec la plus petite distance (coût) actuelle.
                cost = -cost                  # Inverse le signe, car on stocke les coûts négatifs pour faire du min-heap (priorité au coût minimum).
                if dist[v] < cost:            # Si une meilleure distance a déjà été trouvée pour ce sommet, on ignore.
                    continue
                for i, edge in enumerate(self.e[v]):
                    # Parcours de chaque arête sortante du sommet courant pour trouver de meilleurs chemins.
                    if edge.cap > 0 and dist[v] - h[edge.to] < dist[edge.to] - edge.cost - h[v]:
                        # On vérifie que l’arête n’est pas saturée (capacité > 0).
                        # Deuxième condition : vérifie si le nouveau chemin offre une meilleure distance (prise en compte du potentiel pour l’optimisation).
                        dist[edge.to] = dist[v] + edge.cost + h[v] - h[edge.to]   # Mise à jour de la meilleure distance trouvée pour 'edge.to'.
                        prevv[edge.to] = v                                        # On note le sommet précédent pour pouvoir remonter le chemin plus tard.
                        preve[edge.to] = i                                        # On note quelle arête a été utilisée pour remonter.
                        heapq.heappush(pq, (-dist[edge.to], edge.to))             # On ajoute ce nœud à la file de priorité pour exploration.
            if dist[sink] == self.inf:
                # Si on n’a pas pu atteindre le puits (sink), alors il n’existe plus de chemin admissible et on ne peut plus pousser de flot.
                return -1                     # Retourne -1 pour signaler l’impossibilité de compléter la demande de flot.
            for v in range(self.n):
                # Mise à jour du potentiel pour tous les sommets afin d’assurer l’optimalité et garantir l’absence de cycles négatifs.
                h[v] += dist[v]
            d, v = f, sink
            # On recherche la quantité de flot que l’on peut envoyer sur ce chemin d’augmentation :
            # c’est le flot minimal parmi toutes les arêtes traversées.
            while v != source:
                # On remonte le chemin depuis le puits jusqu’à la source en calculant le goulot d’étranglement (capacité minimale).
                d = min(d, self.e[prevv[v]][preve[v]].cap)
                v = prevv[v]
            f -= d                # On diminue la quantité de flot restant à envoyer.
            res += d * h[sink]    # On ajoute au résultat le coût induit par ce chemin augmenté par le potentiel final atteint.
            v = sink
            while v != source:
                # On met à jour les capacités sur le chemin d’augmentation sélectionné :
                # on diminue la capacité de l’arête directe, et on augmente la capacité de l’arête inverse.
                self.e[prevv[v]][preve[v]].cap -= d
                self.e[v][self.e[prevv[v]][preve[v]].rev].cap += d
                v = prevv[v]       # On poursuit la remonte jusqu’à la source.
        return res                 # Retourne finalement le coût total du flot envoyé.

def main():
    # Fonction principale exécutée lors de l’exécution directe du script.
    v, e, f = map(int, input().split())
    # Lecture des trois premiers entiers depuis l’entrée standard :
    # 'v' : le nombre de sommets,
    # 'e' : le nombre d’arêtes,
    # 'f' : le flot total à envoyer.
    MCF = MinCostFlow(v)         # Instanciation de l’objet de flot de coût minimum avec 'v' sommets.
    for _ in range(e):
        # Boucle pour lire et ajouter chacune des 'e' arêtes au graphe.
        a, b, c, d = map(int, input().split())
        # 'a' : sommet d’origine de l’arête,
        # 'b' : sommet de destination,
        # 'c' : capacité de l’arête,
        # 'd' : coût unitaire pour l’arête.
        MCF.add_edge(a, b, c, d) # Ajoute cette arête au graphe.
    print(MCF.compute(0, v - 1, f))
    # Exécute l’algorithme pour envoyer 'f' unités de flot du sommet 0 (source) au sommet v-1 (sink).
    # Affiche le coût total minimal trouvé (ou -1 si impossible).

if __name__ == '__main__':
    main()
    # Ce bloc garantit que la fonction main() ne sera exécutée que si ce fichier est lancé directement,
    # et non s’il est importé comme module dans un autre code.