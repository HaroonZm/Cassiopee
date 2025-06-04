from collections import deque  # Importe la classe deque de la bibliothèque collections, utilisée pour une file efficace à deux extrémités

# Définition de la classe Dinic, qui implémente l'algorithme de Dinic pour trouver le flot maximum dans un graphe orienté
class Dinic:
    def __init__(self, v, inf=float('inf')):
        # v contient le nombre de sommets (noeuds) du graphe
        self.V = v  # Nombre total de sommets dans le graphe
        self.inf = inf  # Variable représentant l'infini, utilisée comme capacité maximale
        self.G = [[] for _ in range(self.V)]  # Liste d'adjacence : chaque sommet a une liste pour stocker ses arêtes sortantes
        self.level = [0] * self.V  # Tableau pour stocker le niveau de chaque sommet lors de la BFS. Au début, ils sont tous à 0
        self.iter = [0] * self.V  # Liste pour suivre l'arête actuellement considérée lors de la DFS pour chaque sommet

    # Fonction pour ajouter une arête au graphe
    def add_edge(self, from_v, to_v, cap):
        # from_v : sommet de départ de l'arête
        # to_v : sommet d'arrivée de l'arête
        # cap : capacité maximale de l'arête
        # Ajoute une arête avant dans le graphe (de from_v à to_v)
        self.G[from_v].append({'to': to_v, 'cap': cap, 'rev': len(self.G[to_v])})
        # Ajoute une arête arrière (reverse edge) de to_v à from_v, initialisée à capacité 0
        self.G[to_v].append({'to': from_v, 'cap': 0, 'rev': len(self.G[from_v]) - 1})

    # Fonction qui effectue un parcours en largeur (BFS) pour construire les niveaux (distance depuis la source)
    def bfs(self, s):
        # Initialise tous les niveaux à -1 (non visités)
        self.level = [-1] * self.V
        # Le niveau du sommet source (s) est 0, car il est le plus proche de lui-même
        self.level[s] = 0
        que = deque()  # Crée une nouvelle file deque (double-ended queue) vide
        que.appendleft(s)  # Ajoute le sommet source au début de la file

        # Tant que la file n'est pas vide
        while len(que) > 0:
            v = que.pop()  # Prend et retire le sommet à la fin de la file
            # Parcourt toutes les arêtes sortantes du sommet v
            for i in range(len(self.G[v])):
                e = self.G[v][i]  # e est un dictionnaire représentant l'arête i sortant de v
                # Vérifie si l'arête e a une capacité résiduelle (>0) et si le sommet d'arrivée n'a pas encore été assigné à un niveau
                if e['cap'] > 0 and self.level[e['to']] < 0:
                    self.level[e['to']] = self.level[v] + 1  # Le niveau du sommet d'arrivée est celui de v augmenté de 1
                    que.appendleft(e['to'])  # Ajoute le sommet d'arrivée au début de la file pour le BFS

    # Procédure récursive DFS pour trouver une chaîne augmentante et envoyer du flot
    def dfs(self, v, t, f):
        # v : sommet courant
        # t : sommet terminal (puits)
        # f : la quantité minimale de flot pouvant encore passer dans cette chaîne
        if v == t:  # Si le sommet courant est le puits, retourne tout le flot reçu, fin de la chaîne augmentante
            return f

        # Parcourt toutes les arêtes sortantes non encore explorées depuis v
        for i in range(self.iter[v], len(self.G[v])):
            self.iter[v] = i  # Enregistre la position actuelle de l'itérateur
            e = self.G[v][i]  # e est l'arête actuelle
            # Vérifie si on peut envoyer du flot à travers cette arête (capacité résiduelle positive et respect du niveau)
            if e['cap'] > 0 and self.level[v] < self.level[e['to']]:
                # Cherche récursivement à envoyer du flot par l'arête e
                d = self.dfs(e['to'], t, min(f, e['cap']))  # Ne peut pas envoyer plus que le minimum entre f et la capacité restante de e
                if d > 0:  # Si on a pu envoyer du flot d dans cette branche
                    e['cap'] -= d  # On réduit la capacité résiduelle de e du flot envoyé
                    # On trouve l'arête arrière (reverse edge) correspondante et on augmente sa capacité
                    self.G[e['to']][e['rev']]['cap'] += d
                    return d  # Retourne la quantité du flot effectivement envoyée par cette branche

        return 0  # Si aucun flot n'a pu être envoyé depuis ce sommet, retourne 0

    # Fonction qui calcule le flot maximum entre la source s et le puits t
    def maxflow(self, s, t):
        flow = 0  # Initialise le flot total à 0
        while True:
            self.bfs(s)  # Construit les niveaux avec BFS depuis la source
            if self.level[t] < 0:  # Si le puits n'est pas atteignable, on a fini, retourne le flot
                return flow

            self.iter = [0] * self.V  # Réinitialise les itérateurs DFS pour tous les sommets
            f = self.dfs(s, t, self.inf)  # Cherche à envoyer le plus de flot possible depuis la source jusqu'au puits
            while f > 0:
                flow += f  # Ajoute la quantité de flot envoyée au flot total
                f = self.dfs(s, t, self.inf)  # Cherche à envoyer davantage de flot tant que possible

