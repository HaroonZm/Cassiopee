from heapq import nlargest
import numpy as np

def solve(n, a_list):
    # Associer directement les indices pour les éléments triés par valeur décroissante
    items = nlargest(n, enumerate(a_list), key=lambda x: x[1])
    positions = np.arange(n)
    # Initialiser dp avec -inf
    dp = np.full((n + 1, n + 1), -np.inf, dtype=np.int64)
    dp[0, 0] = 0

    for i, (k, a) in enumerate(items):
        left_pos = positions[:i+1]
        right_pos = positions[-(i+1):][::-1]
        # Distributions gauche et droite vectorisées avec slicing avancé
        # On propage sur toutes les partitions déjà réalisées jusque là
        prev = dp[i, :i+1]
        # Placement à gauche
        dp[i+1, 1:i+2] = np.maximum(
            dp[i+1, 1:i+2],
            prev + a * np.abs(k - left_pos)
        )
        # Placement à droite
        dp[i+1, :i+1] = np.maximum(
            dp[i+1, :i+1],
            prev + a * np.abs(k - right_pos)
        )

    return int(np.max(dp[n, :]))

def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    print(solve(n, a_list))

def test():
    assert solve(4, [1, 3, 4, 2]) == 20
    assert solve(6, [5, 5, 6, 1, 1, 1]) == 58
    assert solve(6, [8, 6, 9, 1, 2, 1]) == 85

if __name__ == "__main__":
    test()
    main()