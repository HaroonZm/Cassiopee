n, m = map(int, input().split())
U = input().strip()
A = list(map(int, input().split()))
constraints = [tuple(map(int, input().split())) for _ in range(m)]

# On représente l'état de chaque fantôme par un bit: 0 si il regarde comme initialement, 1 sinon.
# Le coût de retourner un fantôme i est A[i].

# Calculer le coût minimal total en assignant un état (0 ou 1) à chaque fantôme.

# On modifie les contraintes:
# Deux fantômes i < j sont en face si i regarde à droite et j regarde à gauche.
# Chaque fantôme peut retourner une fois => l'état final pour i est:
#   Si U[i] = 'L', état 0 = regarde à gauche, état 1 = regarde à droite
#   Si U[i] = 'R', état 0 = regarde à droite, état 1 = regarde à gauche
# Les fantasmes se tournent:

# Ainsi, pour chaque i, si U[i] = 'L':
#   état 0 => gauche
#   état 1 => droite
# Sinon (U[i] = 'R'):
#   état 0 => droite
#   état 1 => gauche

# Le coût pour activer état 1 pour i est A[i].
# Le coût pour état 0 est 0.

# Pour chaque contrainte entre S_i et T_i, ajouter B_i au total si S_i regarde à droite et T_i regarde à gauche.

# Cette condition correspond à (état[S_i], état[T_i]) = (1,0) si on définit état = 0 ou 1 comme ci-dessus.

# Donc on veut minimiser:
# sum_i A[i]*état[i] + sum_j B_j * [état[S_j] == 1 and état[T_j] == 0]

# On peut modéliser cela comme un graphe de flux avec les techniques de min-cut.

# Construire un graphe pour min cut:
# Chaque variable i a un noeud.
# On construit un graphe à partir du problème comme suit:

# - Source (S) et puits (T).
# - Pour chaque i:
#   Cette variable peut être dans état 0 (pas retourner) ou 1 (retourné).
# - On peut associer un coût pour passer de state 0->1 (i.e. retourner: coût A[i]).

# Pour chaque contrainte:
#   si at final (état[S]=1 et état[T]=0) => pénalité B
#   On modélise comme une arête dirigée entre les noeuds qui force la coupure qui permet uniquement cette combinaison.

# On définit "état" comme suit:
#   si nous séparons le noeud i du source, état[i] =1;
#   sinon état[i] =0

# Construction:
#   - Edge from source to i with capacity A[i] (le coût de retourner).
#   - Edge from i to sink with capacity 0 (pas d'autre coût fixe).
#   - Pour la contrainte (S,T,B), on veut pénaliser le cas (état[S]=1, état[T]=0)
#     Cette pénalité correspond à une arête de i->j avec capacité B_j
#     Car pour que l'arête ne soit pas coupée, état[S]=0 ou état[T]=1,
#     else la coupure doit payer B_j

# En reprenant:
# - Si on coupe cette arête S->T, ça correspond à état[S]=1 et état[T]=0, donc pénalité.

# On construit donc:
#   Edge source->i avec capacité A[i]
#   Edge i->sink avec 0 (inutile)
#   Pour chaque contrainte S,T,B:
#       Edge i->j avec capacité B

# Puis min-cut find.

from collections import deque

class MaxFlow:
    def __init__(self, n):
        self.n = n
        self.edges = [[] for _ in range(n)]
    def add_edge(self, frm, to, cap):
        self.edges[frm].append([to, cap, len(self.edges[to])])
        self.edges[to].append([frm, 0, len(self.edges[frm]) - 1])
    def bfs(self, s, t, level):
        queue = deque()
        level[s] = 0
        queue.append(s)
        while queue:
            v = queue.popleft()
            for i, (to, cap, rev) in enumerate(self.edges[v]):
                if cap > 0 and level[to] < 0:
                    level[to] = level[v] + 1
                    queue.append(to)
        return level[t] >= 0
    def dfs(self, v, t, upTo, level, iter):
        if v == t:
            return upTo
        while iter[v] < len(self.edges[v]):
            to, cap, rev = self.edges[v][iter[v]]
            if cap > 0 and level[v] < level[to]:
                d = self.dfs(to, t, min(upTo, cap), level, iter)
                if d > 0:
                    self.edges[v][iter[v]][1] -= d
                    self.edges[to][rev][1] += d
                    return d
            iter[v] += 1
        return 0
    def max_flow(self, s, t):
        flow = 0
        level = [-1]*self.n
        INF = 10**15
        while True:
            level = [-1]*self.n
            if not self.bfs(s, t, level):
                return flow
            iter = [0]*self.n
            while True:
                f = self.dfs(s, t, INF, level, iter)
                if f == 0:
                    break
                flow += f

# Indexation des fantômes de 0 à N-1
# Construction du graphe:
# - source = N
# - sink = N+1
S = n
T = n +1
mf = MaxFlow(n+2)

# Pour chaque fantôme, l'état 1 a un coût A[i]
# On va connecter source -> i avec capacité A[i], pour représenter le coût retourner.
# Pas besoin d'arête i -> sink car le coût d'état 0 est 0.

# Définir mapping si U[i] = 'L': état 1 = regarde à droite
#          U[i] = 'R': état 1 = regarde à gauche

for i in range(n):
    # Ajouter edge source -> i avec capacité A[i]
    mf.add_edge(S, i, A[i])

# Pour chaque contrainte (S_i, T_i, B_i)
# Définir l'arête qui pénalise si etat[S_i]=1 et etat[T_i]=0
# Ce qui équivaut source->S_i->T_i->sink mais on s'arrête au noeud T_i.
# On ajoute une arête de S_i-1 -> T_i-1 avec capacité B_i
# (indices décalés de 1 pour 0-based)
for s_i, t_i, b_i in constraints:
    s_i -=1
    t_i -=1
    # Ajouter arête s_i -> t_i avec capacité b_i
    mf.add_edge(s_i, t_i, b_i)

res = mf.max_flow(S, T)
print(res)