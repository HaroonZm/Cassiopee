import sys  # Importation du module système pour accéder aux flux et méthodes système
input = sys.stdin.readline  # Redéfinition de la fonction input pour une lecture plus rapide, ligne par ligne
sys.setrecursionlimit(10**9)  # Augmente la limite de récursion afin de prévenir les erreurs liés à la profondeur maximale
from bisect import bisect_left, bisect_right  # Importation de fonctions pour la recherche binaire dans des listes triées

# Définition d'une classe pour résoudre le problème de flot à coût minimal
class MinCostFlow:
    # Constructeur, initialisé avec le nombre de nœuds (n) du graphe
    def __init__(self, n):
        self.n = n  # Stocke le nombre de nœuds dans l'objet
        self.edges = [[] for i in range(n)]  # Initialise une liste d'adjacence vide pour chaque nœud

    # Méthode d'ajout d'une arête orientée de 'fr' (from) à 'to' avec une capacité 'cap' et un coût 'cost'
    def add_edge(self, fr, to, cap, cost):
        # On ajoute l'arête directe de fr à to avec la capacité et le coût donnés
        # On stocke également l’indice de l’arête inverse, nécessaire pour la modification des capacités résiduelles
        self.edges[fr].append([to, cap, cost, len(self.edges[to])])
        # On ajoute en même temps l’arête résiduelle inverse de to à fr avec capacité 0 et coût opposé
        self.edges[to].append([fr, 0, -cost, len(self.edges[fr]) - 1])

    # Méthode principale pour calculer le coût minimal pour envoyer 'flow' unités du nœud 'source' au nœud 'sink'
    def MinCost(self, source, sink, flow):
        inf = 10**15 + 1  # Définition d'une valeur très grande représentant l’infini
        n, E = self.n, self.edges  # Raccourcis pour le nombre de nœuds et la liste des arêtes
        prev_v, prev_e = [0] * n, [0] * n  # Tableaux pour mémoriser le précédent nœud et l'arête utilisée pour chaque nœud
        mincost = 0  # Variable pour accumuler le coût minimum total

        while flow:  # Boucle principale qui s'exécute jusqu'à ce que tout le flot demandé soit envoyé
            dist = [inf] * n  # Initialise les distances (coût depuis la source) pour chaque nœud à l'infini
            dist[source] = 0  # La distance à la source elle-même est 0
            flag = True  # Utilisé pour vérifier si une mise à jour a eu lieu dans la boucle suivante

            # Algorithme de Bellman-Ford (version améliorée), repeat jusqu’à plus de mise à jour
            while flag:
                flag = False  # On suppose qu'aucune mise à jour n'aura lieu
                for v in range(n):  # Pour chaque nœud du graphe
                    if dist[v] == inf:  # Si le nœud est encore inaccessible, on ne fait rien
                        continue
                    Ev = E[v]  # Raccourci pour la liste d'arêtes sortantes depuis v
                    for i in range(len(Ev)):  # Pour chaque arête sortant de v
                        to, cap, cost, rev = Ev[i]  # Décomposition des informations de l’arête
                        # Si arête utilisable (capacité > 0) et amélioration du coût possible
                        if cap > 0 and dist[v] + cost < dist[to]:
                            dist[to] = dist[v] + cost  # Met à jour le coût d’atteindre le nœud 'to'
                            prev_v[to], prev_e[to] = v, i  # Mémorise le chemin pris pour l’atteindre (pour backtrack plus tard)
                            flag = True  # Signale qu'une amélioration a eu lieu

            if dist[sink] == inf:  # Si on ne trouve plus de chemin possible vers le puits (sink)
                return 1  # On retourne 1 pour signaler qu'il est impossible d'envoyer davantage de flot

            f = flow  # On initialise f avec la quantité de flot à envoyer
            v = sink  # On commence à backtracker depuis le sink
            # Recherche du goulot d'étranglement sur ce chemin (capacité min des arêtes du chemin trouvé)
            while v != source:
                f = min(f, E[prev_v[v]][prev_e[v]][1])  # Met à jour f
                v = prev_v[v]  # Remonte d’un coup à la source

            flow -= f  # On soustrait le flot envoyé du flot restant à envoyer
            mincost += f * dist[sink]  # On ajoute au coût total le coût de ce flot
            v = sink  # Réinitialisation pour modifier les capacités du chemin

            # Mise à jour des capacités sur le chemin (flot réel et flot résiduel)
            while v != source:
                E[prev_v[v]][prev_e[v]][1] -= f  # On retire la capacité sur l’arête directe
                rev = E[prev_v[v]][prev_e[v]][3]  # On récupère l'index de l'arête inverse
                E[v][rev][1] += f  # On augmente la capacité sur l’arête inverse (résiduelle)
                v = prev_v[v]  # Remonte d’un coup à la source

        return mincost  # On retourne le coût minimal total calculé

# Lecture du nombre d’éléments à traiter
n = int(input())
J = []  # Liste pour stocker les tuples de chaque élément (x, y, v)
L_org, D_org = [1] * n, [1] * n  # Listes de contraintes pour stocker valeurs initiales (gauche et bas) pour chaque index

# Lecture des données principales pour chaque élément
for _ in range(n):
    x, y, v = map(int, input().split())  # Lecture des coordonnées (x, y) et de la valeur associée v
    J.append((x, y, v))  # Stocke chaque tuple lu dans la liste J

