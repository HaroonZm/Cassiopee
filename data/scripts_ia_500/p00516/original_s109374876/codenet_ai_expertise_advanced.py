N, M = map(int, input().split())
A = [int(input()) for _ in range(N)]
B = [int(input()) for _ in range(M)]

# Optimisation: pré-calcul des indices où chaque B[j] pourrait incrémenter C[i]
# Utilisation de la fonction 'next' et d'une comprehension avec une recherche binaire possible

import bisect

sorted_A = sorted((val, idx) for idx, val in enumerate(A))
values = [val for val, _ in sorted_A]

C = [0] * N
for b in B:
    pos = bisect.bisect_right(values, b)
    if pos:
        C[sorted_A[pos-1][1]] += 1

max_idx = max(range(N), key=C.__getitem__)
print(max_idx + 1)