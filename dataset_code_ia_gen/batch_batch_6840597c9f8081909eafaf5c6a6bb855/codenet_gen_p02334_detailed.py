MOD = 10**9 + 7

def modinv(a, m=MOD):
    # Calcule l'inverse modulaire de a modulo m par exponentiation rapide (Petit théorème de Fermat)
    return pow(a, m - 2, m)

def comb(n, k):
    # Calcule C(n,k) modulo MOD en utilisant une approche sans pré-calcul
    # Factorielle modulaire est calculée à la volée ici pour éviter mémoire élevée pour n=1000 ce qui est acceptable
    if k > n or k < 0:
        return 0
    numerator = 1
    denominator = 1
    # calcule n*(n-1)*...*(n-k+1)
    for i in range(k):
        numerator = (numerator * (n - i)) % MOD
    # calcule k!
    for i in range(1, k + 1):
        denominator = (denominator * i) % MOD
    return (numerator * modinv(denominator, MOD)) % MOD

def main():
    # Lis les entrées
    n, k = map(int, input().split())
    # Le problème demande le nombre de façons de distribuer n boules indistinguables dans k boites distinguables
    # Chaque boite peut contenir 0 ou plus de boules
    # C'est un problème classique en combinatoire: "Répartition de n objets indistinguables dans k boites distinguables"
    # La formule est C(n+k-1, k-1)
    # On renvoie le résultat modulo 10^9 + 7
    result = comb(n + k - 1, k - 1)
    print(result)

if __name__ == "__main__":
    main()