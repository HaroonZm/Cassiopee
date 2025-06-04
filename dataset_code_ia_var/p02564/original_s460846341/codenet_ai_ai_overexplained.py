# Définition de la classe CSR, qui représente une structure de données optimisée pour le stockage et l'accès aux graphes orientés en mémoire.
class CSR:
    # Le constructeur de la classe (appelé lors de l'instanciation d'un objet).
    # n : nombre de sommets dans le graphe.
    # edges : liste des arêtes (chaque arête est une paire [départ, arrivée]).
    def __init__(self, n: int, edges: list):
        # self.start est utilisé pour indexer rapidement la position de chaque sommet dans elist.
        # Elle fait n+1 cases pour que l'accès au "dernier sommet + 1" soit possible.
        # Au début, on initialise start avec 0 sur toutes les cases.
        self.start = [0] * (n + 1)  # Exemple : si n=3, alors start = [0, 0, 0, 0]
        # self.elist va contenir tous les sommets d'arrivée de toutes les arêtes, "concatenés".
        # Elle fait autant de cases qu'il y a d'arêtes.
        self.elist = [0] * len(edges)
        # Boucle sur chaque arête du graphe.
        for e in edges:
            # Pour chaque arête, on incrémente la case correspondante au sommet de départ + 1.
            # Cela sert à compter combien d'arêtes partent d'un sommet.
            self.start[e[0] + 1] += 1
        # On cumule les valeurs pour obtenir où commence la liste d'arêtes de chaque sommet dans elist.
        for i in range(1, n + 1):
            # On ajoute à la case i la valeur cumulée jusque i-1.
            self.start[i] += self.start[i - 1]
        # On prend une copie de start pour servir de compteur lors du remplissage de elist.
        counter = self.start[::]  # Cette copie sert à ne pas modifier le start original.
        # Boucle sur toutes les arêtes.
        for e in edges:
            # On place le sommet d'arrivée de chaque arête à la bonne position dans elist.
            # counter[e[0]] donne l'index où on doit placer la prochaine arête partant de e[0].
            self.elist[counter[e[0]]] = e[1]
            # On incrémente le compteur pour ce sommet, pour que la prochaine arête soit placée à la suite.
            counter[e[0]] += 1

