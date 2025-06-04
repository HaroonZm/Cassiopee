import collections  # Importation du module collections pour utiliser la file deque

# Définition de la classe MaxFlow, qui va gérer le calcul du flot maximum dans un graphe
class MaxFlow:
    """
    Implémentation de l'algorithme de Dinic pour trouver le flot maximal dans un graphe orienté avec capacités sur les arêtes.
    La complexité théorique de cet algorithme est O(EV^2), où E est le nombre d'arêtes et V le nombre de sommets.
    Cette classe sera utilisée pour résoudre le problème de flot maximum.
    """

    # Définition de la classe interne Edge pour représenter une arête du graphe
    class Edge:
        def __init__(self, to, cap, rev):
            # 'to' représente le sommet vers lequel l'arête pointe
            # 'cap' est la capacité résiduelle de cette arête
            # 'rev' est l'indice de l'arête opposée dans la liste d'adjacence du sommet cible
            self.to = to
            self.cap = cap
            self.rev = rev

    def __init__(self, V):
        """
        Initialise l'objet MaxFlow.
        V : nombre de sommets dans le graphe (les sommets sont identifiés de 0 à V-1).
        E : liste d'adjacence (pour chaque sommet, une liste d'arêtes sortantes).
        """
        self.V = V  # Nombre total de sommets du graphe
        self.E = [[] for _ in range(V)]  # Création d'une liste vide pour chaque sommet pour stocker les arêtes sortantes

    def add_edge(self, fr, to, cap):
        """
        Ajoute une arête dirigée du sommet 'fr' vers le sommet 'to' avec une capacité 'cap'.
        Ajoute également l'arête de retour nécessaire pour l'algorithme (d'abord à capacité nulle).
        Les arêtes de retour sont utilisées sur le graphe résiduel pour permettre le retour de flot si besoin.
        """
        # Ajoute l'arête directe du sommet 'fr' vers 'to'
        self.E[fr].append(self.Edge(to, cap, len(self.E[to])))
        # Ajoute l'arête de retour de 'to' vers 'fr' de capacité 0 (arête résiduelle)
        # Le paramètre 'rev' pointe sur l'indice de l'arête retournée dans la liste d'adjacence de l'autre sommet
        self.E[to].append(self.Edge(fr, 0, len(self.E[fr])-1))

    def dinic(self, source, sink, INF=10**9):
        """
        Fonction qui recherche le flot maximum du sommet source vers le sommet puits 'sink'.
        La méthode utilise l'algorithme de Dinic (niveaux + DFS bloquée).
        INF : valeur représentant l'infini (utilisé pour initialiser les flots résiduels au départ).
        """
        maxflow = 0  # Initialisation de la valeur totale du flot à 0
        while True:  # Boucle principale
            self.bfs(source)  # Construction du graphe des niveaux depuis la source
            if self.level[sink] < 0:
                # Si le puits n'est pas accessible (niveau < 0), alors il n'y a plus de chemin augmentant possible
                return maxflow  # Le flot total trouvé est maximum
            self.itr = [0] * self.V  # Tableau pour garder la position actuelle de l'itérateur DFS pour chaque sommet
            while True:
                flow = self.dfs(source, sink, INF)  # Recherche d'un chemin augmentant du source au puits
                if flow > 0:
                    # Si un chemin a été trouvé, on ajoute son flot au flot total
                    maxflow += flow
                else:
                    # Aucun nouveau chemin n'a été trouvé : on passe à la prochaine construction de niveau
                    break

    def dfs(self, vertex, sink, flow):
        """
        Recherche récursive en profondeur (DFS) d'un chemin augmentant depuis le sommet 'vertex' jusqu'au 'sink'.
        'flow' indique la quantité maximale de flot qui peut encore être poussée sur ce chemin.
        """
        if vertex == sink:
            # Si on atteint le puits, on retourne la quantité de flot possible (qui pourrait être inférieure à 'flow')
            return flow
        # On parcourt toutes les arêtes sortantes de 'vertex', en commençant à partir de la dernière itérée
        for i in range(self.itr[vertex], len(self.E[vertex])):
            self.itr[vertex] = i  # On mémorise où on en est pour la prochaine DFS éventuelle
            e = self.E[vertex][i]  # On récupère l'arête courante
            # On vérifie deux conditions pour continuer sur cette arête :
            # 1. Sa capacité résiduelle doit être stricte > 0 (sinon elle est saturée)
            # 2. On ne retourne que si on descend dans le graphe des niveaux (niveau croissant)
            if e.cap > 0 and self.level[vertex] < self.level[e.to]:
                # Calcul du flot qu'on peut pousser (le minimum entre ce qu'on pouvait pousser jusqu'ici et la capacité résiduelle de l'arête)
                d = self.dfs(e.to, sink, min(flow, e.cap))
                if d > 0:
                    # S'il est possible de pousser du flot, alors réduction de la capacité résiduelle de l'arête
                    e.cap -= d
                    # Augmentation de la capacité sur l'arête résiduelle (retour) pour permettre l'annulation de flot
                    self.E[e.to][e.rev].cap += d
                    return d  # Retourne le flot réellement poussé sur ce chemin
        # Aucun flot n'a pu être poussé depuis ce sommet sur aucun chemin admissible
        return 0

    def bfs(self, start):
        """
        Recherche en largeur (BFS) pour construire le graphe des niveaux à partir du sommet 'start'.
        Ce graphe sera utilisé par les DFS pour limiter la recherche aux niveaux croissants (chemins les plus courts en nombre d'arêtes).
        """
        que = collections.deque()  # Initialisation d'une file pour la BFS
        # Tableau pour enregistrer le niveau de chaque sommet depuis 'start'. -1 indique que le sommet n'a pas encore été atteint.
        self.level = [-1] * self.V
        que.append(start)  # Ajoute le point de départ à la file
        self.level[start] = 0  # Le niveau du point de départ est 0

        # On boucle tant que la file de sommets à explorer n'est pas vide
        while que:
            fr = que.popleft()  # On prend le premier sommet de la file (FIFO)
            # Pour chaque arête sortante du sommet courant
            for e in self.E[fr]:
                # Si sa capacité résiduelle est positive et qu'on n'a pas encore assigné de niveau à sa destination
                if e.cap > 0 and self.level[e.to] < 0:
                    # On pose le niveau du sommet d'arrivée à un de plus que celui d'origine
                    self.level[e.to] = self.level[fr] + 1
                    # On ajoute ce sommet à la file pour continuer la BFS
                    que.append(e.to)

