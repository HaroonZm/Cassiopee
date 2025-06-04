import sys  # Importation du module sys, utilisé pour la lecture des entrées standard et la configuration de la limite de récursion
input = sys.stdin.readline  # Redéfinition de la fonction input pour utiliser la méthode readline de stdin, ce qui est plus rapide pour la lecture de grandes entrées
sys.setrecursionlimit(10**9)  # Augmentation de la limite de récursion pour éviter l'erreur de récursion maximale dépassée dans des contextes récursifs profonds

from collections import deque  # Importation de deque, une structure de données pour une file d'attente doublement terminée, utile pour le parcours BFS/DFS
from bisect import bisect_left, bisect_right  # Importation des fonctions bisect_left et bisect_right permettant la recherche binaire dans des listes triées

# Définition d'une classe pour résoudre le problème de flot de coût minimum
class MinCostFlow:
    # Constructeur de la classe, initialisant le graphe de n sommets
    def __init__(self, n):
        self.n = n  # Nombre de sommets dans le graphe
        # Initialisation d'une liste d'adjacence pour chaque sommet, contenant toutes ses arêtes sortantes
        self.edges = [[] for i in range(n)]  
    
    # Méthode permettant d'ajouter une arête orientée allant de 'fr' à 'to' de capacité 'cap' et de coût 'cost'
    def add_edge(self, fr, to, cap, cost):
        # Ajout de l'arête directe avec information sur la position de l'arête reverse
        self.edges[fr].append([to, cap, cost, len(self.edges[to])])
        # Ajout de l'arête reverse (pour le graphe résiduel), de capacité initiale 0 et de coût opposé
        self.edges[to].append([fr, 0, -cost, len(self.edges[fr]) - 1])
    
    # Méthode principale pour calculer le flot de coût minimum du sommet 'source' à 'sink' en transportant 'flow'
    def MinCost(self, source, sink, flow):
        inf = 10**15 + 1  # Définition d'une valeur représentant l'infini pour cette implémentation
        n = self.n  # Stockage local du nombre de sommets
        E = self.edges  # Alias pour la liste d'adjacence pour un accès plus rapide
        mincost = 0  # Coût total minimal du flot recherché
        prev_v = [0] * n  # Tableau pour mémoriser le sommet précédent sur le chemin
        prev_e = [0] * n  # Tableau pour mémoriser l'arête précédente sur le chemin
        while flow:  # Boucle principale, s'arrête quand tout le flot demandé a été transporté
            dist = [inf] * n  # Initialisation du tableau des distances à l'infini (car on cherche le chemin de coût minimal)
            dist[source] = 0  # La distance à la source est nulle par définition
            q = deque([source])  # File pour le parcours, initialisée avec la source
            Flag = [False] * n  # Indicateur pour savoir si un sommet est actuellement dans la file
            Flag[source] = True  # On marque la source comme dans la file
            while q:  # Boucle BFS modifiée pour trouver le chemin de coût minimal dans un potentiel graphe négatif
                v = q.popleft()  # On enlève un sommet de la file
                if not Flag[v]:
                    continue  # Si le sommet n'est plus marqué comme dans la file, on le saute
                Flag[v] = False  # Marquer le sommet comme traité
                # On parcourt toutes les arêtes sortantes depuis v
                for i, (to, cap, cost, _) in enumerate(E[v]):
                    # Si la capacité est positive et que l'on trouve un chemin plus court
                    if cap > 0 and dist[to] > dist[v] + cost:
                        dist[to] = dist[v] + cost  # Mise à jour de la distance 
                        prev_v[to], prev_e[to] = v, i  # Stockage du précédent sommet et de l'indice de l'arête utilisée
                        q.append(to)  # Ajout du voisin dans la file
                        Flag[to] = True  # Marquer comme dans la file
            if dist[sink] == inf:
                return 1  # Si on n'a pas pu atteindre le puits, le flot est impossible
            f, v = flow, sink  # On commence avec le flot restant et le sommet cible (puits)
            # Recherche du flot effectif minimum sur le chemin trouvé (goulot d'étranglement)
            while v != source:
                f = min(f, E[prev_v[v]][prev_e[v]][1])  # Mise à jour avec la plus petite capacité sur le chemin
                v = prev_v[v]  # Remonter d'un sommet sur le chemin
            flow -= f  # Décrément du flot restant à envoyer
            mincost += f * dist[sink]  # Mise à jour du coût total accumulé
            v = sink  # On repart du puits
            # Mise à jour des capacités du graphe résiduel le long du chemin utilisé
            while v != source:
                E[prev_v[v]][prev_e[v]][1] -= f  # On enlève le flot utilisé sur l'arête directe
                rev = E[prev_v[v]][prev_e[v]][3]  # On récupère l'indice de l'arête reverse
                E[v][rev][1] += f  # On augmente la capacité de l'arête reverse dans le graphe résiduel
                v = prev_v[v]  # Remonter d'un sommet sur le chemin
        return mincost  # Retour du coût total du flot

# Lecture de l'entier n, représentant probablement le nombre de points ou d'entités à traiter
n = int(input())
J = []  # Liste pour stocker les données lues
L_org, D_org = [1]*n, [1]*n  # Listes initialisées à 1, servant à des bornes/marges pour chaque point

