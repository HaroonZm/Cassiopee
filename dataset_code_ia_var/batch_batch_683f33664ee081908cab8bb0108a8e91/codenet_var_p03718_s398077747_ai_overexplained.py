from collections import deque  # Importation de la classe deque depuis le module collections pour des files efficaces en O(1)

INF = 1 << 23  # Définition d'une très grande valeur constante, ici 2^23, souvent utilisée pour représenter l'infini dans les algorithmes de graphes.

class Dinic:
    # Cette classe implémente l'algorithme de Dinic pour calculer le flot maximal dans un graphe orienté.

    def __init__(self, N):
        # Constructeur de la classe, appelé lors de la création d'une instance Dinic.
        # N : nombre total de nœuds dans le graphe.
        self.N = N  # On stocke le nombre de nœuds pour l'utiliser dans les autres méthodes.
        # self.G est une liste d'adjacence qui servira à représenter le graphe sous forme de listes de listes.
        # Chaque indice représente un nœud, et pour chaque nœud, on stocke une liste de ses arêtes sortantes.
        self.G = [[] for _ in range(self.N)]

    def add_edge(self, u, v, cap):
        # Cette méthode ajoute une arête orientée de u vers v de capacité cap au graphe, ainsi que l'arête d'opposée résiduelle nécessaire à l'algorithme.
        # u : le nœud de départ de l'arête.
        # v : le nœud d'arrivée.
        # cap : la capacité de l'arête.
        # On stocke pour chaque arête une liste contenant :
        # - l'indice du nœud d'arrivée,
        # - la capacité restante sur cette arête,
        # - l'indice (dans la liste d'adjacence de v) de l'arête opposée (nécessaire pour les mises à jour).
        # Ajout de l'arête directe.
        self.G[u].append([v, cap, len(self.G[v])])
        # Ajout de l'arête résiduelle opposée avec capacité 0.
        self.G[v].append([u, 0, len(self.G[u])-1])

    def bfs(self, s):
        # Cette méthode effectue un parcours en largeur (BFS) à partir du sommet source s, pour attribuer un niveau à chaque nœud.
        # Le niveau permet de s'assurer que l'algorithme recherche uniquement des chemins augmentants valides dans le graphe de niveau.
        self.level = [-1] * self.N  # Initialiser tous les niveaux à -1 (non visités)
        que = deque([s])  # Initialiser la file avec le sommet source s.
        self.level[s] = 0  # Le niveau du sommet source vaut 0.
        while que:  # Tant que la file n'est pas vide.
            u = que.popleft()  # Prendre le sommet au début de la file.
            for (v, cap, _) in self.G[u]:  # Pour chaque arête sortante de u.
                # Si la capacité de l'arête est strictement positive ET si le nœud d'arrivée n'a pas encore été atteint.
                if cap > 0 and self.level[v] < 0:
                    self.level[v] = self.level[u] + 1  # On donne un niveau au nœud d'arrivée.
                    que.append(v)  # On l'ajoute à la file pour explorer également ses voisins.

    def dfs(self, u, t, f):
        # Cette méthode effectue une descente récursive en profondeur (DFS) pour chercher un chemin augmentant de capacité positive du sommet u à t.
        # Elle retourne le flot supplémentaire trouvé depuis u vers t (peut être nul si aucun chemin n'est disponible).
        # u : nœud courant
        # t : nœud terminal (puits)
        # f : flot disponible pour ce parcours (contrainte de capacité minimale sur le chemin déjà suivi)
        if u == t:
            # Si on a atteint le puits, on retourne le flot (qui sera la capacité minimale le long du chemin suivi)
            return f
        # On essaye d'avancer sur le graphe à partir du dernier arc exploré pour éviter de refaire inutilement le même travail.
        for i in range(self.progress[u], len(self.G[u])):
            self.progress[u] = i  # On sauvegarde l'indice du dernier arc essayé.
            (v, cap, rev) = self.G[u][i]  # On récupère les informations de l'arête : noeud d'arrivée, capacité, indice de l'arête opposée.
            # On veut uniquement explorer les arêtes ayant une capacité résiduelle positive et où le niveau du voisin est strictement supérieur (proche du sink).
            if cap > 0 and self.level[u] < self.level[v]:
                # On cherche à augmenter le flot sur ce chemin, la quantité étant bornée par la capacité disponible ou celle déjà consommée.
                d = self.dfs(v, t, min(f, cap))
                if d > 0:
                    # Si un flot positif a pu être envoyé jusqu'au puits via ce chemin...
                    self.G[u][i][1] -= d  # On met à jour la capacité de l'arête utilisée en la diminuant du flot trouvé.
                    self.G[v][rev][1] += d  # On augmente la capacité sur l'arête opposée (pour permettre un éventuel flot de retour).
                    return d  # On retourne la quantité de flot effectivement envoyée.
        return 0  # Aucun flot supplémentaire n'a pu être envoyé depuis u.

    def max_flow(self, s, t):
        # Cette méthode principale lance la recherche du flot maximal entre le sommet source s et le puits t.
        flow = 0  # On initialise la valeur totale du flot trouvé à zéro.
        INF = 10**9  # On fixe une valeur (très) grande pour la capacité maximale possible lors des recherches DFS.
        while True:
            # D'abord, on construit le graphe de niveau via BFS.
            self.bfs(s)
            # Si le puits n'est pas atteignable depuis la source (niveau négatif), il n'existe plus de chemins augmentants.
            if self.level[t] < 0:
                return flow  # On peut retourner la valeur du flot maximal trouvée.
            # On initialise un tableau pour suivre l'état de la recherche DFS sur chaque nœud.
            self.progress = [0] * self.N
            current_flow = self.dfs(s, t, INF)  # On essaie d'augmenter le flot sur un chemin jusqu'à saturation.
            while current_flow > 0:  # Tant qu'on peut encore pousser du flot depuis s jusqu'à t,
                flow += current_flow  # On augmente la valeur totale du flot.
                current_flow = self.dfs(s, t, INF)  # On recherche à nouveau un chemin non saturé.

