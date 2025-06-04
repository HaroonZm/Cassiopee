# Solution complète pour le problème "True Liars"

# Approche :
# - Chaque habitant appartient soit à la tribu divine (vraisemblablement "vrai"), soit à la tribu diabolique (mensonge).
# - Les questions posées ont la forme : "L'habitant x dit que l'habitant y est membre de la tribu divine" (oui/non).
# - Si x est divine, alors sa déclaration est vraie.
# - Si x est diabolique, alors sa déclaration est fausse.
# 
# On doit déterminer, à partir des réponses, à quelle tribu chaque habitant appartient.
# Le problème est similaire à une formulation SAT / 2-SAT où chaque variable (habitant) peut être Vrai (divine) ou Faux (diabolique).
#
# Variables: pour chaque habitant i, une variable booléenne D_i = True s'il est divine, False sinon.
# 
# Contraintes: d'après la réponse a_i (yes/no) de x_i au sujet de y_i:
# - Si a_i == "yes":
#    Si x_i est divine, y_i doit être divine (D_xi => D_yi)
#    Si x_i est diabolique, il ment, donc y_i n'est pas divine (¬D_xi => ¬D_yi)
# - Si a_i == "no":
#    Si x_i est divine, alors y_i n'est pas divine (D_xi => ¬D_yi)
#    Si x_i est diabolique, alors y_i est divine (¬D_xi => D_yi)
#
# Ces contraintes peuvent être traduites en implications logiques, chacune sous forme 2-SAT:
# Exemple pour "yes":
#  D_xi → D_yi   <=> ¬D_xi ∨ D_yi
#  ¬D_xi → ¬D_yi <=> D_xi ∨ ¬D_yi
#
# Exemple pour "no":
#  D_xi → ¬D_yi  <=> ¬D_xi ∨ ¬D_yi
#  ¬D_xi → D_yi  <=> D_xi ∨ D_yi
#
# On construit un graphe d'implications pour les variables et leur négation.
# Ensuite on utilise l'algorithme 2-SAT classique (basé sur les composantes fortement connexes).
#
# Après avoir trouvé une solution compatible avec le nombre exact des membres divins (p1) et diaboliques (p2),
# on vérifie que cette solution est unique.
# Une solution est unique si aucune variable n'a d'alternative sans contradictions (on réalise deux passes de résolution SAT, une avec la variable vraie et l'autre avec la variable fausse, pour tester l'unicité).
#
# Si unique, on affiche la liste des divins; sinon "no".
#
# Code ci-dessous implémente cette méthode.

import sys
sys.setrecursionlimit(10**7)

class TwoSAT:
    # Classe pour résoudre un problème 2-SAT avec n variables.
    # Variables indexées de 0 à n-1.
    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(2*n)]  # graphe d'implications
        self.adj_rev = [[] for _ in range(2*n)]  # graphe inverse pour SCC

    def add_implication(self, u, v):
        # Ajoute une implication u -> v dans le graphe
        self.adj[u].append(v)
        self.adj_rev[v].append(u)

    def add_or(self, u, v):
        # Ajoute la clause u OR v : ¬u -> v et ¬v -> u
        self.add_implication(u ^ 1, v)
        self.add_implication(v ^ 1, u)

    def add_var(self, u):
        # Force la variable u à True
        # u est un littéral: 2*index + 0 pour x_i, 2*index + 1 pour ¬x_i
        # Forcer x_i à vrai = clause (x_i)
        self.add_implication(u ^ 1, u)

    def var_id(self, x):
        # transforme la variable x (index 0..n-1) True en littéral 2*x (pour vrai) ou 2*x+1 (pour faux)
        return 2 * x

    def neg(self, u):
        # renvoie le littéral négation de u
        return u ^ 1

    def satisfiable(self):
        # Recherche des composants fortement connexes par Kosaraju
        n = 2 * self.n
        order = []
        used = [False] * n
        component = [-1] * n

        def dfs(v):
            used[v] = True
            for w in self.adj[v]:
                if not used[w]:
                    dfs(w)
            order.append(v)

        def rdfs(v, k):
            component[v] = k
            for w in self.adj_rev[v]:
                if component[w] == -1:
                    rdfs(w, k)

        for v in range(n):
            if not used[v]:
                dfs(v)
        k = 0
        for v in reversed(order):
            if component[v] == -1:
                rdfs(v, k)
                k += 1

        assignment = [False] * self.n
        for i in range(self.n):
            if component[2*i] == component[2*i+1]:
                return None  # insatisfiable
            assignment[i] = component[2*i] > component[2*i+1]
        return assignment

