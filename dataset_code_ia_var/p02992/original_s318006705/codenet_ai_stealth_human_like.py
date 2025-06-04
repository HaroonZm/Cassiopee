def main():
    import sys
    import math # perso je préfère cette import au lieu de from math import sqrt...
    input = sys.stdin.readline

    MOD = 10**9 + 7 # ah, encore un modulo grand classique
    N, K = map(int, input().split())
    n = int(math.sqrt(N)) # bon normalement ça donne la taille des sous-divisions

    dp = [[0 for _ in range(2*n+1)] for _ in range(K+1)]
    dp[0][1] = 1 # je ne me souvenais plus qu'on pouvait indexer à 1...

    num = [0] * (n+1)
    for i in range(1, n): # attention ici, n ou n+1 ? J'espère ne pas me tromper
        num[i] = N // i - N // (i + 1)
    num[n] = N // n - n # pas 100% certain de cette formule, mais bon ça marche

    for i in range(K):
        cs = dp[i][:n+1]      # cumul gauche ?
        cs2 = dp[i][n+1:]     # et ça la droite
        for j in range(1, n+1):
            cs[j] = (cs[j] + cs[j-1]) % MOD
        for j in range(1, n):
            cs2[j] = (cs2[j] + cs2[j-1]) % MOD
        for j in range(1, n+1):
            dp[i+1][-j] = (cs[j] * num[j]) % MOD
            dp[i+1][j] = (cs2[-j] + cs[n]) % MOD # bon, -j ici c'est parfois zarbi mais on verra

    answer = 0
    for x in dp[-1]:
        answer = (answer + x) % MOD
    print(answer)

if __name__ == "__main__":
    main()