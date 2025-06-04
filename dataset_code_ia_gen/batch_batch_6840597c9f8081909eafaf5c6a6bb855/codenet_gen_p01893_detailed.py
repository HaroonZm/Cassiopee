n = int(input())

# a_i: nombre de sommets avec degré entrant i
a = list(map(int, input().split()))
# b_i: nombre de sommets avec degré sortant i
b = list(map(int, input().split()))

# Vérification rapide des sommes pour une condition nécessaire
# La somme des degrés entrants doit être égale à la somme des degrés sortants
in_sum = sum(i * a[i] for i in range(n+1))
out_sum = sum(i * b[i] for i in range(n+1))
if in_sum != out_sum:
    print("NO")
    exit()

# Construire les listes des degrés entrants et sortants des sommets
# Chaque sommet aura un out_deg et un in_deg assigné selon a et b
in_deg_list = []
for deg_in in range(n+1):
    in_deg_list.extend([deg_in]*a[deg_in])

out_deg_list = []
for deg_out in range(n+1):
    out_deg_list.extend([deg_out]*b[deg_out])

# Vérifier que le nombre total de sommets correspond
if len(in_deg_list) != n or len(out_deg_list) != n:
    # Somme a_i ou b_i ne correspond pas au nombre de sommets
    print("NO")
    exit()

# On va essayer de trouver une affectation des sommets: quelle permutation des sommets 
# associe leur out_deg à un sommet avec in_deg, pour essayer de construire une matrice d'adjacence.

# L'idée: On ordonne les sommets par out_deg décroissant et in_deg décroissant
# Puis on construit la matrice au fur et à mesure en tentant de satisfaire les contraintes.
# C'est une variante du problème de la réalisation d'une matrice binaire avec des marges données.

# Représentons les sommets par leurs indices après tri (permutation)
vertices = list(range(n))

# Pour la construction, on utilise une technique de "greedy" souvent utilisée dans la théorie des graphes bipartis:
# On trie les sommets par out_deg décroissant et in_deg décroissant
# Ensuite, on construit arêtes du sommet avec plus grand out_deg vers les sommets avec plus grand in_deg.

# Trier index selon out_deg décroissant
out_sorted = sorted(vertices, key=lambda x: out_deg_list[x], reverse=True)
# Trier index selon in_deg décroissant
in_sorted = sorted(vertices, key=lambda x: in_deg_list[x], reverse=True)

# Pour construire la matrice: initialement tout à 0
E = [[0]*n for _ in range(n)]

# On crée des copies des degrés à entamer (restants)
out_remain = out_deg_list[:]
in_remain = in_deg_list[:]

# On va essayer d'affecter les arêtes de la manière suivante:
# Pour chaque sommet selon out_sorted,
# on essaie d'ajouter des arêtes vers des sommets selon in_sorted tant que degres le permettent
# On autorise les boucles (i->i) puisque elles sont permises

# Pour éviter multiples arêtes, on prend soin de ne pas doubler

# Algorithme:
# Pour chaque sommet u selon out_sorted:
#   on parcourt les sommets v selon in_sorted:
#       si out_remain[u] > 0 et in_remain[v] > 0 et E[u][v] == 0:
#           on place une arête u->v
#           décrémente out_remain[u], in_remain[v]
#       arrête quand out_remain[u]==0

for u in out_sorted:
    # On parcourt in_sorted pour trouver v
    for v in in_sorted:
        if out_remain[u] == 0:
            break
        if in_remain[v] == 0:
            continue
        if E[u][v] == 1:
            # Pas de multi-arêtes
            continue
        # On peut placer une arête
        E[u][v] = 1
        out_remain[u] -= 1
        in_remain[v] -= 1

# Vérification finale : tous les degrés doivent être satisfaits
if all(x == 0 for x in out_remain) and all(x == 0 for x in in_remain):
    print("YES")
    for i in range(n):
        print(" ".join(str(E[i][j]) for j in range(n)))
else:
    print("NO")