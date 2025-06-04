# Nous devons construire une tour en empilant des blocs, chaque étage ayant un certain nombre de blocs horizontalement.
# Chaque bloc supporte un poids maximum correspondant à K blocs.
# Le poids sur un bloc à un étage est égal à la somme des blocs situés au-dessus divisée par le nombre de blocs à cet étage.
# Le but est de maximiser le nombre d'étages de la tour.
# 
# Approche :
# - Notons les étages de haut en bas : étage 1 tout en haut, étage h le plus bas.
# - Soit la configuration des blocs par étage : b1, b2, ..., bh (bi >= 1)
# - La somme des bi est <= N.
# - Le poids sur chaque bloc à l'étage i est le poids total au-dessus (b1 + b2 + ... + b_{i-1}) divisé par bi.
# - Cette valeur doit être <= K.
# 
# Pour maximiser h, on essaye h possible et on vérifie s'il existe une répartition des blocs b1..bh qui respecte les contraintes.
# 
# Observations pour vérifier la faisabilité pour un h donné :
# 1. Au premier étage (tout en haut), il n'y a pas de blocs au-dessus, donc la contrainte est toujours satisfaite.
# 2. Pour chaque étage i > 1 :
#    poids maximal par bloc = K
#    poids total au-dessus = sum(b1 .. b_{i-1})
#    alors poids par bloc i = sum_b_above / bi <= K  => bi >= sum_b_above / K
#
# Stratégie pour minimiser le nombre total de blocs pour h étages :
# - Fixons b1 = 1 (minimiser les blocs du premier étage)
# - Pour i > 1, bi doit être au moins ceil(sum_b_above / K)
# - On calcule b_i selon la contrainte, on somme les blocs et on vérifie que la somme <= N
#
# Algorithme :
# - Testons par dichotomie la hauteur h possible entre 1 et N
# - Pour chaque h testé, on simule la construction :
#    b1 = 1
#    sum_blocks = 1
#    poids_above = 1
#    pour i de 2 à h:
#       bi = ceil(poids_above / K)
#       sum_blocks += bi
#       poids_above += bi
#    Si sum_blocks <= N alors h est faisable sinon non
# 
# La recherche binaire permettra d'optimiser la recherche de la hauteur maximale.

def max_stages(N, K):
    import math

    # Fonction testant si une hauteur h est réalisable avec N blocs et force K
    def can_build(h):
        # b1 = 1 (minimum)
        poids_above = 1  # somme des blocs au-dessus de l'étage i, initialement étage 1 ne porte pas de poids (haut)
        sum_blocks = 1   # nombre total de blocs utilisés
        for i in range(2, h + 1):
            # nombre minimum de blocs à l'étage i pour que poids par bloc <= K
            bi = (poids_above + K - 1) // K  # équivalent à ceil(poids_above / K)
            if bi == 0:
                bi = 1  # au moins un bloc par étage
            sum_blocks += bi
            poids_above += bi
            if sum_blocks > N:
                return False
        return True

    # Recherche binaire pour la hauteur maximale
    left, right = 1, N
    answer = 1
    while left <= right:
        mid = (left + right) // 2
        if can_build(mid):
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    return answer

# Lecture input
N, K = map(int, input().split())
# Calcul et sortie
print(max_stages(N, K))