def main():
    # Fonction principale du programme.
    # Elle lit les données d'entrée, construit le graphe selon la description, puis calcule et affiche le flot maximal.

    # Lecture des tailles de la grille rectangulaire (H pour le nombre de lignes, W pour le nombre de colonnes).
    H, W = (int(i) for i in input().split())
    # Lecture du tableau de caractères représentant le terrain/grille.
    A = [input() for i in range(H)]

    # Création d'une instance de l'algorithme de Dinic.
    # Le nombre total de sommets est H+W+2 :
    # - H sommets pour les lignes (représentés de W à W+H-1)
    # - W sommets pour les colonnes (représentés de 0 à W-1)
    # - 1 sommet 's' pour la source (indice H+W)
    # - 1 sommet 't' pour le puits (indice H+W+1)
    F = Dinic(H+W+2)
    s = H+W      # indice du sommet source
    t = H+W+1    # indice du sommet puits

    Sh, Sw = -1, -1  # Variables pour stocker la position de 'S' dans la grille
    Th, Tw = -1, -1  # Variables pour stocker la position de 'T'

    # Parcours de chaque case du tableau de caractères.
    for h in range(H):
        for w in range(W):
            # Si la case contient la source 'S'
            if A[h][w] == "S":
                Sh, Sw = h, w  # On retient les coordonnées de 'S'
                # On relie la source 's' au sommet représentant la ligne (h+W) et la colonne (w)
                F.add_edge(s, h+W, INF)  # l'infini car la source peut utiliser n'importe quelle ligne/colonne
                F.add_edge(s, w, INF)
            # Si la case contient le puits 'T'
            elif A[h][w] == "T":
                Th, Tw = h, w  # On retient les coordonnées de 'T'
                # On relie la ligne (h+W) et la colonne (w) au sommet puits 't'
                F.add_edge(h+W, t, INF)
                F.add_edge(w, t, INF)
            # Pour chaque case qui n'est pas vide (pas ".")
            if A[h][w] != ".":
                # On relie le sommet de la ligne (h+W) au sommet de la colonne (w) avec capacité 1
                # ainsi que l'arête opposée, pour autoriser le déplacement dans les deux directions entre case et colonne/ligne
                F.add_edge(h+W, w, 1)
                F.add_edge(w, h+W, 1)

    # Si la source et le puits sont sur la même ligne ou la même colonne, il n'existe aucun chemin valide (sinon l'infini circule).
    if Sh == Th or Sw == Tw:
        return print(-1)  # On affiche -1 pour signifier l'impossibilité du flot.

    # Sinon, on calcule et affiche le flot maximal entre 's' et 't'.
    print(F.max_flow(s, t))


if __name__ == '__main__':
    # Ce bloc permet d'exécuter la fonction main uniquement si ce script est l'entrée principale du programme, 
    # et pas lorsqu'il est importé comme module dans un autre script.
    main()