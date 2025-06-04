# AOJ 2304 Reverse Roads
# Python3 2018.7.21 bal4u

# *******************************************
# Implémentation de l'Algorithme de Flot Maximum de Dinic
# *******************************************

class MaxFlow:
    # Le constructeur de la classe MaxFlow initialise la structure.
    # V : nombre de sommets (nœuds) du graphe.
    def __init__(self, V):
        self.V = V  # Le nombre de sommets dans le graphe
        # self.level : liste utilisée pour stocker le niveau (distance depuis la source) de chaque sommet lors du BFS
        self.level = [0] * V
        # self.iter : vecteur utilisé pour enregistrer l'indice de l'arête en cours d'exploration pour chaque sommet lors du DFS
        self.iter = [0] * V
        # self.edge : liste d'adjacence où chaque entrée est une liste représentant les arêtes sortantes du nœud
        # Chaque arête est représentée par une liste contenant :
        # [destination, capacité, indice de l'arête inverse dans la liste d'adjacence du sommet "destination"]
        self.edge = [[] for i in range(V)]

    # Fonction pour ajouter une arête orientée de 'fr' (source) vers 'to' (destination) avec une capacité 'cap'
    def add_edge(self, fr, to, cap):
        # 'f' est l'indice de la nouvelle arête dans la liste d’adjacence du sommet de départ (fr)
        # 't' est l'indice de la nouvelle arête dans la liste d’adjacence du sommet d’arrivée (to)
        # Elles aident à retrouver les arêtes réciproques lors de la mise à jour du flot
        f, t = len(self.edge[fr]), len(self.edge[to])
        # Ajoute l'arête réelle dans le sens de l’écoulement du flot
        self.edge[fr].append([to, cap, t])
        # Ajoute l'arête inverse (pour la capacité résiduelle) dans le sens inverse
        self.edge[to].append([fr, cap, f])

    # Fonction BFS pour construire le graphe de niveaux (parcours en largeur depuis la source)
    def bfs(self, s):
        # On réinitialise tous les niveaux à -1 (non visités)
        self.level = [-1] * self.V
        # La source s a un niveau 0
        self.level[s] = 0
        # File pour gérer les sommets à explorer (ici sous forme de liste)
        Q = []
        Q.append(s)
        # Continue tant qu'il reste des sommets à explorer dans la file
        while Q:
            # On retire un sommet de la file
            v = Q.pop()
            # On parcourt toutes les arêtes sortantes du sommet 'v'
            for to, cap, rev in self.edge[v]:
                # Si la capacité de l'arête est positive et que le sommet 'to' n'a pas encore été visité
                if cap > 0 and self.level[to] < 0:
                    # On l'étiquette avec son niveau (niveau parent + 1)
                    self.level[to] = self.level[v] + 1
                    # Et on l'ajoute à la file pour explorer ses voisins par la suite
                    Q.append(to)

    # Fonction DFS pour trouver des chemins augmentants dans le graphe de niveaux
    # v : sommet courant, t : puits, f : capacité pouvant être poussée
    def dfs(self, v, t, f):
        # Si le sommet courant est le puits, on retourne le flot pouvant être poussé
        if v == t:
            return f
        # Explore toutes les arêtes sortantes de 'v', à partir de la position stockée dans self.iter
        for i in range(self.iter[v], len(self.edge[v])):
            to, cap, rev = self.edge[v][i]
            # Si on a une capacité disponible (cap > 0) et que le sommet cible est plus profond dans le graphe de niveaux
            if cap > 0 and self.level[v] < self.level[to]:
                # Détermine la quantité de flot pouvant être poussée le long de ce chemin
                d = self.dfs(to, t, min(f, cap))
                # Si on peut pousser du flot dans ce chemin
                if d > 0:
                    # Réduit la capacité résiduelle sur l'arête directe
                    self.edge[v][i][1] -= d
                    # Augmente la capacité résiduelle sur l'arête inverse
                    self.edge[to][rev][1] += d
                    # Retourne le flot poussé
                    return d
            # Mets à jour l'indice actuel d'exploration des arêtes pour ce sommet
            self.iter[v] = i
        # Si aucun flot ne peut être poussé depuis ce sommet, retourne 0
        return 0

    # Fonction principale pour calculer le flot maximum entre une source s et un puits t
    # Le paramètre optionnel INF sert de borne supérieure au flot pouvant être envoyé à chaque recherche
    def maxFlow(self, s, t, INF=10**8):
        flow = 0  # Variable qui va accumuler la quantité totale de flot envoyée du s à t
        while True:
            # On reconstruit le graphe de niveaux depuis la source à chaque itération de Dinic
            self.bfs(s)
            # Si le puits n'est pas atteint, c'est que le flot maximum a été trouvé et on s'arrête
            if self.level[t] < 0:
                break
            # On réinitialise pour chaque DFS quel voisin a été testé pour chaque sommet
            self.iter = [0] * self.V
            # On essaie de pousser du flot autant que possible via des DFS successifs
            while True:
                f = self.dfs(s, t, INF)
                # Si aucun flot n'a pu être poussé, on sort de la boucle interne de DFS
                if f <= 0:
                    break
                # Sinon, on ajoute ce flot au total
                flow += f
        # On retourne le flot maximum trouvé
        return flow

