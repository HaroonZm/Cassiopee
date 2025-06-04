# Lecture du nombre d'éléments
N = int(input())

# Lecture de la séquence d'entiers
A = list(map(int, input().split()))

# Initialisation du compteur de swaps
swap_count = 0

# Algorithme de tri à bulles selon le pseudocode donné
for i in range(N):
    for j in range(N-1, i, -1):
        # Comparer l'élément j avec l'élément précédent
        if A[j] < A[j-1]:
            # Échanger les deux éléments
            A[j], A[j-1] = A[j-1], A[j]
            swap_count += 1  # Incrémenter le nombre de swaps

# Affichage des résultats
# Afficher la séquence triée sur une ligne
print(' '.join(map(str, A)))

# Afficher le nombre total de swaps effectués
print(swap_count)