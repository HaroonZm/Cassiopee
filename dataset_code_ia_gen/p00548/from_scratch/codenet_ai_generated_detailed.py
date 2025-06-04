import sys
import collections

def main():
    input = sys.stdin.readline
    N, M, K = map(int, input().split())
    A = [int(input()) for _ in range(N)]

    # dp[i]: coût minimal pour empaqueter les oranges 0 à i-1
    dp = [float('inf')] * (N + 1)
    dp[0] = 0

    # Pour chaque position i (fin de sous-ensemble), on parcourt au plus M oranges à l'arrière
    # Afin de trouver la meilleure découpe possible en considérant des sous-tableaux contigus
    # avec au plus M éléments
    for i in range(1, N + 1):
        max_deque = collections.deque()  # stocke les valeurs A[j] décroissantes pour trouver le max
        min_deque = collections.deque()  # stocke les valeurs A[j] croissantes pour trouver le min
        # On essaie de prendre entre 1 et M oranges avant i
        for s in range(1, min(M, i) + 1):
            j = i - s  # début du segment [j..i-1]
            x = A[j]

            # Mettre à jour max_deque pour trouver max dans A[j..i-1]
            while max_deque and max_deque[-1] < x:
                max_deque.pop()
            max_deque.append(x)
            # Mettre à jour min_deque pour trouver min dans A[j..i-1]
            while min_deque and min_deque[-1] > x:
                min_deque.pop()
            min_deque.append(x)

            a = max_deque[0]
            b = min_deque[0]

            # Calcul du coût pour ce segment
            cost = K + s * (a - b)

            # Mise à jour dp
            if dp[j] + cost < dp[i]:
                dp[i] = dp[j] + cost

    # Résultat final : coût minimal pour empaqueter toutes les oranges
    print(dp[N])

if __name__ == "__main__":
    main()