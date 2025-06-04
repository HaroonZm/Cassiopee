import collections  # Importation du module collections qui contient des structures de données comme deque (file à double extrémité), utile pour le BFS
import sys  # Importation du module sys pour accéder aux informations liées à l’interpréteur Python

# Compatibilité avec Python 2 : dans Python 2, xrange est le générateur équivalent à range, et raw_input équivaut à input
if sys.version[0] == '2':
    range, input = xrange, raw_input

class MaxFlow:
    """
    Algorithme de Dinic pour calculer le flot maximum (max-flow) dans un graphe orienté et pondéré en capacités.
    Complexité : O(EV^2) où E est le nombre d'arêtes et V le nombre de sommets.
    """

    class Edge:
        """
        Représente une arête dans le graphe avec :
        - to : le sommet d'arrivée (destination de l'arête)
        - cap : la capacité restante sur cette arête
        - rev : l'index de l'arête de retour dans la liste du sommet d'arrivée (pour l'arête résiduelle)
        """
        def __init__(self, to, cap, rev):
            # Attribue le sommet de destination, la capacité et l'index de l'arête de retour
            self.to = to
            self.cap = cap
            self.rev = rev

    def __init__(self, V):
        """
        Initialise le graphe avec :
        - V : le nombre total de sommets (numérotés de 0 à V-1)
        - E : la liste d'adjacence du graphe, où chaque case contient une liste d'arêtes partant de ce sommet
        """
        self.V = V  # Nombre de sommets
        self.E = [[] for _ in range(V)]  # Liste d'adjacence vide pour chaque sommet

    def add_edge(self, fr, to, cap):
        """
        Ajoute une arête dirigée (et son arête de retour) entre deux sommets :
        - fr : sommet de départ de l'arête
        - to : sommet d'arrivée de l'arête
        - cap : capacité maximale de l'arête
        Pour chaque arête normale, ajoute aussi une arête retour ayant une capacité nulle.
        """
        # Ajout de l'arête principale de fr vers to
        self.E[fr].append(self.Edge(to, cap, len(self.E[to])))
        # Ajout de l'arête retour (pour le graphe résiduel, capacité initiale 0)
        self.E[to].append(self.Edge(fr, 0, len(self.E[fr]) - 1))

    def run(self, source, sink, INF=10**9):
        """
        Calcule le flot maximum du sommet source vers le sommet sink en utilisant l’algorithme de Dinic.
        - source : point de départ du flot
        - sink : point d’arrivée du flot
        - INF : valeur utilisée pour représenter l'infini (capacité illimitée fictive)
        Retourne la valeur du flot maximum trouvée.
        """
        maxflow = 0  # Initialisation du flot maximum total à zéro
        while True:  # Boucle jusqu'à ce qu'il n'existe plus de chemin augmentant
            self.bfs(source)  # Enregistre le niveau de chaque sommet à partir de source
            if self.level[sink] < 0:  # Si le sink est inatteignable, terminer
                return maxflow  # Retourner le flot maximum accumulé
            self.itr = [0] * self.V  # Indice d'exploration de chaque sommet pour DFS
            while True:
                flow = self.dfs(source, sink, INF)  # Cherche un chemin augmentant
                if flow > 0:
                    maxflow += flow  # Ajoute le flot trouvé
                else:
                    break  # Aucun autre chemin augmentant possible dans ce calque

    def dfs(self, vertex, sink, flow):
        """
        Parcourt le graphe en profondeur (Depth-First Search) pour trouver un chemin augmentant du vertex au sink.
        - vertex : sommet courant à explorer
        - sink : objectif à atteindre 
        - flow : capacité maximale pouvant encore circuler dans ce chemin partiel
        Retourne le min entre flow et la capacité trouvée sur le chemin, ou 0 si aucun chemin n’est possible.
        """
        if vertex == sink:
            return flow  # Si on est au sink, retourne le flot possible
        for i in range(self.itr[vertex], len(self.E[vertex])):  # Parcours les arêtes à partir du sommet vertex
            self.itr[vertex] = i  # Met à jour l’index courant pour éviter de le refaire
            e = self.E[vertex][i]  # Récupère l'arête i partant du sommet courant
            # Condition pour avancer : s'il reste de la capacité et si le niveau du voisin > au niveau actuel
            if e.cap > 0 and self.level[vertex] < self.level[e.to]:
                # Cherche plus loin, la capacité minimale entre ce qui reste à passer et la capacité de l'arête
                d = self.dfs(e.to, sink, min(flow, e.cap))
                if d > 0:
                    # Soustraire le flot sur l'arête directe (utilise de la capacité)
                    e.cap -= d
                    # Ajoute le flot sur l'arête de retour (pour éventuellement y "revenir" avec le flot résiduel)
                    self.E[e.to][e.rev].cap += d
                    return d  # Retourne le flot utilisé dans ce chemin
        return 0  # Aucun chemin permettant d’augmenter le flot

    def bfs(self, start):
        """
        Parcours en largeur (Breadth-First Search) pour calculer le niveau (distance minimale) de chaque sommet depuis start.
        Utilisé pour construire le graphe des niveaux dans Dinic.
        - start : sommet de départ (source)
        """
        que = collections.deque()  # Crée une file pour explorer les sommets
        self.level = [-1] * self.V  # Initialise tous les niveaux à -1 (non visités)
        que.append(start)  # Commence à explorer depuis le sommet start
        self.level[start] = 0  # Le niveau du sommet de départ est 0

        while que:  # Tant qu’il y a des sommets à explorer
            fr = que.popleft()  # Récupère le sommet en tête de file
            for e in self.E[fr]:  # Parcourt toutes les arêtes sortantes
                # Si l'arête a encore de la capacité et que le sommet d'arrivée n'a pas encore de niveau
                if e.cap > 0 and self.level[e.to] < 0:
                    self.level[e.to] = self.level[fr] + 1  # Attribue le niveau au sommet voisin
                    que.append(e.to)  # Ajoute le sommet voisin à la file pour exploration

