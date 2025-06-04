n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Vérification de la somme des degrés d'entrée et de sortie
if sum(i * a[i] for i in range(n + 1)) != sum(i * b[i] for i in range(n + 1)):
    print("NO")
    exit()

# Total des sommets doit être n
if sum(a) != n or sum(b) != n:
    print("NO")
    exit()

# Construire la liste des sommets avec leur degré entrant et sortant
in_degs = []
out_degs = []

for deg in range(n + 1):
    in_degs.extend([deg] * a[deg])
    out_degs.extend([deg] * b[deg])

# Vérification supplémentaire des degrés totaux
if len(in_degs) != n or len(out_degs) != n:
    print("NO")
    exit()

# Trie les sommets (indice) par degré entrant et sortant, pour correspondre
# on va essayer d'affecter une matrice qui correspond aux degrés demandés
# L'approche: échanger out_degs (colonne) et in_degs (ligne) de manière à construire une matrice d'adjacence 0/1

# On va construire une liste de tuples (index, out_deg) triée par out_deg décroissante
out_vertices = sorted([(i, out_degs[i]) for i in range(n)], key=lambda x: -x[1])
in_vertices = sorted([(i, in_degs[i]) for i in range(n)], key=lambda x: -x[1])

# Initialisation de la matrice adjacence
E = [[0] * n for _ in range(n)]

# Vecteur mutable des demandes d'input degrés pour chaque ligne (d'entrée)
in_req = [deg for i, deg in in_vertices]
# Vecteur mutable des soutants (sortants) pour chaque colonne (sommets triés par out deg)
out_req = [deg for i, deg in out_vertices]

# Pour couvrir précisément les degrés, on va assigner des arcs depuis out_vertices vers in_vertices

for o_idx, (ori, deg_out) in enumerate(out_vertices):
    deg_to_assign = deg_out
    for i_idx, (endi, deg_in) in enumerate(in_vertices):
        if deg_to_assign == 0:
            break
        if in_req[i_idx] > 0 and E[ori][endi] == 0:
            E[ori][endi] = 1
            in_req[i_idx] -= 1
            deg_to_assign -= 1

    if deg_to_assign != 0:
        print("NO")
        exit()

# Vérification que chaque sommet a le degré d'entrée correspondant
if any(x != 0 for x in in_req):
    print("NO")
    exit()

print("YES")
for i in range(n):
    print(" ".join(str(E[i][j]) for j in range(n)))