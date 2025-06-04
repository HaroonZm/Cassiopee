import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

max_val = 2 * 10**5
freq_B = [0] * (max_val + 1)
for b in B:
    freq_B[b] += 1

# Pré-calcul du nombre d'éléments dans B >= x pour x en [0..max_val]
count_ge = [0] * (max_val + 2)
for x in range(max_val, -1, -1):
    count_ge[x] = count_ge[x + 1] + freq_B[x]

result = 0
for a in A:
    # Pour chaque multiple k de a, on compte combien de B se situent dans [k*a, (k+1)*a)
    k = 0
    while k * a <= max_val:
        L = k * a
        R = min(max_val, (k+1)*a - 1)
        count_in_range = count_ge[L] - count_ge[R + 1]
        # Contribution de ces éléments: somme sur b dans ce range de b % a = sum (b - k*a)
        result += count_in_range * (a * k) * (-1)  # on soustrait k*a pour le mod, mais vu plus bas
        k += 1

# La somme de tous les éléments de B multipliée par N
sum_B = sum(B)
result += N * sum_B

print(result)