def compute_special_value(H, W, K):
    """
    Calcule une valeur basée sur les entiers H, W, K selon une formule combinatoire.
    
    Paramètres
    ----------
    H : int
        Nombre d'éléments dans la dimension "hauteur"
    W : int
        Nombre d'éléments dans la dimension "largeur"
    K : int
        Un entier utilisé dans le calcul combinatoire
    
    Retourne
    -------
    int
        Le résultat du calcul modulo P (10**9 + 7)
    """
    P = 10**9 + 7              # Modulo utilisé pour tous les calculs afin d'éviter les débordements
    N = H + W                  # Somme des dimensions, utilisée à plusieurs endroits dans la formule
    
    # Calcul de la première partie de la formule :
    # K*(K+3)//2 calcule la somme (K^2 + 3K)/2
    # (K^3-K)//3 calcule (K^3 - K)/3
    # H*W est multiplié pour pondérer par la surface
    # pow(base, exp, mod) calcule (base^exp) % mod ; ici, inverse modulaire de (N*N-N)
    part1 = K * (K + 3) // 2
    part2 = ((K**3 - K) // 3) * H * W
    denominator = N * N - N
    inv_denominator = pow(denominator, P-2, P)  # Inverse modulaire, utilisé pour diviser sous modulo P
    
    x = (part1 + part2 * inv_denominator) % P   # On additionne les deux parties, puis réduit sous modulo P
    
    # Multiplication itérative : pour chaque i de 0 à K-1, multiplie x par (N-i) sous modulo P
    for i in range(K):
        x = (x * (N - i)) % P
    
    return x

if __name__ == "__main__":
    # Lecture de l'entrée utilisateur : trois entiers séparés par des espaces
    H, W, K = map(int, input().split())
    # Appel de la fonction de calcul et affichage du résultat
    print(compute_special_value(H, W, K))