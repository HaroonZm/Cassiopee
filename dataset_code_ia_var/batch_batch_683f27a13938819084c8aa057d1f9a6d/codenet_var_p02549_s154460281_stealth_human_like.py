import sys
input = sys.stdin.readline

def main():
    n, k = map(int, input().split())
    mod = 998244353

    dp = [0 for _ in range(n)]

    segments = []
    for idx in range(k):
        segments.append(tuple(map(int, input().split())))
    segments.sort()

    # C'est ici que tout commence !
    dp[0] = 1
    cache = [0]*k  # J'ai mis ce nom, mais bof...

    for i in range(1, n):
        acc = 0
        for j in range(k):
            l, r = segments[j]
            # On essaie d'ajouter... ou de retirer, je ne sais plus trop pourquoi :)
            if i - l >= 0:
                cache[j] = (cache[j] + dp[i-l])  # On fait la somme
            if i - r - 1 >= 0:
                cache[j] -= dp[i-r-1]  # On retire car hors de portée

            # En vrai je ne suis pas sûr de la logique ici, mais ça avait l'air de marcher...
        dp[i] = (sum(cache)) % mod  # Addition pas très optimisée
        # J'espère que le modulo est bien placé :/

    result = dp[-1]  # Je préfère utiliser -1, c'est plus "pythonic", non ?
    print(result)

if __name__ == "__main__":
    main()