# *******************************************************
# AOJ 2304 Reverse Roads - Python3 2018.7.21 bal4u
# Réécriture complètement commentée du code donné, 
# avec des explications très détaillées de chaque ligne 
# et concept, aussi basique soit-il.
# *******************************************************

# Déclaration d'une constante pour l'infini (utilisée dans l'algorithme du flot maximum)
INF = 0x7fffffff  # Valeur très grande utilisée pour représenter "l'infini"

# Définition de la classe Donic qui implémente l'algorithme de Dinic pour le flot maximum sur un graphe
class Donic:
    def __init__(self, V):
        # Cette méthode spéciale est le constructeur appelé lors de la création d'un objet Donic
        # V : nombre total de sommets dans le graphe
        self.V = V  # Stocke le nombre de sommets
        self.level = [0] * V  # Liste pour stocker le niveau de chaque sommet durant le BFS, initialisée à 0
        self.iter = [0] * V   # Liste utilisée pour éviter de répéter les recherches d'arcs lors du DFS, initialisée à 0
        # La variable 'edge' est une liste de listes qui stocke les arêtes sortantes pour chaque sommet
        # Chaque arête est représentée par [destination, capacité, index de l'arête inverse dans le sommet destination]
        self.edge = [[] for i in range(V)]  # Créée par compréhension de liste, une liste vide par sommet

    def add_edge(self, frm, to, cap):
        # Ajoute une arête entre deux sommets avec la capacité donnée
        # frm : sommet de départ de l'arête
        # to : sommet d'arrivée de l'arête
        # cap : capacité de l'arête (c'est-à-dire le flux maximal possible sur cette arête)
        # f et t stockent la position respective où la nouvelle arête sera ajoutée dans chaque liste d'adjacence,
        # c'est utilisé pour le suivi de l'arête inverse
        f, t = len(self.edge[frm]), len(self.edge[to])
        # Ajoute une nouvelle arête dans la liste des arêtes du sommet frm
        # [to, cap, t] : to est le sommet d'arrivée, cap la capacité, t est l'index de l'arête inverse dans edge[to]
        self.edge[frm].append([to, cap, t])
        # Ajoute l'arête inverse (pour le graphe résiduel), capacité d'origine (pour gérer la suppression)
        self.edge[to].append([frm, cap, f])

    def bfs(self, s):
        # Effectue une recherche en largeur (BFS) depuis le sommet 's'
        # Sert à construire le graphe des niveaux nécessaire à l'algorithme de Dinic
        self.level = [-1] * self.V  # Initialement tous les niveaux sont à -1 (inaccessible)
        self.level[s] = 0  # Le niveau du sommet source est 0 (puisqu'on démarre ici)
        Q = []  # La variable Q sera utilisée comme file pour stocker les sommets à visiter
        Q.append(s)  # On commence en ajoutant s à la file
        while Q:
            v = Q.pop()  # Retire un sommet de la file (ici on l'utilise comme pile, donc l'ordre n'est pas garanti optimal)
            for to, cap, rev in self.edge[v]:  # Pour chaque arête sortant du sommet v
                # Si l'arête a encore de la capacité résiduelle et que le sommet d'arrivée n'a pas été visité
                if cap > 0 and self.level[to] < 0:
                    self.level[to] = self.level[v] + 1  # Le niveau du sommet d'arrivée est le niveau du sommet courant + 1
                    Q.append(to)  # Ajoute le sommet d'arrivée à la file pour le visiter plus tard

    def dfs(self, v, t, f):
        # Effectue une recherche en profondeur (DFS) du sommet v vers le sommet t avec un flot disponible f
        # v : sommet courant
        # t : sommet terminal (but)
        # f : flot disponible que l'on tente d'envoyer
        if v == t:
            # Condition d'arrêt : si le sommet courant est le terminal, retourner le flot f
            return f
        k = self.iter[v]  # Commence à regarder la prochaine arête à partir de l'indice stocké pour éviter de revisiter des arcs inutiles
        while k < len(self.edge[v]):  # Parcourt toutes les arêtes sortantes restantes de v
            to, cap, rev = self.edge[v][k]  # Décompose l'arête
            # On ne traverse l'arête que si elle a une capacité résiduelle > 0 et que to est à un niveau supérieur à v 
            if cap > 0 and self.level[v] < self.level[to]:
                # On ne peut pas envoyer plus de flotte que la capacité de l'arête, ni que f lui-même
                d = self.dfs(to, t, f if f <= cap else cap)
                if d > 0:
                    # Si un flot strictement positif a pu être envoyé, mettre à jour les capacités
                    self.edge[v][k][1] -= d  # Diminue la capacité résiduelle sur l'arête vers 'to'
                    self.edge[to][rev][1] += d  # Augmente la capacité sur l'arête inverse dans le sens opposé
                    return d  # Retourne le flot trouvé sur ce chemin
            self.iter[v] += 1  # Passe à l'arête suivante
            k += 1
        return 0  # Si aucun flot n'a pu être envoyé, retourne 0

    def maxFlow(self, s, t):
        # Calcule la valeur maximale du flot de s vers t dans le graphe à l'aide de Dinic
        # s : sommet source du flot
        # t : sommet puit/terminal du flot
        flow = 0  # Stocke la quantité totale de flot envoyée du début à la fin
        while True:
            self.bfs(s)  # Met à jour les niveaux de chaque sommet à chaque itération principale
            if self.level[t] < 0:
                # Si on ne peut plus atteindre le sommet terminal depuis la source, l'algo s'arrête
                break
            self.iter = [0] * self.V  # Réinitialise les indices d'itération du DFS pour chaque sommet
            while True:
                # On envoie autant de flots augmentants que possible sur le réseau de niveaux avant de rebâtir les niveaux
                f = self.dfs(s, t, INF)  # Essaie de pousser le flot maximal dans le graphe de niveaux
                if f <= 0:
                    # Si aucun flot supplémentaire ne peut être envoyé, on arrête et refait un BFS
                    break
                flow += f  # Ajoute le flot trouvé au flot total
        return flow  # Retourne le flot total maximal trouvé du sommet s au sommet t

