N = int(input())
A = list(map(int, input().split()))

# dp[i][value] = le nombre de façons d'obtenir "value" après avoir traité le i-ème chiffre (0-based),
# en respectant les contraintes intermédiaires (0 <= value <= 20).
# On calcule uniquement jusqu'à l'avant-dernier chiffre, car le dernier est l'élément après le '='.
dp = [ [0]*21 for _ in range(N-1) ]

# Initialisation : la valeur après le premier chiffre est ce chiffre lui-même, une seule façon.
dp[0][A[0]] = 1

for i in range(1, N-1):
    for val in range(21):
        if dp[i-1][val] == 0:
            continue
        # Opération '+'
        new_val = val + A[i]
        if 0 <= new_val <= 20:
            dp[i][new_val] += dp[i-1][val]
        # Opération '-'
        new_val = val - A[i]
        if 0 <= new_val <= 20:
            dp[i][new_val] += dp[i-1][val]

# Nombre de façons où le résultat final (avant '=') est égal au dernier chiffre
# car l'équation est de la forme expr = A[N-1]
print(dp[N-2][A[N-1]])