# Lecture des modifications/contraintes supplémentaires
m = int(input())  # Lecture du nombre de contraintes supplémentaires
T = []  # Liste pour stocker les contraintes additionnelles

for _ in range(m):
    t, a, b = input().split()  # Lecture d'un triplet (type, valeur, index)
    a, b = int(a), int(b)  # Conversion des valeurs numériques
    T.append((t, a, b))  # Ajout de cette contrainte dans la liste T
    # Mise à jour appropriée de la liste de contraintes selon le type (L: gauche, D: bas)
    if t == 'L':
        L_org[b] = a + 1  # Pour les contraintes de gauche, on ajuste l’index b à a+1
    elif t == 'D':
        D_org[b] = a + 1  # Pour les contraintes de bas, on ajuste l’index b à a+1

# On parcourt les initialisations à partir de la deuxième case (pour éviter les conflits d’indices plus faibles)
for i in range(1, n):
    # On prend à chaque index le maximum cumulatif des contraintes jusqu’ici
    L_org[i] = max(L_org[i - 1], L_org[i])
    D_org[i] = max(D_org[i - 1], D_org[i])

# Définition d'une fonction de résolution prenant un entier k comme paramètre
def solve(k):
    # On copie les k premières valeurs des contraintes originales
    L, D = L_org[:k], D_org[:k]
    R, U = [100] * k, [100] * k  # On initialise les contraintes pour Droite (R) et Haut (U) à une valeur supérieure possible

    # Application des autres contraintes (à droite ou en haut)
    for t, a, b in T:
        if k - b - 1 >= 0:  # On ne traite que les indices valides
            if t == 'R':     # Pour les contraintes Droite
                R[k - b - 1] = a - 1  # On l’applique à l’indice qui lui correspond
            elif t == 'U':   # Pour les contraintes Haut
                U[k - b - 1] = a - 1

    # Mise à jour cumulative : pour chaque index, on prend la valeur minimale jusqu'ici (restriction la plus forte)
    for i in range(k - 2, -1, -1):  # Parcours à rebours du tableau d’indices
        R[i] = min(R[i], R[i + 1])
        U[i] = min(U[i], U[i + 1])

    # Création d’un objet MinCostFlow pour modéliser le problème de flot pour les k éléments
    solver = MinCostFlow(2 * n + 2 * k + 2)  # Nombre total de nœuds arbitrairement déterminé en fonction du problème

    # Ajout d’arêtes depuis la source (nœud 0) aux k premiers éléments (côté gauche du flot)
    for i in range(1, k + 1):
        solver.add_edge(0, i, 1, 0)  # Capacité unitaire, coût nul
        solver.add_edge(2 * n + k + i, 2 * n + 2 * k + 1, 1, 0)  # Chaque côté droit vers la destination (capacité 1, coût 0)

    # Ajout d’arêtes pour modéliser la sélection d'éléments parmi tous les n disponibles
    for i in range(n):
        v = J[i][2]  # On récupère la valeur v de l'élément i
        solver.add_edge(k + i + 1, n + k + i + 1, 1, -v)  # On relie (avec capacité 1 et coût négatif pour maximiser la valeur)

    # Connexion entre contraintes et objets selon leur position x, y et les tableaux de restriction
    for i in range(n):
        x, y = J[i][0], J[i][1]  # On récupère les coordonnées x, y de l'élément i
        l = bisect_right(L, x)  # Recherche du plus petit index où x < L[index], pour la gauche
        r = bisect_left(R, x) + 1  # Recherche du plus grand index où x ≧ R[index], pour la droite +1 car décalage d’indice
        d = bisect_right(D, y)  # Pareil pour y par rapport à D
        u = bisect_left(U, y) + 1  # Pareil pour U +1

        # Ajout d’arêtes depuis la contrainte de gauche vers les éléments sélectionnés selon les résultats de recherche binaire
        for j in range(r, l + 1):  # Pour tous les indices valides entre r et l (inclus)
            solver.add_edge(j, k + i + 1, 1, 0)  # Capacité unitaire, coût nul

        # Ajout d’arêtes depuis chaque objet vers les contraintes de droite selon y
        for j in range(u, d + 1):  # Pour tous les indices valides entre u et d (inclus)
            solver.add_edge(n + k + i + 1, 2 * n + k + j, 1, 0)  # Capacité unitaire, coût nul

    # Calcul du coût minimal total obtenu sous contrainte de flot k, renvoyé en valeur absolue (car valeurs négatives plus haut)
    return -solver.MinCost(0, 2 * n + 2 * k + 1, k)

ans = 0  # Variable pour stocker la réponse finale (le maximum trouvé)
k = 1  # On commence à k = 1, on cherche la meilleure sélection croissante

while True:  # Boucle principale pour tester toutes les valeurs de k possibles
    tmp = solve(k)  # On teste le cas pour k éléments sélectionnés
    ans = max(ans, tmp)  # On met à jour le maximum global si on a trouvé mieux
    if tmp == -1 or k == n:  # Si c'est impossible d'aller plus loin ou k atteint le maximum possible
        break  # On s’arrête
    k += 1  # Sinon, on augmente k et on recommence

print(ans)  # On affiche le résultat final, c’est-à-dire la valeur maximale trouvée