# Boucle principale de traitement : gère plusieurs jeux de données, s’arrête quand H vaut -1
while True:
    # Lecture et décomposition des paramètres principaux de l’instance en cours
    H, W, C, M, NW, NC, NM = map(int, input().split())
    if H == -1:
        break  # Si on rencontre H == -1, cela signale la fin des jeux de données

    # Calcul du nombre total de sommets dans le graphe (chaque sous-composant a une plage d’indices dédiée)
    V = H + 2 * (W + C) + M + 5 + 2  # H amis + W*2 (entrée/sortie) + C*2 (entrée/sortie) + M maîtres + 5 supersommets + 2 (source, puits)
    
    # Création d’une nouvelle instance de MaxFlow avec V sommets
    mf = MaxFlow(V)
    source = V - 2  # L'avant-dernier sommet sert de source (point de départ du flot)
    sink = V - 1    # Le dernier sommet sert de puits (destination finale du flot)

    # Définition de fonctions lambda pour obtenir l'indice des différents sous-ensembles de sommets
    inH = lambda i: i  # Les indices 0, ..., H-1 représentent les sommets "amis" (input)
    inW = lambda i: H + i  # Les W "entrée" pour les "wizards" sont juste après les H
    outW = lambda i: H + W + i  # Les W "sortie" pour les wizards suivent
    inC = lambda i: H + 2 * W + i  # Les C "entrée" pour les "cats" après les wizards
    outC = lambda i: H + 2 * W + C + i  # Les C "sortie" pour les cats suivent
    inM = lambda i: H + 2 * (W + C) + i  # Les M maîtres après tous les in/out de wizards et cats
    # Les 5 supersommets "inNW", "outNW", "inNC", "outNC", "inNM" suivent...
    inNW = H + 2 * (W + C) + M
    outNW = inNW + 1
    inNC = outNW + 1
    outNC = inNC + 1
    inNM = outNC + 1

    # Ajout d’arêtes de la source à chaque sommet "ami" (inH)
    for i in range(H):
        mf.add_edge(source, inH(i), 1)  # Capacité 1, chaque ami ne peut être pris qu’une fois

    # Ajout d’arêtes des "amis" vers chaque "wizard" selon les informations fournies (liste d'amis pour chaque wizard)
    for i in range(W):
        friends = [int(x) - 1 for x in input().split()][1:]  # Récupère la liste (convertie à l'indexation 0)
        for friend in friends:  # Pour chaque ami qui connaît ce wizard
            mf.add_edge(inH(friend), inW(i), 1)  # Ajoute une arête de la case de l’ami vers la "entrée" du wizard

    # Ajout d’arêtes de chaque "ami" vers le supersommet "inNW" (No-Wizard)
    for i in range(H):
        mf.add_edge(inH(i), inNW, 1)  # Capacité 1

    # Ajout d'arêtes "entrée wizard -> sortie wizard" de capacité 1
    for i in range(W):
        mf.add_edge(inW(i), outW(i), 1)  # Capacité 1
    # Ajout d'une arête "inNW -> outNW" de capacité NW (No-Wizard)
    mf.add_edge(inNW, outNW, NW)

    # Lecture et ajout des arêtes de "outW" (sortie wizard) et "outNW" (sortie No-Wizard) vers chaque cat (entrée cat)
    for i in range(C):
        friends = [int(x) - 1 for x in input().split()][1:]  # Liste des wizard qui connaissent ce cat
        for friend in friends:
            mf.add_edge(outW(friend), inC(i), 1)  # Wizard sorti -> entrée cat
        mf.add_edge(outNW, inC(i), 1)  # Sortie No-Wizard -> entrée cat

    # Ajout d’arêtes de chaque "outW" vers le supersommet "inNC" (No-Cat)
    for i in range(W):
        mf.add_edge(outW(i), inNC, 1)  # Capacité 1

    # Ajout d'arêtes "entrée cat -> sortie cat" de capacité 1, plus "inNC -> outNC" de capacité NC
    for i in range(C):
        mf.add_edge(inC(i), outC(i), 1)  # Capacité 1
    mf.add_edge(inNC, outNC, NC)  # No-Cat

    # Lecture et ajout des arêtes de "outC" (sortie cat) et "outNC" (sortie No-Cat) vers chaque maître
    for i in range(M):
        friends = [int(x) - 1 for x in input().split()][1:]  # Liste des cats qui connaissent ce maître
        for friend in friends:
            mf.add_edge(outC(friend), inM(i), 1)  # Sortie cat -> maître
        mf.add_edge(outNC, inM(i), 1)  # Sortie No-Cat -> maître

    # Ajout d’arêtes de chaque "outC" (sortie cat) vers le supersommet "inNM" (No-Master)
    for i in range(C):
        mf.add_edge(outC(i), inNM, 1)  # Capacité 1

    # Relie les maîtres (inM) et le supersommet NM au puits, chacun de capacité 1 (NM peut en prendre NM)
    for i in range(M):
        mf.add_edge(inM(i), sink, 1)  # Chaque maître vers le puits
    mf.add_edge(inNM, sink, NM)  # No-Master

    # Exécute l’algorithme de flot maximum et affiche la solution pour ce jeu de données
    print(mf.run(source, sink))