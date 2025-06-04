from sys import stdin
from itertools import accumulate

def main():
    N, D = map(int, stdin.readline().split())
    d = list(map(int, stdin.readline().split()))

    # Avancé : calcul lazy de dp avec accumulation et générateurs
    dp = [abs(D - d[0]) if abs(D - d[0]) < D else D]
    for i in range(1, N):
        dp.append(min(dp[-1], abs(dp[-1] - d[i])))

    # Précalcul data en utilisant tableau, optimisation du parcours arrière
    data = [0] * (N + 1)
    for i in range(N-1, -1, -1):
        if d[i] // 2 > data[i+1]:
            data[i] = data[i+1]
        else:
            data[i] = data[i+1] + d[i]

    # Expressions génératrices et comprehension
    ans = [
        "YES" if (dp[i-1] > data[i+1] if i > 0 else D > data[1]) else "NO"
        for i in range(N)
    ]

    Q = int(stdin.readline())
    queries = map(int, stdin.readline().split())
    print('\n'.join(ans[q-1] for q in queries))

if __name__ == "__main__":
    main()