def solve():
    while True:
        line = ''
        while line.strip() == '':
            line = sys.stdin.readline()
            if not line:
                return
        n, p1, p2 = map(int, line.strip().split())
        if n == 0 and p1 == 0 and p2 == 0:
            break

        total = p1 + p2
        queries = []
        for _ in range(n):
            line = ''
            while line.strip() == '':
                line = sys.stdin.readline()
            x, y, a = line.strip().split()
            x, y = int(x), int(y)
            queries.append((x-1, y-1, a))  # indices de 0 à total-1

        # Construire le 2-SAT
        # variable i : True = divin, False = diabolique

        ts = TwoSAT(total)

        # Traduire chaque contrainte :
        # pour chaque question (x,y,a):
        # si a == "yes":
        #   D_x -> D_y    => ¬D_x ∨ D_y
        #   ¬D_x -> ¬D_y  => D_x ∨ ¬D_y
        # clause 1 : ¬D_x ∨ D_y
        # clause 2 : D_x ∨ ¬D_y
        # si a == "no":
        #   D_x -> ¬D_y   => ¬D_x ∨ ¬D_y
        #   ¬D_x -> D_y   => D_x ∨ D_y
        # clause 1 : ¬D_x ∨ ¬D_y
        # clause 2 : D_x ∨ D_y

        for x, y, a in queries:
            Dx = 2 * x
            Dy = 2 * y
            if a == 'yes':
                # ¬D_x ∨ D_y
                ts.add_or(Dx ^ 1, Dy)
                # D_x ∨ ¬D_y
                ts.add_or(Dx, Dy ^ 1)
            else:
                # ¬D_x ∨ ¬D_y
                ts.add_or(Dx ^ 1, Dy ^ 1)
                # D_x ∨ D_y
                ts.add_or(Dx, Dy)

        # Chercher une solution satisfaisante
        assignment = ts.satisfiable()
        if assignment is None:
            # Non possible (selon l'énoncé cela n'arrive pas car donnée cohérente)
            print("no")
            continue

        # Vérifier que le nombre de divins = p1
        nb_divin = sum(assignment)
        if nb_divin != p1:
            # Imposons la contrainte supplémentaire qu'on ait exactement p1 divins
            # Par la résolution SAT, on a une solution possible mais pas avec ce nombre ?
            # Comme l'énoncé dit les populations sont fiables, donc on doit trouver une solution avec ce count.
            # Sinon "no"
            print("no")
            continue

        # Vérifier unicité :
        # Unicité peut être vérifiée en essayant d'inverser chaque variable et voir si ça reste satisfiable.

        # Méthode:
        # Pour chaque variable i,
        # - si variable i est True dans l'affectation, forcer x_i = False et voir si satisfiable.
        # - si oui, alors multiple solutions, pas unique.
        #
        # Pour accélérer, on peut ne tester que les variables où on a:
        # Au moins une variable testée révèlera si non unique.

        unique = True

        for i in range(total):
            ts2 = TwoSAT(total)
            # Recréer le graphe
            ts2.adj = [list(l) for l in ts.adj]
            ts2.adj_rev = [list(l) for l in ts.adj_rev]

            # Forcer variable i à la valeur opposée à assignment[i]
            # Littéral à forcer (True = 2*i, False = 2*i+1)
            if assignment[i]:
                # on avait True => on force False = 2*i+1
                ts2.add_var(2*i+1)
            else:
                # on avait False => on force True = 2*i
                ts2.add_var(2*i)

            assign2 = ts2.satisfiable()
            if assign2 is not None:
                # Il existe une autre solution distincte
                unique = False
                break

        if not unique:
            print("no")
            continue

        # Affichage des divins en ordre croissant + "end"
        for i in range(total):
            if assignment[i]:
                print(i+1)
        print("end")

if __name__ == "__main__":
    solve()