# Lecture des données d'entrée

# On lit deux entiers, N (nombre de sommets) et M (nombre d'arêtes)
N, M = map(int, input().split())

# Construction d'une matrice 'dir' de taille NxN pour stocker la direction des arêtes
# dir[i][j] vaudra 1 s'il existe une arête dirigée de i vers j
dir = [[0 for j in range(N)] for i in range(N)]

# Construction d'une matrice 'id' de taille NxN pour mémoriser l'identifiant de l'arête allant de i vers j
# Cet identifiant est indexé à partir de 1 suivant l'ordre d'apparition de l'arête dans l'entrée
id = [[0 for j in range(N)] for i in range(N)]

# Création d'une instance de MaxFlow pour N sommets
d = MaxFlow(N)

# On itère sur toutes les M arêtes du graphe
for i in range(M):
    # Lecture d'une arête orientée, donnée par ses extrémités x et y (1-indexées dans l'entrée)
    x, y = map(int, input().split())
    # Conversion en indices de tableau 0-indexés (plus pratique en Python)
    x, y = x - 1, y - 1
    # On indique qu'il existe une arête de y vers x (pour la matrice dir ; voir la suite pour justification)
    dir[y][x] = 1
    # On mémorise l'identifiant de cette arête (i + 1)
    id[y][x] = i + 1
    # On ajoute l'arête au graphe de flot, dans le sens x -> y, avec une capacité de 1
    d.add_edge(x, y, 1)

# Lecture des numéros de la source (S) et du puits (T), 1-indexés dans l'entrée, correction en 0-indexée
S, T = map(int, input().split())

# Calcul du flot maximum entre S et T, résultat affiché
print(d.maxFlow(S - 1, T - 1))

# Initialisation de la liste des identifiants d'arêtes utilisées dans le flot maximum
ans = []
# Parcours de chaque sommet
for i in range(N):
    # Pour chaque arête sortante depuis i (pour chaque arête réelle ou inverse dans le graphe de flot résiduel)
    for to, cap, rev in d.edge[i]:
        # Si la capacité sur l'arête a été utilisée (cap < 1) et qu'il s'agit d'une arête réelle du graphe original
        if cap < 1 and dir[i][to]:
            # On ajoute l'identifiant de cette arête à notre liste de réponse (on retrouve l'id stocké précédemment)
            ans.append(id[i][to])

# On trie la liste des identifiants d'arêtes par ordre croissant
ans.sort()

# On affiche le nombre d'arêtes utilisées dans le flot maximum
print(len(ans))

# Si au moins une arête a été utilisée, on affiche ses identifiants, un par ligne
if len(ans) > 0:
    print(*ans, sep='\n')