# Lecture des n triplets de valeurs pour J, et initialisation des bornes de L_org et D_org
for _ in range(n):
    x, y, v = map(int, input().split())  # Lecture de trois entiers : abscisse, ordonnée, valeur
    J.append((x, y, v))  # Ajout du triplet à la liste J

# Lecture du nombre m d'opérations ou contraintes supplémentaires
m = int(input())
T = []  # Liste pour stocker ces contraintes

# Lecture et traitement de chaque contrainte
for _ in range(m):
    t, a, b = input().split()  # Lecture du type de contrainte (t) et de deux entiers (a, b)
    a, b = int(a), int(b)  # Conversion des deux derniers éléments en entiers
    T.append((t, a, b))  # Ajout du triplet (type, valeur, index) à la liste T
    if t == 'L':
        L_org[b] = a + 1  # Mise à jour de L_org selon la contrainte
    elif t == 'D':
        D_org[b] = a + 1  # Mise à jour de D_org selon la contrainte

# Propagation vers l'avant : chaque position hérite de la borne maximale cumulée
for i in range(1, n):
    L_org[i] = max(L_org[i-1], L_org[i])  # Propager la borne gauche pour L_org
    D_org[i] = max(D_org[i-1], D_org[i])  # Propager la borne basse pour D_org

# Définition d'une fonction solve prenant k en paramètre, permettant de résoudre un sous-problème sur les k premiers objets
def solve(k):
    L, D = L_org[:k], D_org[:k]  # Récupérer les k premières valeurs des bornes gauches/basses
    R, U = [100]*k, [100]*k  # Initialisation des bornes droites/hautes à une grande valeur arbitraire (ici, 100)
    # Application des contraintes 'R' (droite) et 'U' (haut) si elles touchent les premiers k objets
    for t, a, b in T:
        if k - b - 1 >= 0:  # Vérifie si la contrainte concerne un des k premiers objets
            if t == 'R':
                R[k-b-1] = a - 1  # Mise à jour de la borne droite
            elif t == 'U':
                U[k-b-1] = a - 1  # Mise à jour de la borne haute
    # Propagation des bornes droites/hautes pour garantir la cohérence des contraintes
    for i in range(k-2, -1, -1):  # Parcours à l'envers pour minimiser chaque borne
        R[i] = min(R[i], R[i+1])
        U[i] = min(U[i], U[i+1])
    # Initialisation du solveur de flot à coût minimum sur un graphe construit spécialement d'après le problème et la valeur k
    solver = MinCostFlow(2*n + 2*k + 2)  # Graphe avec 2*n + 2*k + 2 sommets
    # Ajout des arêtes sources → sélection des lignes, et colonnes → puits (une capacité de 1 pour chaque élément)
    for i in range(1, k+1):  # Pour chaque première ligne ou indice jusqu'à k
        solver.add_edge(0, i, 1, 0)  # Arête du super-source (0) vers i, capacité 1, coût 0
        solver.add_edge(2*n + k + i, 2*n + 2*k + 1, 1, 0)  # Arête de la colonne vers le puits, capacité 1, coût 0
    # Ajout des arêtes internes entre objets J (chacun peut être relié à des lignes et colonnes)
    for i in range(n):
        v = J[i][2]  # Valeur de l'objet
        solver.add_edge(k + i + 1, n + k + i + 1, 1, -v)  # Arête entre deux couches, coût -v pour maximiser la somme
    # Ajout des arêtes entre les lignes sélectionnées et les objets, suivant si les contraintes sont respectées (fenêtres glissantes)
    for i in range(n):
        x, y = J[i][0], J[i][1]  # Position de l'objet
        l = bisect_right(L, x)  # Trouver la position où x > L[j] (bornes inclusives/exclusives selon le sens)
        r = bisect_left(R, x) + 1  # Pareil à droite
        d = bisect_right(D, y)
        u = bisect_left(U, y) + 1
        # Pour chaque ligne j correspondant à la fenêtre, ajout d'une arête de la ligne vers l'objet
        for j in range(r, l+1):
            solver.add_edge(j, k + i + 1, 1, 0)
        # Pour chaque colonne j correspondant à la fenêtre, ajout d'une arête de l'objet vers la colonne
        for j in range(u, d+1):
            solver.add_edge(n + k + i + 1, 2*n + k + j, 1, 0)
    # On retourne l'inverse du coût minimum trouvé (car les coûts sont négatifs pour maximiser la valeur totale)
    return -solver.MinCost(0, 2*n + 2*k + 1, k)

ans = 0  # Initialisation de la réponse maximale à 0
k = 1  # On commence avec un sous-ensemble de taille 1
# Boucle pour essayer tous les sous-ensembles de taille croissante
while True:
    tmp = solve(k)  # Appel de la fonction solve pour le k actuel
    ans = max(ans, tmp)  # Mise à jour de la meilleure réponse possible jusqu'ici
    if tmp == -1 or k == n:  # Si solve renvoie -1 (flot impossible) ou que l'on a atteint le maximum 
        break  # On arrête la boucle
    k += 1  # Sinon, on tente un sous-ensemble plus grand
print(ans)  # Affichage de la réponse finale, qui est la valeur maximale possible sous les contraintes