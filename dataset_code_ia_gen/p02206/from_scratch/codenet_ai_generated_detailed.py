# Solution en Python pour le problème de distribution de la prime selon les contraintes données.
# Commentaire détaillé expliquant l'approche suivie.

# Problème résumé :
# - N membres dans l'équipe numérotés de 1 à N (Segtree est le 1).
# - K, la somme totale de la prime à répartir entre les N membres.
# - Chaque membre i (i≥2) doit recevoir au moins la moitié entière (floor division by 2) de la prime reçue par le membre i-1.
#   Sinon, il s’énerve.
# - Trouver la prime maximale que Segtree (membre 1) peut recevoir sans faire enrager personne.
# - En d'autres termes, on cherche le maximum a1 tel que :
#    a1 + a2 + a3 + ... + aN <= K
#    et pour tout i>=2, a_i >= floor(a_{i-1} / 2).
#
# Approche :
# On note a1 = x (ce que Segtree reçoit).
# La suite est définie par :
#    a_1 = x
#    a_2 = floor(x/2)
#    a_3 = floor(a_2/2) = floor(floor(x/2)/2)
#    ...
#
# On remarque que la somme S(x) = x + floor(x/2) + floor(floor(x/2)/2) + ... est décroissante rapidement.
# La suite est égale à la somme des divisions successives par 2 (floor).
#
# Pour trouver le maximal x avec S(x) <= K, on peut utiliser une recherche binaire entre 0 et K (car Segtree ne peut pas recevoir plus que K).
#
# Implémentation des étapes :
# 1. Une fonction "sum_awards(x, N)" qui calcule la somme des primes données avec a1 = x selon les règles.
# 2. Une recherche binaire sur x dans [0..K] pour chercher le maximum x avec sum_awards(x, N) <= K.

import sys

def sum_awards(x, N):
    # Calcule la somme des primes a_i pour i=1..N,
    # avec a_1 = x et a_i = floor(a_{i-1}/2) pour i>=2.
    # Optimisation : On arrête dès que a_i == 0 car après, tous a_j seront 0.
    total = 0
    cur = x
    for _ in range(N):
        if cur == 0:
            break
        total += cur
        cur //= 2
    return total

def main():
    input_line = sys.stdin.readline()
    N_str, K_str = input_line.strip().split()
    N = int(N_str)
    K = int(K_str)

    # Recherche binaire pour le max x avec sum_awards(x, N) <= K
    left = 0
    right = K  # max possible pour Segtree

    while left < right:
        mid = (left + right + 1) // 2
        if sum_awards(mid, N) <= K:
            left = mid
        else:
            right = mid - 1

    print(left)

if __name__ == "__main__":
    main()