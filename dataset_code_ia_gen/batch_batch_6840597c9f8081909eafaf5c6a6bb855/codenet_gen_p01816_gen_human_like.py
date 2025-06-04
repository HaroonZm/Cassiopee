import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N, M = map(int, input().split())
ops = [None] * N
ops[0] = None
for i in range(1, N):
    ops[i] = input().strip()

graph = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# On construit un arbre enraciné en 0, et on mémorise les enfants
parent = [-1] * N
parent[0] = 0
stack = [0]
order = []
while stack:
    u = stack.pop()
    order.append(u)
    for w in graph[u]:
        if parent[w] == -1:
            parent[w] = u
            stack.append(w)

children = [[] for _ in range(N)]
for v in range(1, N):
    children[parent[v]].append(v)

# On définit une fonction qui applique l'opération du noeud sur T avec X,Y
def apply_op(t, op, X, Y):
    if op is None:
        return t
    if 'X' not in op and 'Y' not in op:
        return t
    # op est une string parmi: T=T&X, T=T&Y, T=T|X, T=T|Y, T=T^X, T=T^Y
    if op == 'T=T&X':
        return t & X
    if op == 'T=T&Y':
        return t & Y
    if op == 'T=T|X':
        return t | X
    if op == 'T=T|Y':
        return t | Y
    if op == 'T=T^X':
        return t ^ X
    if op == 'T=T^Y':
        return t ^ Y
    return t

