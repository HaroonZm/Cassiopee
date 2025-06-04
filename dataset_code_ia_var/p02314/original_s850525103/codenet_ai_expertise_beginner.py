import sys

def main():
    # On lit les entrées
    N_W = input().split()
    N = int(N_W[0])
    W = int(N_W[1])
    coins = list(map(int, input().split()))

    # On initialise la liste dp avec de grandes valeurs
    dp = [100000] * 100000
    dp[0] = 0

    # On fait la programmation dynamique
    for i in coins:
        for j in range(100000):
            if j - i >= 0:
                dp[j] = min(dp[j], dp[j - i] + 1)
    print(dp[N])

if __name__ == "__main__":
    main()