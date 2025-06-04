import heapq  # Importe le module 'heapq' qui fournit une implémentation pour les files de priorité (min-heaps)
import sys    # Importe le module 'sys' pour manipuler des aspects du système Python, ici pour vérifier la version

# Gestion de la compatibilité entre Python 2 et 3 pour les fonctions 'range' et 'input'
if sys.version[0] == '2':  # Si le premier caractère du numéro de version (ex: '2.7') est '2', on est sous Python 2
    range, input = xrange, raw_input  # On redéfinit 'range' pour utiliser 'xrange' (version efficace de 'range' sous Python 2)
                                      # On redéfinit 'input' pour utiliser 'raw_input' (pour obtenir une chaîne de caractères)

# Définition de la classe MinCostFlow qui encapsule toute la logique nécessaire pour résoudre un problème de flot à coût minimum
class MinCostFlow:
    # Définition d'une classe interne Edge pour représenter une arête dans le graphe
    class Edge:
        # Constructeur pour une arête
        def __init__(self, to, cap, rev, cost):
            # 'to' : entier, le sommet d'arrivée de cette arête
            # 'cap' : entier, la capacité restante de l'arête (combien d'unité de flot elle peut supporter)
            # 'rev' : entier, l'indice de l'arête opposée (rétrograde) dans la liste des arêtes du sommet 'to'
            # 'cost' : entier, le coût unitaire de transporte du flot par cette arête
            self.to = to        # Affectation directe de l'argument 'to'
            self.cap = cap      # Affectation directe de 'cap'
            self.rev = rev      # Affectation directe de 'rev'
            self.cost = cost    # Affectation directe de 'cost'

    # Constructeur de la classe MinCostFlow
    def __init__(self, V):
        # 'V' représente le nombre total de sommets du graphe
        self.V = V
        # 'E' sera une liste de listes, où chaque élément (liste) correspond aux arêtes sortantes de chaque sommet
        self.E = [[] for _ in range(V)]  # Génération d'une liste vide pour chaque sommet, de longueur V

    # Méthode pour ajouter une arête au graphe
    def add_edge(self, fr, to, cap, cost):
        # 'fr' : sommet de départ
        # 'to' : sommet d'arrivée
        # 'cap' : capacité de l'arête
        # 'cost' : coût associé à traverser cette arête
        # On ajoute d'abord l'arête directe 'fr'->'to'
        self.E[fr].append(self.Edge(to, cap, len(self.E[to]), cost))
        # Ensuite, on ajoute l'arête rétrograde (reverse edge) qui servira pour les traitements de flot. Elle part de 'to' vers 'fr'
        # Sa capacité est mise à 0 et le coût est opposé pour permettre d'annuler un flot éventuellement.
        self.E[to].append(self.Edge(fr, 0, len(self.E[fr]) - 1, -cost))

    # Algorithme de calcul du flot à coût minimum
    def run(self, source, sink, f, INF=10**5):
        # 'source' : sommet source du flot
        # 'sink' : sommet puits
        # 'f' : quantité totale de flot à envoyer du source vers le puits
        # 'INF : grande valeur entière servant à initialiser les distances
        res = 0  # Initialisation de la variable résultat qui stockera le coût total
        # 'h' va contenir les potentials des sommets (pour la réduction des coûts par Johnson)
        h = [0] * self.V  
        # 'prevv' contiendra pour chaque sommet le sommet précédent sur le chemin de flot optimal
        prevv = [0] * self.V
        # 'preve' contiendra pour chaque sommet l'indice de l'arête par laquelle on est arrivé
        preve = [0] * self.V

        # Boucle principale tant qu'il reste du flot à faire passer
        while f > 0:
            # Initialisation de la file de priorité
            pque = []
            # Initialisation des distances depuis la source pour chaque sommet avec une valeur infinie de base
            dist = [INF] * self.V
            # La distance de la source à elle-même est toujours 0
            dist[source] = 0
            # On ajoute la source à la file de priorité avec une distance de 0
            heapq.heappush(pque, (0, source))

            # Boucle pour trouver le plus court chemin du source vers tous les autres sommets (Dijkstra adapté)
            while pque:
                cost, v = heapq.heappop(pque)  # Récupère le sommet 'v' avec le coût le plus faible actuellement dans la file
                cost = -cost  # On inverse le coût pour corriger car on a utilisé des valeurs négatives dans la file de priorité
                # Si la distance trouvée est supérieure à la valeur actuellement connue, on ne traite pas ce sommet
                if dist[v] < cost:
                    continue
                # Pour chaque arête sortant de 'v' (i : index, e : arête)
                for i, e in enumerate(self.E[v]):
                    # Si l'arête a encore une capacité (on peut passer du flot)
                    # ET si le chemin obtenu propose une amélioration sur la distance au sommet 'e.to'
                    if e.cap > 0 and dist[v] - h[e.to] < dist[e.to] - e.cost - h[v]:
                        # On calcule la nouvelle distance en prenant en compte le coût modifié par le potentiel (Johnson)
                        dist[e.to] = dist[v] + e.cost + h[v] - h[e.to]
                        # On note que pour atteindre 'e.to' le sommet précédent est 'v' et l'arête est indexée par 'i'
                        prevv[e.to] = v
                        preve[e.to] = i
                        # On ajoute à la file de priorité ce sommet avec coût négatif (pour obtenir un min-heap avec heapq)
                        heapq.heappush(pque, (-dist[e.to], e.to))

            # Si la distance pour atteindre le puits 'sink' est toujours à l'infini, c'est qu'il n'y a plus de chemin possible
            if dist[sink] == INF:
                return -1  # Renvoie -1 pour indiquer qu'il est impossible d'envoyer le flot demandé
            # Mise à jour des potentials pour le prochain tour (Johnson)
            for v in range(self.V):
                h[v] += dist[v]

            # On trouve la quantité minimale de flot qu'on peut envoyer sur ce chemin
            d = f  # On commence par supposer qu'on peut envoyer tout le flot restant
            v = sink
            # On remonte le chemin depuis le puits jusqu'à la source
            while v != source:
                # On prend le minimum entre d et la capacité de l'arête empruntée à l'étape précédente
                d = min(d, self.E[prevv[v]][preve[v]].cap)
                v = prevv[v]  # On passe au sommet précédent

            # On réduit la quantité de flot restant à envoyer
            f -= d
            # On ajoute au coût total le produit de la quantité de flot envoyée sur ce chemin et le potentiel final (qui donne le coût réel)
            res += d * h[sink]
            # Mise à jour du graphe résiduel : on retire 'd' unité de capacité sur les arêtes parcourues, et on augmente en sens inverse
            v = sink
            while v != source:
                # On retire 'd' du flot disponible sur l'arête 'prevv[v]' -> 'v'
                self.E[prevv[v]][preve[v]].cap -= d
                # On ajoute 'd' sur l'arête rétrograde correspondante ce qui permettrait, en théorie, d'annuler le flot
                self.E[v][self.E[prevv[v]][preve[v]].rev].cap += d
                v = prevv[v]  # On revient sur le sommet précédent

        # Lorsque le flot total a bien été envoyé, on renvoi la valeur du coût total du flot à coût minimum
        return res