# Lecture du nombre de sommets et d'arêtes du graphe
N, M = map(int, input().split())  # N: nombre de sommets, M: nombre d'arêtes
# Initialise deux matrices de taille N x N (avec des zéros)
# dir[i][j] indique s'il existe une arête dirigée de j vers i dans les données (pour l'identification dans la dernière phase)
# id[i][j] stocke l'identifiant associé à l'arête de j vers i, pour l'affichage final
dir = [[0 for j in range(N)] for i in range(N)]  # crée une matrice de zéros indiquant la direction des arcs
id =  [[0 for j in range(N)] for i in range(N)]  # crée une matrice pour stocker l'identifiant unique de chaque arc

# Création du graphe de flot en initialisant un objet Donic avec N sommets
d = Donic(N)

# Boucle pour lire les M arêtes
for i in range(M):
    x, y = map(int, input().split())  # Lecture des sommets x et y (donné au format 1-based dans l'entrée)
    x, y = x-1, y-1  # Convertit de 1-based à 0-based car les listes Python commencent à 0
    dir[y][x] = 1  # Marque dans dir qu'il y a une arête de x vers y
    id[y][x] = i+1  # Stocke l'identifiant unique de cette arête (à partir de 1, pas de 0)
    d.add_edge(x, y, 1)  # Ajoute l'arête au graphe de flot, capacité 1 (car le flot maximal par route est de 1)

# Lecture des sommets source et terminaux pour le flot maximal
S, T = map(int, input().split())  # Lecture de la source (S) et du puits (T)
# Calcul et affichage du flot maximum possible de S à T (tout en convertissant S,T au format 0-based)
print(d.maxFlow(S-1, T-1))

# Récupération des identifiants des arêtes utilisées dans le flot maximum
ans = []  # Va contenir les identifiants des arêtes empruntées dans le flot maximal
# Parcourt tous les sommets de 0 à N-1
for i in range(N):
    # Pour chaque arête sortante de i
    for to, cap, rev in d.edge[i]:
        # On regarde si 'cap' est maintenant < 1 et si l'arête existait dans les données d'entrée
        if cap < 1 and dir[i][to]:
            # Cela signifie que cette arête a été utilisée lors du flot maximal
            ans.append(id[i][to])  # Ajoute l'identifiant de cette arête à la réponse

# Trie les identifiants des arêtes utilisées dans l'ordre croissant, comme demandé par l'énoncé du problème
ans.sort()
print(len(ans))  # Affiche le nombre total d'arêtes empruntées dans le flot maximal

# Si au moins une arête a été utilisée, affiche ses identifiants (un par ligne)
if len(ans) > 0:
    print(*ans, sep='\n')  # Le *dépaquette* la liste ans pour print, sep='\n' force un saut de ligne par identifiant