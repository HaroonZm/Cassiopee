import collections  # Importation du module collections, qui contient des structures de données avancées, comme deque
import sys  # Importation du module sys, qui fournit diverses fonctions et variables liées à l'environnement Python

# Compatibilité Python 2 : si la version majeure de Python (indice 0) est '2'
if sys.version[0] == '2':
    # Dans Python 2, 'xrange' est l'équivalent de 'range' en Python 3 et 'raw_input' correspond à 'input'
    range, input = xrange, raw_input

# Définition d'une classe MaxFlow pour représenter le calcul de flot maximal dans un graphe (problème "max-flow")
class MaxFlow:
    """Implémentation de l'algorithme de Dinic pour trouver le flot maximal d'un graphe orienté.
       Complexité temporelle : O(E * V^2), avec E le nombre d'arêtes et V le nombre de sommets.
    """
    # Définition d'une classe interne Edge pour représenter une arête du graphe
    class Edge:
        # Constructeur de la classe Edge
        def __init__(self, to, cap, rev):
            # 'to' : identifiant du sommet d'arrivée de l'arête
            # 'cap' : capacité résiduelle de l'arête
            # 'rev' : indice de l'arête inverse dans la liste d'adjacence du sommet d'arrivée
            self.to, self.cap, self.rev = to, cap, rev

    # Constructeur de la classe MaxFlow, qui prend en paramètre le nombre total de sommets V
    def __init__(self, V):
        # 'V' : nombre de sommets dans le graphe
        self.V = V
        # 'E' : liste d'adjacence représentant, pour chaque sommet (indice de 0 à V-1), la liste de ses arêtes sortantes
        self.E = [[] for _ in range(V)]

    # Méthode pour ajouter une arête dirigée du sommet 'fr' au sommet 'to', avec une certaine capacité 'cap'
    def add_edge(self, fr, to, cap):
        # Ajoute l'arête principale, de 'fr' à 'to', avec capacité 'cap', et retient l'indice de la prochaine arête dans la liste 'to'
        self.E[fr].append(self.Edge(to, cap, len(self.E[to])))
        # Ajoute l'arête inverse (rétro-arête), de 'to' à 'fr', avec capacité nulle (0), et retient la position de l'arête précédente dans 'fr'
        self.E[to].append(self.Edge(fr, 0, len(self.E[fr])-1))

    # Fonction principale pour calculer le flot maximal entre un sommet source et un sommet puits
    def run(self, source, sink, INF=10**9):
        """Exécution de l'algorithme de Dinic pour trouver le flot maximal entre 'source' et 'sink'"""
        maxflow = 0  # Variable pour stocker le flot maximum trouvé
        # Boucle principale : répète les étapes tant qu'il existe un chemin du source au puits dans le graphe résiduel
        while True:
            self.bfs(source)  # Calcul des niveaux des sommets par BFS (exploration en largeur)
            # Si le niveau du puits est négatif, il n'est pas accessible : on a terminé
            if self.level[sink] < 0:
                return maxflow  # Retourne la valeur finale du flot maximal
            # 'itr' stocke, pour chaque sommet, le prochain indice d'arête à tester lors du DFS (évite de tout reparcourir à chaque fois)
            self.itr = [0] * self.V
            while True:
                flow = self.dfs(source, sink, INF)
                if flow > 0:
                    maxflow += flow
                else:
                    break  # Si aucun flot supplémentaire n'a pu être trouvé, on passe à la prochaine exploration par BFS

    # Méthode DFS (exploration en profondeur), cherche un chemin d'augmentation du flot depuis un sommet donné
    def dfs(self, vertex, sink, flow):
        """Cherche un chemin d'augmentation depuis 'vertex' vers 'sink', pouvant encore supporter du flot 'flow'"""
        if vertex == sink:  # Si on arrive au puits, on retourne le flot qu'on peut envoyer (le minimum précédemment trouvé)
            return flow
        # On explore toutes les arêtes sortantes restantes depuis ce sommet
        for i in range(self.itr[vertex], len(self.E[vertex])):
            self.itr[vertex] = i  # On mémorise l'indice à partir duquel commencer la prochaine fois
            e = self.E[vertex][i]  # Récupère l'arête i depuis le sommet 'vertex'
            # On vérifie si l'arête a une capacité positive, et si le niveau du sommet arrivé est strictement supérieur
            if e.cap > 0 and self.level[vertex] < self.level[e.to]:
                # On tente d'envoyer le flot minimum (entre la capacité résiduelle et le flot restant à envoyer)
                d = self.dfs(e.to, sink, min(flow, e.cap))
                # Si un flot non nul a pu être envoyé
                if d > 0:
                    # On diminue la capacité résiduelle de l'arête suivie
                    e.cap -= d
                    # On augmente la capacité de l'arête inverse (rétro-arête) pour rendre possible un retour de flot ultérieur
                    self.E[e.to][e.rev].cap += d
                    # On renvoie la quantité de flot effectivement envoyée
                    return d
        # Si aucun chemin ou flot n'a été trouvé, retourne 0
        return 0

    # Méthode BFS (exploration en largeur), calcule le niveau de chaque sommet à partir de 'start'
    def bfs(self, start):
        """Calcule la distance minimale (en nombre d'arêtes) de chaque sommet depuis 'start' dans le graphe résiduel"""
        que = collections.deque()  # On utilise une deque pour implémenter la file de la BFS
        self.level = [-1] * self.V  # On initialise tous les niveaux à -1 (donc non visités)
        que.append(start)  # On commence à explorer le sommet de départ
        self.level[start] = 0  # Le niveau du sommet de départ est 0

        while que:
            fr = que.popleft()  # On retire le premier sommet de la file pour l'explorer
            for e in self.E[fr]:  # On parcourt toutes les arêtes sortantes
                # Si l'arête a une capacité positive et que le sommet d'arrivée n'a pas encore été visité
                if e.cap > 0 and self.level[e.to] < 0:
                    # On définit le niveau du sommet d'arrivée comme le niveau du sommet courant + 1
                    self.level[e.to] = self.level[fr] + 1
                    que.append(e.to)  # On ajoute le sommet d'arrivée dans la file pour l'explorer ensuite