# Lancement du programme principal : lecture des entrées et résolution répétée du problème jusqu'à saisie de 0
while True:
    # Lecture d'un entier depuis l'entrée standard représentant le nombre de requêtes (N)
    N = int(input())
    # Si la saisie est 0, on sort de la boucle : cela termine le programme
    if not N:
        break
    # On fixe le nombre de sommets à 366, probablement pour modéliser les jours d'une année (1 à 365 inclus) plus le jour 0
    V = 366
    # Création d'un objet MinCostFlow avec V sommets
    mcf = MinCostFlow(V)
    # On ajoute les arêtes allant de chaque jour au jour suivant, capacité 2, coût 0
    for i in range(V - 1):
        mcf.add_edge(i, i + 1, 2, 0)
    # Pour chaque requête utilisateur, on lit les 3 entiers (s, t, c)
    for _ in range(N):
        s, t, c = map(int, input().split())
        # On ajoute une arête allant du jour 's-1' au jour 't', de capacité 1, et de coût -c (coût négatif pour maximisation du bénéfice)
        mcf.add_edge(s - 1, t, 1, -c)
    # On lance l'algorithme de flot à coût minimum de 0 à V-1 (du premier au dernier jour), pour 2 unités de flot
    # On inverse le signe du coût final avec '-' pour afficher le bénéfice maximal (puisque le coût initial était négatif)
    print(-mcf.run(0, V - 1, 2, 10 ** 9))