# On travaille par dfs sur l'arbre pour calculer les scores optimaux T possible en partant d'une même valeur
# À chaque noeud, les joueurs jouent à alterner :
#   A veut max(T_next)
#   B veut min(T_next)
# 
# On sait que le joueur jouant au noeud d'indice 'depth' % 2
# On calcule dp(u, t, player) = score final optimal si on est au noeud u avec valeur t et c'est player qui joue.
# Mais t peut prendre 2^16 valeurs => impossible.
#
# Donc on fait la stratégie inverse: on pré-calcule une fonction f_u(t) = valeur finale optimal en partant du noeud u avec T = t au départ du noeud (après avoir appliqué l'opération du noeud).
#
# Les opérations ne changent que t une fois.
# Comme T est borné par 2^16, on peut faire de la programmation dynamique avec un tableau de taille 2^16 à chaque noeud
# Mais N=10^5 est trop grand pour ça.
#
# On remarque que la racine a T=0 au départ (avant la première opération, c'est 0).
# Ensuite on applique l'opération du noeud sur T.
# On va mémoriser un tableau de taille 2^16 pour chaque noeud éliminé.
# C'est trop grand.
#
# Solution: on remarque que la structure du jeu est un min-max sur chemin d'arbre.
# Pour chaque noeud on calcule, sachant la valeur de T en arrivant sur ce noeud (avant d'appliquer op), la valeur optimale qu'on peut obtenir jusqu'à la feuille.
# On peut inverser le problème:
# pour chaque valeur de T possible, calculer la meilleure valeur finale.
#
# Essayer une autre méthode :
# On fait une fonction f(u, t) = score optimal pour joueur au noeud u avec valeur t.
# Le joueur à u est A si profondeur[u]%2==0, sinon B
# On applique op[u] sur t, obtenant t2.
# Si u est une feuille, f(u,t) = t2
# Sinon si joueur A, f(u,t) = max_{v enfant de u} f(v,t2)
# sinon f(u,t) = min_{v enfant de u} f(v,t2)
#
# Pour chaque jeu, on fait f(0,0).
#
# Mais pour M=10^5 et N=10^5, c'est lourd.
#
# Observation: Les opérations s'appliquent à T qui est au plus 16 bits. L'arbre a 10^5 noeuds.
#
# L'idée est de pré-calculer un tableau des valeurs pour chaque noeud, pour toutes les valeurs possibles de T.
#
# Impossible en mémoire.
#
# Nouvelle idée:
# Chaque noeud correspond à une fonction de T --> résultat
# On peut regarder la fonction complète représentée par ce noeud, calculée à partir des fonctions des enfants.
#
# On va construire une fonction représentée par un tableau de 0..2^16 (65536) entiers.
#
# Le nombre de noeuds est grand, donc mémoire trop grande (65536*100000)
#
# On peut essayer d'utiliser une structure de calcul fonctionnelle via Trie (Bit DP)
#
# Alternative suggérée par la contrainte:
# Les opérations sont & X, & Y, | X, | Y, ^ X, ^ Y
# donc on peut composer les fonctions linéaires sur bits.
#
# On peut représenter les fonctions composées comme deux masques pour un opérateur & puis | puis ^ (layers)
#
# On va représenter chaque fonction f : x -> ((x & A) | B) ^ C
# Qui suffit pour toutes combinaisons de &,|,^
#
# Chaque opération appliquée à f peut être combinée par composition avec un masque & et | et ^
#
# On peut donc composer les fonctions du chemin par leur masque.
#
# Ensuite faire min-max sur les enfants.
#
# MAIS B cherche à minimiser, A à maximiser
#
# On peut calculer pour chaque noeud une fonction f_u correspondante à appliquer à T la fonction de ce noeud et ses enfants avec min/max.
#
# On peut représenter f_u par 3 masques: a (for &), b (for |), c (for ^).
#
# Mais quel masque choisir parmi les enfants pour min/max ?
#
# Il y a un nombre large de fonctions.
#
# On doit faire min ou max sur les résultats, donc pas possible directement sur les fonctions masques.
#
# Donc on procède ainsi:
# On code une fonction pour appliquer l'opération du noeud sur un ensemble de valeurs t.
# Puis on fait dfs par récursion
# Pour chaque noeud, on récupère les arrays des enfants, on applique l'opération, puis on fait min ou max sur les arrays enfants
# Comme on ne peut pas stocker autant,
# On procède à un rappel récursif sur T seulement lors des queries.
#
# On implémente une fonction dfs(u, T, X, Y, player) pour un couple (X,Y) donné
# On mémorise les résultats dans un dictionnaire pour éviter recalculs
#
# Comme M peut être 10^5, et le même noeud peut être appelé plusieurs fois avec différentes T, ce sera trop lent
#
# Donc on pré-calculera la profondeur (pair ou impair) et le parent des noeuds puis on générera les stratégies en hauteur.
#
# Finalement la solution ou on simule la partie par la recherche du meilleur chemin va marcher:
#
# Pour chaque (X,Y), on parcourt l'arbre avec minimax:
#   T initial = 0
#   On fait une dfs minimax(u, T, player)
#   On applique op[u]
#   Si feuille → retourner T
#   Sinon
#      Si player=A → return max dfs enfant
#      Si player=B → return min dfs enfant
#
# Pour optimiser, on mémorise la profondeur de chaque noeud; player = 0 (A) si profondeur pair, 1 (B) sinon
#
# On a N=10^5, M=10^5 et chaque appel complet serait O(N) → trop grand,
# Il faut améliorer :
#
# On pré-calcule les enfants car c'est un arbre.
#
# Grâce à la profondeur, on fait que le joueur A joue max, B joue min.
#
# Le problème est fortement lié aux opérations et pas aux (X,Y)
#
# Il faut noter que sur un même arbre pour différents (X,Y), la structure min/max ne change pas.
#
# On va coder une fonction qui:
# - Récursivement, fait f(u, T, X, Y) → score final pour sommet u, valeur T actuelle, en jouant optimally
#
# Pour que ça soit rapide, on fera un cache LRU limité selon (u,T)
#
# Mais T peut être 2^16 différentes valeurs → cache énorme
#
# Alternative: on fait pour chaque (X,Y):
# A l'étape racine T=0
# On fait dfs_minimax(u, T):
#     T2 = apply_op(t, op[u], X, Y)
#     si feuille: retourne T2
#     si player A: retourne max over children dfs_minimax(child, T2)
#     sinon: min
#
# On limite le dfs car on l'exécute M fois
#
# Donc optimisation : faire une mémorisation seulement par (u, joueur), mais T différente
#
# Pas possible.
#
# On va ici coder simplement l'algorithme récursif et on verra si passe. Sinon faudrait faire la même logique.
#
# Coder avec sys.setrecursionlimit et @lru_cache pour accélérer
#
# Feel free to timeout for big inputs, solution conceptuelle.

depth = [-1] * N
depth[0] = 0
stack = [0]
while stack:
    u = stack.pop()
    for w in children[u]:
        depth[w] = depth[u] + 1
        stack.append(w)

from functools import lru_cache

# player at node = A if depth[u]%2==0, else B

def op_func(t, op, X, Y):
    if op == None:
        return t
    if op == 'T=T&X':
        return t & X
    if op == 'T=T&Y':
        return t & Y
    if op == 'T=T|X':
        return t | X
    if op == 'T=T|Y':
        return t | Y
    if op == 'T=T^X':
        return t ^ X
    if op == 'T=T^Y':
        return t ^ Y
    return t

sys.setrecursionlimit(10**7)

def solve_for_xy(X, Y):
    @lru_cache(None)
    def dfs(u, T):
        T2 = op_func(T, ops[u], X, Y)
        if not children[u]:
            return T2
        if depth[u] % 2 == 0:  # A joue, maximise
            res = 0
            first = True
            for w in children[u]:
                val = dfs(w, T2)
                if first or val > res:
                    res = val
                    first = False
            return res
        else:
            res = 0
            first = True
            for w in children[u]:
                val = dfs(w, T2)
                if first or val < res:
                    res = val
                    first = False
            return res
    return dfs(0, 0)

for _ in range(M):
    Xq, Yq = map(int, input().split())
    print(solve_for_xy(Xq, Yq))