# Lecture du nombre de sommets (N) et du nombre d'arêtes (M) depuis l'entrée standard
N, M = map(int, input().split())

# Création d'un objet MaxFlow avec N sommets
mf = MaxFlow(N)

# Tableau pour enregistrer certaines informations sur les arêtes, afin de les manipuler plus tard si besoin
rev_edge = []

# Pour chaque arête à lire
for i in range(M):
    # Lecture des extrémités de l'arête (indices 1-based à convertir en 0-based)
    s, t = [int(x)-1 for x in input().split()]
    # Ajout d'une arête de s vers t de capacité 1
    mf.add_edge(s, t, 1)
    # Ajout d'une arête de t vers s de capacité 1 (l'arête reste non-orientée pour ce problème)
    mf.add_edge(t, s, 1)
    # On stocke l'identifiant de l'arête, l'extrémité t, et l'indice de la dernière arête ajoutée à E[t]
    rev_edge.append((i+1, t, len(mf.E[t])-1))

# Lecture des indices du sommet source et du sommet puits, au format 1-based puis conversion en 0-based
source, sink = [int(x)-1 for x in input().split()]

# Appel à la méthode dinic pour calculer le flot maximum. On affiche le résultat (nombre entier)
print(mf.dinic(source, sink))

# On prépare à enregistrer les indices des arêtes qui ont été utilisées dans le flot maximal calculé
ans = []

# Pour chaque arête mémorisée plus tôt
for i, t, idx in rev_edge:
    e = mf.E[t][idx]  # Récupère l'arête correspondante
    # On vérifie la capacité résiduelle de l'arête retournée (complémentaire) dans le flot maximal
    if mf.E[e.to][e.rev].cap == 1:
        # Si la capacité est exactement 1, cela veut dire que ce flot est bien passé par cette arête (l'arête originale a été "saturée" dans l'autre sens)
        ans.append(i)  # On enregistre l'identifiant de cette arête

# On affiche d'abord le nombre d'arêtes effectivement utilisées dans un flot maximum
print(len(ans))
# S'il y a effectivement des arêtes concernées, on affiche leurs identifiants, une par ligne
if ans:
    print(*ans, sep='\n')