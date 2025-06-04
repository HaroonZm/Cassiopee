import sys

# J'augmente la récursion, au cas où
sys.setrecursionlimit(1000000000)
INF = 10**18  # Une grosse valeur, on verra si on s'en sert
MOD = int(1e9)+7  # classiquement modulo

# je trouve ça plus pratique de raccourcir l'input
input = lambda: sys.stdin.readline().strip()

# Fonctions pour afficher Yes/No, un peu inutile mais bon
def YesNo(b):
    if b:
        print('Yes')
        return True
    else:
        print('No')
        return False

def YESNO(b):
    if b:
        print('YES')
        return True
    print('NO')
    return False

int1 = lambda x: int(x)-1  # Pour passer 1-indexé en 0-indexé

def main():
    N, M = map(int, input().split())
    S = tuple(map(int, input().split()))
    T = tuple(map(int, input().split()))
    # Initialisation DP façon tableau, on aurait pu le faire en compréhension aussi
    dp = []
    for _ in range(N+1):
        dp.append([0]*(M+1))
    # SUM, pas besoin de +2 partout je crois, mais bon, ça marche
    SUM = [[0]*(M+2) for _ in range(N+2)]
    ans = 1
    for s in range(N):
        for t in range(M):
            if S[s]==T[t]:
                dp[s+1][t+1] = SUM[s+1][t+1] + 1
                ans = (ans + dp[s+1][t+1]) % MOD
            else:
                dp[s+1][t+1] = 0  # inutile en Python, mais explicite
            # Préfixe SUM, je ne suis pas sûr d'avoir bien compris cet update mais je garde
            SUM[s+2][t+2] = (SUM[s+1][t+2] + SUM[s+2][t+1] - SUM[s+1][t+1] + dp[s+1][t+1]) % MOD
    print(ans)

if __name__ == "__main__":
    main()