# Définition de la classe SccGraph, qui permet de construire un graphe orienté
# puis de calculer ses composantes fortement connexes (SCC).
class SccGraph:
    # Constructeur de la classe, avec un paramètre optionnel n initialisé à 0 par défaut.
    def __init__(self, n: int = 0):
        # __n contient le nombre de sommets dans le graphe.
        self.__n = n
        # __edges est la liste des arêtes (liste de [s, t]).
        self.__edges = []
    # Fonction spéciale pour permettre d'utiliser len(sg).
    def __len__(self):
        # Retourne le nombre de sommets dans le graphe.
        return self.__n
    # Fonction pour ajouter une arête dirigée de s vers t au graphe.
    def add_edge(self, s: int, t: int):
        # Assertion : vérifie que s et t sont bien valides (dans l'intervalle [0, __n)).
        assert 0 <= s < self.__n and 0 <= t < self.__n
        # Ajout de l'arête à la liste interne __edges.
        self.__edges.append([s, t])
    # Fonction privée pour déterminer les composantes fortement connexes (SCC).
    # Elle retourne (nombre de groupes, tableau des identifiants de groupe de chaque sommet).
    def __scc_ids(self):
        # On construit la structure CSR optimisée pour notre graphe, à partir des arêtes.
        g = CSR(self.__n, self.__edges)
        # now_ord sert à donner un ordre/check de visite unique à chaque sommet.
        now_ord = group_num = 0  # Initialisation de deux compteurs à zéro.
        # visited est une pile qui gardera trace des sommets visités, pour pouvoir reconstruire les SCC à la remontée.
        visited = []
        # low[v] est la plus petite order accessible depuis v (chemin arrière, notion essentielle de Tarjan).
        low = [0] * self.__n
        # order[v] est l'indice d'ordre auquel v a été visité (par DFS). -1 signifie non visité.
        order = [-1] * self.__n
        # ids[v] sera l'identifiant du groupe de SCC auquel appartient le sommet v.
        ids = [0] * self.__n
        # parent[v] sera le parent de v dans la pile d'exploration.
        parent = [-1] * self.__n
        # On lance la recherche de SCC pour chaque sommet qui n'a pas encore d'ordre (cad pas encore visité).
        for root in range(self.__n):
            if order[root] == -1:  # Si racine non visitée,
                stack = [root, root]  # On commence avec la racine dans la pile, deux fois (astuce pour gérer la sortie/rentrée).
                while stack:
                    v = stack.pop()  # On dépile le prochain sommet à traiter.
                    if order[v] == -1:
                        # Si le sommet v n'a jamais été visité :
                        visited.append(v)  # On l'ajoute à la pile des visités.
                        low[v] = order[v] = now_ord  # On lui associe le numéro d'ordre.
                        now_ord += 1  # On prépare le numéro d'ordre suivant.
                        # Parcours des voisins directs de v, c'est à dire tous les sommets t tels qu'il existe une arête v->t.
                        for i in range(g.start[v], g.start[v + 1]):
                            t = g.elist[i]  # t est un voisin direct de v.
                            if order[t] == -1:
                                # Si t n'a pas été visité, on l'empile deux fois (voir plus bas pourquoi).
                                stack += [t, t]
                                parent[t] = v  # v est parent de t dans le parcours DFS.
                            else:
                                # Si t a déjà un ordre --> t fait partie d'une remontée du DFS, donc on met à jour low[v].
                                low[v] = min(low[v], order[t])
                    else:
                        # Si on revisite v (seconde apparition dans la pile) :
                        if low[v] == order[v]:
                            # Si personne de plus petit que v n'est accessible dans son arbre DFS (cas racine d'une SCC).
                            while True:
                                # On vide la pile visited jusqu'à retrouver v.
                                u = visited.pop()
                                order[u] = self.__n  # On met un gros ordre pour éviter de le resélectionner.
                                ids[u] = group_num  # On associe le numéro de composante courant à u.
                                if u == v:
                                    break  # On a trouvé le dernier sommet de la SCC courante, on quitte la boucle.
                            group_num += 1  # On passe à la SCC suivante.
                        # Mise à jour du low du parent : le parent remonte la plus petite low de ses enfants.
                        if parent[v] != -1:
                            low[parent[v]] = min(low[parent[v]], low[v])
        # Après tout le traitement, on inverse les numéros de SCC pour avoir un ordre topologique croissant.
        # Plus précisément, on soustrait group_num-1 à chaque id, ce qui inverse le classement.
        for i, x in enumerate(ids):
            ids[i] = group_num - 1 - x
        # On renvoie enfin le nombre total de composantes et la liste des identifiants pour chaque sommet.
        return group_num, ids
    # Fonction publique permettant d'obtenir la liste des composantes fortement connexes.
    # Chaque groupe est une liste de sommets.
    def scc(self):
        # On récupère (nombre de groupes, affectation sommet -> groupe).
        group_num, ids = self.__scc_ids()
        # On compte combien de sommets sont dans chaque groupe/composante.
        counts = [0] * group_num
        for x in ids:
            counts[x] += 1
        # On initialise une liste de listes vides pour stocker chaque composante.
        groups = [[] for _ in range(group_num)]
        # Pour chaque sommet i, en fonction de l'identifiant de son groupe x, on l'ajoute à ce groupe.
        for i, x in enumerate(ids):
            groups[x].append(i)
        # On renvoie la liste des groupes (chacun étant une liste de sommets).
        return groups

# Partie interface utilisateur : lecture des données et exécution.
# On attend d'abord en entrée deux entiers séparés par un espace :
# N est le nombre de sommets, M le nombre d'arêtes dans le graphe.
N, M = map(int, input().split())
# Création d'une nouvelle instance de SccGraph avec N sommets.
sg = SccGraph(N)
# Boucle sur le nombre d'arêtes M : à chaque itération, on lit deux entiers a et b,
# qui définissent une arête dirigée de a vers b.
for _ in range(M):
    a, b = map(int, input().split())
    sg.add_edge(a, b)
# On calcule les composantes fortement connexes du graphe construit.
scc = sg.scc()
# On affiche le nombre de composantes fortement connexes trouvées.
print(len(scc))
# Pour chaque composante (appelée group), on affiche d'abord son nombre de sommets,
# puis la liste des sommets (tous les membres de la composante).
for group in scc:
    print(*([len(group)] + group))  # Notation * pour envoyer chaque élément du tableau séparément à print.