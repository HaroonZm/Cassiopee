import sys
sys.setrecursionlimit(10**7)

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

# alternation pré-calculée de gauche à droite
left = [1]*N
for i in range(1, N):
    if A[i] != A[i-1]:
        left[i] = left[i-1] + 1

# alternation pré-calculée de droite à gauche
right = [1]*N
for i in range(N-2, -1, -1):
    if A[i] != A[i+1]:
        right[i] = right[i+1] + 1

# sans modification, le max
ans = max(left)

# pour chaque position, tenter de changer une séquence commençant ou terminant ici
# On essaye de considérer l'effet d'une inversion sur un intervalle [l,r]
# L'idée est de modifier un segment pour maximiser la séquence alternée autour du segment modifié.
# On essaie donc de vérifier pour chaque position, combien on peut raccorder de gauche et de droite.

# On veut calculer la longueur après inversion sur [l,r]
# Inversion change 0->1 et 1->0 dans ce segment, donc les alternances proche deviennent lisses si on choisit bien

# Pour accélérer, on va tester pour chaque position i la coupure (inversion) possible:
# on peut essayer d'inverser un segment de longueur 1 (un seul élément)
# on parcourt et on vérifie la nouvelle longueur possible sans reconstruire tout.

# Pour cela on essaye pour chaque position i, soit inverser uniquement A[i]
# Et on calcule la longueur de la plus grande alternance qui passe par i après inversion de A[i]

def val(x):
    return 1 - x  # inversion

max_len = ans

for i in range(N):
    # On inverse A[i] seul
    new_val = val(A[i])

    # On regarde a gauche:
    left_len = 1
    if i > 0 and new_val != A[i-1]:
        left_len += left[i-1]

    # On regarde a droite:
    right_len = 1
    if i < N-1 and new_val != A[i+1]:
        right_len += right[i+1]

    # on combine :
    total = left_len + right_len -1
    if total > max_len:
        max_len = total

# Pour inverser un segment de plus de 1 élément, le maximum est atteint en inversant un seul élément de la zone où la séquence est mauvaise.
# Pour vérifier cela, on vérifie pour joindre les séquences alternées de part et d'autre d'un intervalle où la séquence est cassée.

# On essaie tous les cassures (i où A[i] == A[i+1])
for i in range(N-1):
    if A[i] == A[i+1]:
        # inversion sur [i+1,i+1] déjà testé (single element)
        # On essaie inversion sur [i+1, j], mais ça est coûteux.
        # Optons pour une approche efficace:

        # longueur à gauche (à gauche de i+1)
        left_len = left[i]

        # longueur à droite (à droite de i+1)
        right_len = right[i+1]

        # Si on inverse [i+1, i+1] (faible gain), mais on peut inverser [i+1, i+1] déjà testé.
        # L'inversion peut connecter ces deux séquences en une seule séquence alternée parfaite.

        # Pour connecter les deux bouts, on vérifie si en inversant [i+1, i+1], cela fonctionne (déjà fait).
        # Sinon on peut envisager d'inverser une plus grande partie.

        # Mais le maximum de séquence alternée possible est au plus left_len + right_len

        candidate = left_len + right_len
        if candidate > max_len:
            max_len = candidate

print(max_len)