# Fonction pour lire les entrées de l'utilisateur, attend la taille n et deux listes de couples d'entiers
def read_input():
    n = int(input())  # Lis le nombre d'éléments n

    red = []  # Liste qui contiendra les couples 'rouges'
    for i in range(n):  # Pour chaque élément de 0 à n-1
        a, b = map(int, input().split())  # Lis deux entiers sur la même ligne, séparés par un espace
        red.append((a, b))  # Ajoute le couple lu à la liste red

    blue = []  # Liste qui contiendra les couples 'bleus'
    for i in range(n):  # Recommence n fois pour la liste bleue
        c, d = map(int, input().split())  # Lis deux entiers, les coordonnées du point bleu
        blue.append((c, d))  # Ajoute ce couple à la liste blue

    return n, red, blue  # Retourne le nombre n et les deux listes de couples rouges et bleus

# Fonction principale qui assemble le graphe selon le problème, puis calcule et affiche le flot maximum
def submit():
    n, red, blue = read_input()  # Récupère la taille et les couples colorés
    dinic = Dinic(2*n+2)  # Crée une instance de Dinic adaptée à la taille du graphe (2*n sommets pour les points + source + puits)

    # Ajoute une arête de la source (2*n) à chaque sommet rouge (index de 0 à n-1), capacité 1
    for i in range(n):
        dinic.add_edge(2*n, i, 1)

    # Ajoute une arête de chaque sommet bleu (index de n à 2*n-1) vers le puits (2*n+1), capacité 1
    for i in range(n):
        dinic.add_edge(n+i, 2*n+1, 1)

    # Ajoute une arête entre un sommet rouge (j) et un sommet bleu (n+i) si le couple (rouge) a ses deux coordonnées inférieures à celles du couple (bleu)
    for i, b in enumerate(blue):  # Pour chaque point bleu, i est son index dans blue, b est le couple (x,y)
        for j, r in enumerate(red):  # Pour chaque point rouge
            if r[0] < b[0] and r[1] < b[1]:  # Si à la fois x_rouge < x_bleu et y_rouge < y_bleu
                dinic.add_edge(j, n+i, 1)  # Crée une arête de capacité 1 de rouge à bleu

    # Calcule le flot maximum du sommet source (2*n) vers le puits (2*n+1) et affiche le résultat
    print(dinic.maxflow(2*n, 2*n+1))

# Code à exécuter seulement si ce script est le programme principal (pas importé comme module)
if __name__ == '__main__':
    submit()  # Appelle la fonction principale pour exécuter le programme