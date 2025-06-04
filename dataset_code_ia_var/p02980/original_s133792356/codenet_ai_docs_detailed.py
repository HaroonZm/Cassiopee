def main():
    """
    Lit les entiers N et M depuis l'entrée standard et calcule un résultat modulo 998244353
    selon une combinaison de coefficients binomiaux, de puissances et de factorielles.
    Affiche le résultat.
    """
    N, M = map(int, input().split())
    mod = 998244353  # Modulo utilisé pour toutes les opérations

    # Échange N et M pour s'assurer que N <= M, ce qui optimise certaines boucles
    if N > M:
        N, M = M, N

    # Initialisation des tableaux pour les factorielles, les puissances de (M+1), (N+1)
    fact = [0] * (M + 1)   # fact[i] : i!
    powm = [0] * (M + 1)   # powm[i] : (M+1)^i
    pown = [0] * (M + 1)   # pown[i] : (N+1)^i
    fact[0] = powm[0] = pown[0] = 1  # Initialisation de la base des puissances et factorielles

    # Pré-calcul des factorielles et des puissances jusqu'à M inclus
    for i in range(1, M + 1):
        fact[i] = fact[i - 1] * i % mod
        powm[i] = powm[i - 1] * (M + 1) % mod
        pown[i] = pown[i - 1] * (N + 1) % mod

    def mod_pow(n, m):
        """
        Calcule la puissance n^m modulo mod de manière récursive et efficace (exponentiation rapide).

        Args:
            n (int): La base.
            m (int): L'exposant.
        Returns:
            int: Le résultat de n^m % mod.
        """
        if m == 0:
            return 1
        elif m == 1:
            return n % mod
        elif m % 2 == 0:
            tmp = mod_pow(n, m // 2)
            return tmp * tmp % mod
        else:
            tmp = mod_pow(n, m // 2)
            return tmp * tmp % mod * n % mod

    # Pré-calcul des inverses des factorielles modulo mod (nécessaires pour les combinaisons)
    inv_fact = [0] * (M + 1)  # inv_fact[i] : inverse modulaire de fact[i]
    inv_fact[M] = mod_pow(fact[M], mod - 2)  # L'inverse de fact[M] avec le petit théorème de Fermat
    for i in reversed(range(0, M)):
        # inv_fact[i] = inv_fact[i+1] * (i+1) % mod, d'où inv_fact[0] = 1 à la fin
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % mod

    def comb(n, r):
        """
        Calcule la combinaison C(n, r) modulo mod à l'aide des factorielles pré-calculées.

        Args:
            n (int): Le nombre total d'éléments.
            r (int): Le nombre d'éléments à choisir.
        Returns:
            int: La combinaison C(n, r) % mod, ou 0 si r > n ou r < 0.
        """
        if r < 0 or r > n:
            return 0
        return fact[n] * inv_fact[r] % mod * inv_fact[n - r] % mod

    # Calcul de la somme alternée selon la formule donnée
    ans = 0
    for i in range(N + 1):
        # Pour chaque i, on calcule le terme selon la formule :
        # (-1)^i * C(N, i) * C(M, i) * i! * (M+1)^(N-i) * (N+1)^(M-i)
        sign = -1 if (i % 2) else 1  # (-1)^i
        term = (
            sign *
            comb(N, i) *
            comb(M, i) *
            fact[i] %
            mod *
            powm[N - i] % mod *
            pown[M - i] % mod
        )
        ans = (ans + term) % mod  # On veille toujours à ne pas dépasser le modulo

    print(ans)

if __name__ == "__main__":
    main()