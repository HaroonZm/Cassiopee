# Lecture des entrées
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Calcul de la somme des éléments de A
sum_A = sum(A)
# Calcul de la somme des éléments de B
sum_B = sum(B)

# Le total de la saveur est la somme de toutes les combinaisons possibles, soit :
# (A_1 + A_2 + ... + A_N) * (B_1 + B_2 + ... + B_M)
total_deliciousness = sum_A * sum_B

# Affichage du résultat avec une nouvelle ligne
print(total_deliciousness)