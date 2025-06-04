import sys
input = sys.stdin.readline

# Lecture des données initiales
N, Q, S, T = map(int, input().split())
A = [int(input()) for _ in range(N + 1)]

# La température change dépend uniquement des pentes entre A[i] et A[i+1]
# Initialement, la température à Spot 0 est 0
# Delta T entre Spot i et Spot i+1 :
#   Si A[i] < A[i+1] => temperature diminue de S*(A[i+1]-A[i])
#   Sinon => temperature augmente de T*(A[i]-A[i+1])

# Calculer initialement la somme de température à Spot N
# On somme les changements de température entre chaque paire (i,i+1)
temp_sum = 0
for i in range(N):
    diff = A[i+1] - A[i]
    if diff > 0:
        temp_sum -= S * diff
    else:
        temp_sum += T * (-diff)

# Pour chaque opération, on modifie certains A[k] avec X_j (additif)
# L'altitude change de X_j pour tous les k in [L_j,R_j]
# Il faut mettre à jour la température en tenant compte uniquement des bords de l'intervalle car
# les pentes internes de l'intervalle sont inchangées (tout est augmenté du même montant)

# Ainsi seules les pentes aux positions L_j-1 et R_j peuvent être affectées :
# - arête à gauche : entre L_j-1 et L_j (si L_j > 1)
# - arête à droite : entre R_j et R_j+1 (si R_j < N)

# On applique donc les changements uniquement sur ces 0, 1 ou 2 pentes

# Fonction pour calculer la contribution à la température entre i et i+1
def edge_contrib(a_i, a_next):
    diff = a_next - a_i
    if diff > 0:
        return -S * diff
    else:
        return T * (-diff)

for _ in range(Q):
    L, R, X = map(int, input().split())

    # Mise à jour des bords affectés
    # Avant modification, on retire la contribution des 2 arêtes possibles

    # Arête à gauche (L-1, L)
    if L > 1:
        temp_sum -= edge_contrib(A[L - 2], A[L - 1])

    # Arête à droite (R, R+1)
    if R < N:
        temp_sum -= edge_contrib(A[R - 1], A[R])

    # On applique la modification aux altitudes de L à R
    # Pour éviter une boucle coûteuse, on met à jour les altitudes directement
    # Cela peut être optimisé avec segment tree mais pas obligatoire ici
    # Néanmoins la contrainte est grande, il faut une solution O(Q) ou O(Q log N) => 
    # Pour cela on ne modifie pas tout A[L:R+1] mais on garde en mémoire un delta et on applique le delta avec une structure
    # Comme la solution en temps réel peut être coûteuse, on utilise un tableau de décalage (lazy propagation concept)
    # mais ici, on a la contrainte que les altitudes sont directement lus (ne pas faire lazy)
    # La seule façon est de stocker les altitudes, mais ici on va faire une approche différente

    # Approche alternative:
    # On garde les altitudes dans un tableau, on applique la modification à un buffer de décalage
    # Prendre en compte décalages de chaque position avec un tableau de taille N+1 en utilisant une fenwick ou segment tree
    #
    # Mais on a besoin uniquement d'altitudes à L-1, L, R, R+1 car seules 2 arêtes sont affectées
    # Donc on garde un tableau de décalages + les altitudes initiales pour récupérer les altitudes uniquement nécessaires
    #
    # On va gérer un tableau delta de décalages de rang N+1 initialisé à 0
    # Après chaque query, on met delta[L], delta[R+1] pour faire difference prefix sum (Imos method)
    # Puis on calcule valeurs pour L-1, L, R, R+1 en calculant la somme prefix

    # Initialisation du tableau delta si premier tour:
    # On crée delta avec 0

    # On commence par ça : (hors boucle)

# Init delta [0]*(N+2) pour la méthode Imos
delta = [0] * (N + 2)

# Fonction pour avoir altitude actuelle à l'indice i: A[i] + sum delta[1..i]
def get_alt(i):
    # préfixe de delta jusqu'à i inclus
    # On va construire un tableau prefix sum pour delta en dehors de la boucle Q, 
    # mais ici on fait linéaire par query car max Q=200000 donc linéaire Q*4 ok
    # On optimise la somme prefix delta effectivement

    # On peut créer un prefix sum delta avant les queries mais on modifie delta à chaque query
    # On calcule la somme prefix delta à part sur les indices nécessaires

    # Ici on doit faire au maximum 4 calcule de delta prefix par query
    # On utilise une fonction auxiliaire:

    s = 0
    for j in range(i):
        s += delta[j+1]
    return A[i] + s

# mais la fonction ci-dessus en O(N) pour chaque call est trop lente.
# On doit garder un prefix_delta et le mettre à jour à chaque query.
# Problème : on modifie delta[L] += X et delta[R+1] -= X
# On peut avoir un prefix_delta corrompu après chaque modification.
# Donc, on garde un tableau prefix_delta à jour en faisant delta comme Fenwick ou segment tree.
# Comme on fait Q updates et Q queries, Fenwick tree est adapté.

class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0]*(n+1)
    def add(self, i, x):
        while i <= self.n:
            self.bit[i] += x
            i += i & (-i)
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & (-i)
        return s
    def range_add(self, l, r, x):
        self.add(l, x)
        self.add(r+1, -x)
    def get(self, i):
        return self.sum(i)

fenw = Fenwick(N+1)

for _ in range(Q):
    L, R, X = map(int, input().split())

    # Retirer anciennes contributions
    if L > 1:
        a_left = A[L-2] + fenw.get(L-1)
        a_right = A[L-1] + fenw.get(L)
        temp_sum -= edge_contrib(a_left, a_right)
    if R < N:
        a_left = A[R-1] + fenw.get(R)
        a_right = A[R] + fenw.get(R+1)
        temp_sum -= edge_contrib(a_left, a_right)

    # Appliquer modification dans fenw
    fenw.range_add(L, R, X)

    # Ajouter nouvelles contributions
    if L > 1:
        a_left = A[L-2] + fenw.get(L-1)
        a_right = A[L-1] + fenw.get(L)
        temp_sum += edge_contrib(a_left, a_right)
    if R < N:
        a_left = A[R-1] + fenw.get(R)
        a_right = A[R] + fenw.get(R+1)
        temp_sum += edge_contrib(a_left, a_right)

    print(temp_sum)