# Boucle principale, lit et traite les jeux de données jusqu'à la condition de terminaison
while True:
    # Récupération des sept entiers donnés sur une ligne d'entrée utilisateur
    H, W, C, M, NW, NC, NM = map(int, input().split())
    # Si le nombre d'humains H vaut -1, on arrête la boucle (condition de terminaison)
    if H == -1:
        break
    # Calcule le nombre total de sommets (V) utilisés dans le graphe, selon la construction prévue
    V = H + 2 * (W + C) + M + 5 + 2
    # Instancie un objet MaxFlow avec V sommets
    mf = MaxFlow(V)
    # Détermine les indices des sommets source et puits (sink) dans la numérotation globale
    source, sink = V - 2, V - 1

    # Définition de fonctions anonymes (lambda) retournant l'indice correspondant à chaque type de nœud dans la numérotation globale des sommets
    inH = lambda i: i  # Sommet humain numéro i (entrée)
    inW = lambda i: H + i  # Sommet métier W numéro i (entrée)
    outW = lambda i: H + W + i  # Sommet métier W numéro i (sortie)
    inC = lambda i: H + 2 * W + i  # Sommet club C numéro i (entrée)
    outC = lambda i: H + 2 * W + C + i  # Sommet club C numéro i (sortie)
    inM = lambda i: H + 2 * (W + C) + i  # Sommet M numéro i (entrée)
    # Les nœuds spéciaux NW, NC, NM sont placés à la suite des autres (voir la construction des indices ci-dessous)
    inNW = H + 2 * (W + C) + M
    outNW = inNW + 1
    inNC = outNW + 1
    outNC = inNC + 1
    inNM = outNC + 1

    # Création des arcs ('edges') dans le graphe du flot (représentant les contraintes du problème)

    # 1. Liaison du sommet source à tous les humains
    for i in range(H):
        mf.add_edge(source, inH(i), 1)  # Capacité de 1 pour chaque humain (car au plus une affectation/joueur)

    # 2. Liaison des humains aux métiers (inW)
    for i in range(W):
        # Lecture d'une ligne contenant la liste des copains habilités pour ce métier W
        friends = [int(x) - 1 for x in input().split()][1:]  # On ignore le premier nombre (le nombre de copains)
        for friend in friends:
            mf.add_edge(inH(friend), inW(i), 1)  # Chaque humain éligible à ce métier W reçoit une arête de capacité 1

    # 3. Chaque humain doit pouvoir se connecter au "super-nœud" NW (inNW), qui gère une contrainte de cardinalité sur le nombre d'humains restants
    for i in range(H):
        mf.add_edge(inH(i), inNW, 1)  # Capacité de 1

    # 4. Ajout des arcs pour relier chaque sommet métier (inW) à sa sortie (outW) et le super-nœud inNW à sa sortie outNW
    for i in range(W):
        mf.add_edge(inW(i), outW(i), 1)  # Capacité de 1 pour chaque métier
    mf.add_edge(inNW, outNW, NW)  # Capacité maximale NW, limite le nombre de personnes passant par NW

    # 5. Pour chaque club, crée les arcs nécessaires depuis les métiers (W) sortants et outNW, vers le club
    for i in range(C):
        friends = [int(x) - 1 for x in input().split()][1:]  # Liste des métiers amis pour ce club
        for friend in friends:
            mf.add_edge(outW(friend), inC(i), 1)  # Pour chaque métier ami, flèche sortante vers ce club
        mf.add_edge(outNW, inC(i), 1)  # Le "super-nœud" NW relie aussi à chaque club

    # 6. Chaque métier sortant se connecte aussi au "super-nœud" NC (inNC)
    for i in range(W):
        mf.add_edge(outW(i), inNC, 1)  # Capacité 1

    # 7. Pour chaque club, relie l'entrée du club à sa sortie, puis relie le super-nœud NC à sa sortie
    for i in range(C):
        mf.add_edge(inC(i), outC(i), 1)  # Capacité 1 pour traverser chaque club
    mf.add_edge(inNC, outNC, NC)  # Contrainte cardinalité : au plus NC personnes via ce nœud

    # 8. Chaque club sortant outC connecte à M (inM), et le super-nœud outNC aussi
    for i in range(M):
        friends = [int(x) - 1 for x in input().split()][1:]  # Liste des clubs amis pour ce poste M
        for friend in friends:
            mf.add_edge(outC(friend), inM(i), 1)  # Arêtes de capacité 1 des clubs sortants vers chaque poste M
        mf.add_edge(outNC, inM(i), 1)  # Super-nœud outNC vers chaque poste M

    # 9. Chaque club sortant se relie aussi au "super-nœud" NM (inNM)
    for i in range(C):
        mf.add_edge(outC(i), inNM, 1)  # Capacité 1

    # 10. Chaque M se relie au puits (sink), le nœud spécial NM aussi
    for i in range(M):
        mf.add_edge(inM(i), sink, 1)  # Chaque poste M ne peut être attribué qu'une fois
    mf.add_edge(inNM, sink, NM)  # Super-nœud NM, cardinalité NM

    # Calcul le flot maximal du graphe construit et l'affiche
    print(mf.run(source, sink))  # Affichage du résultat final pour ce jeu de données