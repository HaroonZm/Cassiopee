from collections import deque  # Importe la classe deque du module collections pour créer des files ou piles efficaces

# Définition de la classe csr (Compressed Sparse Row) pour stocker efficacement un graphe dirigé
class csr:
    def __init__(self, N, edges):
        # N : Nombre de sommets dans le graphe (numérotés de 0 à N-1)
        # edges : Liste des arêtes du graphe, chaque arête étant un tuple (source, destination)
        
        # self.start sera un tableau de taille N+1
        # Pour chaque sommet v, les successeurs de v sont stockés dans elist[start[v]:start[v+1]]
        self.start = [0] * (N + 1)  # Initialise la structure start avec des zéros pour tous les sommets et un extra pour la fin
        
        # self.elist va stocker toutes les extrémités des arêtes dans l'ordre compacté
        self.elist = [0] * len(edges)  # Tableau de la même taille que le nombre total d'arêtes
        
        # Première passe : on compte le nombre d'arêtes sortantes pour chaque sommet
        for e in edges:
            # e est un tuple (source, destination)
            self.start[e[0] + 1] += 1  # On incrémente la case suivante pour chaque source
        
        # Deuxième passe : on calcule la somme cumulative pour start
        # Cela fait start[v+1] = index de fin des successeurs de v dans elist
        for i in range(1, N + 1):
            self.start[i] += self.start[i - 1]  # Somme cumulative
        
        # Utilisé pour savoir où insérer dans elist pour chaque sommet
        counter = self.start[:]  # Fait une copie de start
        
        # Troisième passe : on place effectivement les destinations dans elist
        for e in edges:
            self.elist[counter[e[0]]] = e[1]  # Place la destination au bon endroit
            counter[e[0]] += 1  # Avance le compteur pour cette source

