import sys
from collections import deque

# Lecture efficace depuis l'entrée et écriture dans la sortie
readline = sys.stdin.readline
write = sys.stdout.write

class Dinic:
    """
    Implémentation de l'algorithme de Dinic pour le calcul du flot maximum dans un graphe orienté.

    Attributs
    ---------
    N : int
        Nombre de sommets du graphe.
    G : List[List[list]]
        Liste d'adjacence représentant le graphe. Chaque arc est une liste de forme [to, cap, rev].
    D : dict
        Dictionnaire facilitant l'accès rapide aux arcs [from, to].
    """

    def __init__(self, N):
        """
        Initialise la structure pour un graphe ayant N sommets (de 0 à N-1).

        Paramètres
        ----------
        N : int
            Nombre de sommets du graphe.
        """
        self.N = N
        self.G = [[] for _ in range(N)]  # Liste d'adjacence
        self.D = {}                      # Pour retrouver rapidement un arc donné

    def add_edge(self, fr, to, cap):
        """
        Ajoute un arc orienté de 'fr' vers 'to' avec une capacité 'cap' au graphe.

        Paramètres
        ----------
        fr : int
            Identifiant du sommet de départ (0-indexé).
        to : int
            Identifiant du sommet d'arrivée (0-indexé).
        cap : int
            Capacité de l'arc.
        """
        forward = [to, cap, None]          # Arc direct
        forward[2] = backward = [fr, 0, forward]  # Arc inverse lié au direct (capacité nulle)
        self.G[fr].append(forward)
        self.G[to].append(backward)
        self.D[fr, to] = forward           # Pour accès rapide à l'arc (facultatif)

    def bfs(self, s, t):
        """
        Réalise un BFS à partir du sommet source 's' jusqu'au puits 't',
        et calcule les niveaux de chaque sommet atteignable depuis 's' via des arcs possédant du flot restant.

        Paramètres
        ----------
        s : int
            Indice du sommet source.
        t : int
            Indice du sommet puits.

        Retourne
        -------
        bool
            True si le puits 't' est atteignable depuis 's', False sinon.
        """
        self.level = level = [None] * self.N
        deq = deque([s])
        level[s] = 0
        G = self.G
        while deq:
            v = deq.popleft()
            lv = level[v] + 1
            for w, cap, _ in G[v]:
                if cap and level[w] is None:
                    level[w] = lv
                    deq.append(w)
        return level[t] is not None

    def dfs(self, v, t, f):
        """
        Recherche un chemin augmentant du sommet 'v' vers le puits 't', 
        dont le flot maximum transférable ne dépasse pas 'f'.

        Paramètres
        ----------
        v : int
            Sommet courant lors de la recherche DFS.
        t : int
            Indice du sommet puits.
        f : int
            Flot maximum transférable pour ce chemin.

        Retourne
        -------
        int
            Quantité de flot effectivement envoyée à travers ce chemin.
        """
        if v == t:
            return f
        level = self.level
        for e in self.it[v]:
            w, cap, rev = e
            if cap and level[v] < level[w]:
                d = self.dfs(w, t, min(f, cap))
                if d:
                    e[1] -= d
                    rev[1] += d
                    return d
        return 0

    def flow(self, s, t):
        """
        Calcule le flot maximum entre le sommet source 's' et le puits 't' du graphe courant, 
        via l'algorithme de Dinic.

        Paramètres
        ----------
        s : int
            Indice du sommet source.
        t : int
            Indice du sommet puits.

        Retourne
        -------
        int
            Valeur du flot maximum trouvé du graphe de 's' à 't'.
        """
        flow = 0
        INF = 10**9 + 7  # Flot très grand, supérieur à tout flot possible dans l'instance
        G = self.G
        while self.bfs(s, t):  # Tant qu'il existe un chemin augmentant
            *self.it, = map(iter, self.G)  # Réinitialise les itérateurs pour chaque sommet
            f = INF
            while f:
                f = self.dfs(s, t, INF)
                flow += f
        return flow

def solve():
    """
    Traite un jeu d'entrée standard pour trouver le flot maximum
    et le nombre d'arêtes qui doivent être augmentées afin d'augmenter le flot.
    Écrit la solution au format demandé dans la sortie standard.

    Lecture format : 
    - Première ligne : N M S T (N sommets, M arêtes, source S, puits T)
    - Suivent M lignes : a b (arêtes orientées de a vers b, 1-indexées)

    Retourne
    -------
    bool
        True si le problème traité n'est pas terminé (permet la boucle principale), 
        False pour terminer la résolution.
    """
    N, M, S, T = map(int, readline().split())
    if N == M == 0:  # Cas d'arrêt de la boucle principale
        return False

    # Conversion en indices 0-based pour l'implémentation
    S -= 1  
    T -= 1
    E = []            # Liste des arêtes lues
    INF = 10**9       # Grande valeur pour le flot, pour modéliser l'infini
    dinic = Dinic(N)  # Initialisation de l'instance de Dinic

    # Lecture des arêtes et construction du graphe
    for i in range(M):
        a, b = map(int, readline().split())
        a -= 1
        b -= 1
        dinic.add_edge(a, b, 1)  # Capacité unité (peut être adapté selon le contexte)
        E.append((a, b))

    f = dinic.flow(S, T)        # Calcul du flot maximum

    # Préparation pour l'analyse des coupes minimales
    used = [0]*N                # Statut des sommets : 0=non visité, 1=atteignable depuis S, 2=atteignable depuis T via résiduel
    que = deque([S])
    used[S] = 1

    # Marquage des sommets atteignables depuis S via arcs résiduels (capacité > 0)
    while que:
        v = que.popleft()
        for w, cap, _ in dinic.G[v]:
            if cap == 0 or used[w]:
                continue
            used[w] = 1
            que.append(w)

    # Marquage des sommets atteignables depuis T par les arcs saturés (capacité == 0 dans le sens originel)
    que = deque([T])
    used[T] = 2
    while que:
        v = que.popleft()
        for w, cap, _ in dinic.G[v]:
            if cap > 0 or used[w]:
                continue
            used[w] = 2
            que.append(w)

    # Décompte des arêtes de la coupe qui permettraient d'augmenter le flot
    cnt = 0
    for a, b in E:
        if used[a] == 2 and used[b] == 1:
            cnt += 1

    # Affichage du résultat selon la présence d'arêtes permettant d'augmenter le flot
    if cnt:
        write("%d %d\n" % (f+1, cnt))
    else:
        write("%d %d\n" % (f, 0))

    return True

# Boucle principale : traite chaque jeu de données jusqu'à la condition d'arrêt
while solve():
    ...