# Classe principale pour la détection des composantes fortement connexes
class scc_graph:
    def __init__(self, N):
        # N : nombre de sommets dans le graphe
        self.N = N
        self.edges = []  # Liste pour stocker les arêtes du graphe
        
    def add_edge(self, v, w):
        # Ajoute une arête orientée du sommet v vers le sommet w
        self.edges.append((v, w))

    # Cette méthode calcule les IDs de chaque composante fortement connexe
    def scc_ids(self):
        # Crée une représentation du graphe via la structure csr
        g = csr(self.N, self.edges)
        
        now_ord = 0  # Va contenir l'ordre d'exploration de chaque sommet
        group_num = 0  # Nombre total de composantes trouvées
        visited = deque()  # Va servir de pile pour mémoriser l'ordre des sommets visités
        
        low = [0] * self.N  # Tableau pour stocker la plus petite "order" accessible depuis chaque sommet
        order = [-1] * self.N  # Tableau pour donner à chaque sommet son index d'exploration, -1 si non visité
        ids = [0] * self.N  # Id de composante pour chaque sommet, initialisé à zéro
        parent = [-1] * self.N  # Parent dans l'arbre de parcours DFS, -1 pour la racine

        # Parcours tous les sommets
        for i in range(self.N):
            if order[i] == -1:  # Si le sommet i n'a pas encore été visité
                stack = deque()  # Crée une pile pour le parcours en profondeur (DFS) explicite
                stack.append(i)  # Rajoute le sommet i deux fois pour gérer le moment de retour
                stack.append(i)
                while stack:
                    v = stack.pop()  # Prend le sommet sur le dessus de la pile
                    if order[v] == -1:  # Si ce sommet n'a pas encore été visité
                        low[v] = order[v] = now_ord  # Attribue l'ordre actuel à low[v] et order[v]
                        now_ord += 1  # Incrémente l'ordre pour le prochain sommet
                        visited.append(v)  # Ajoute v à la liste des sommets visités
                        # Explore les voisins accessibles depuis v
                        for i in range(g.start[v], g.start[v + 1]):
                            to = g.elist[i]  # Voisin accessible depuis v
                            if order[to] == -1:  # Si le voisin n'a pas été visité
                                stack.append(to)  # Rajoute le voisin à la pile
                                stack.append(to)  # On le met deux fois pour gérer correctement le point de retour
                                parent[to] = v  # On note que v est le parent de to pour l'arbre DFS
                            else:
                                # Si le voisin a été visité, met à jour low[v] avec order[to] si nécessaire
                                low[v] = min(low[v], order[to])
                    else:
                        # Une fois qu'on revient à v dans la pile ("post-traitement" d'un sommet, après tous ses voisins)
                        if low[v] == order[v]:  # Si low[v] == order[v], v est la racine d'une composante fortement connexe
                            while True:
                                u = visited.pop()  # On dépile les sommets de la composante
                                order[u] = self.N  # Marque u comme terminé et retire son numéro d'ordre pour éviter d'être pris à nouveau
                                ids[u] = group_num  # Affecte à u l'identifiant de la composante courante
                                if u == v:
                                    break  # On s'arrête une fois toute la composante extraite
                            group_num += 1  # Passe à la composante suivante
                        # Mise à jour de low du parent pour propager l'information de la composante
                        if parent[v] != -1:  # Si v n'est pas la racine du DFS
                            low[parent[v]] = min(low[parent[v]], low[v])
        # On inverse l'ordre des composantes pour que le 0 soit pour la "première" dans le sens topologique
        for i, x in enumerate(ids):
            ids[i] = group_num - 1 - x  # On fait l'inversion pour correspondre à une numérotation topologique croissante

        return group_num, ids  # Retourne le nombre de composantes et l'id de composante pour chaque sommet

    # Regroupe les sommets par composante fortement connexe
    def scc(self):
        group_num, ids = self.scc_ids()  # Récupère le nombre de composantes et le mapping sommet -> composante
        groups = [[] for _ in range(group_num)]  # Crée une liste de listes pour contenir, pour chaque composante, les sommets
        for i, x in enumerate(ids):
            groups[x].append(i)  # Ajoute le sommet i à la composante appropriée selon son id
        return groups  # Retourne la liste des groupes (une liste par composante)

import sys  # On importe sys pour accéder à la lecture rapide depuis l'entrée standard

# Définition de fonctions pour lire les entrées
readline = sys.stdin.buffer.readline  # Permet de lire une ligne complète (et rapide) depuis l'entrée standard (sous forme de bytes)
read = sys.stdin.buffer.read  # Permet de lire tout ce qui reste sur l'entrée standard (rapide pour de gros blocs)

# Lecture des deux premiers entiers définissant le nombre de sommets (N) et d'arêtes (M)
N, M = map(int, readline().split())  # Utilise map pour convertir chaque partie en int après découpage sur les espaces

# Lecture des 2*M entiers décrivant chaque arête (a1, b1, a2, b2, ...)
ab = list(map(int, read().split()))  # Lit tous les entiers restants, les découpe et les convertit en int, puis les place dans une liste

sg = scc_graph(N)  # Crée l'objet de graphe pour la détection de composantes fortement connexes

# Utilise un itérateur pour consommer les entiers par paires et ajouter chaque arête au graphe
it = iter(ab)  # Crée un itérateur sur la liste ab
for a, b in zip(it, it):  # zip(it, it) permet de prendre chaque paire consécutive d'entiers (a,b)
    sg.add_edge(a, b)  # Ajoute une arête de a vers b

scc = sg.scc()  # Calcule les composantes fortement connexes

print(len(scc))  # Affiche le nombre de composantes fortement connexes trouvées

# Pour chaque groupe, affiche le nombre de sommets dans la composante puis la liste des sommets de cette composante
for group in scc:
    # * permet de "dépaqueter" list pour que chaque élément soit envoyé comme argument séparé à print
    print(*([len(group)] + group))  # Par exemple, pour un groupe [2, 5], affichera "2 2 5"