def read_input():
    """
    Lit les entrées standard pour obtenir la taille de la séquence et la séquence elle-même.

    Returns:
        tuple: Un entier N représentant la taille de la séquence,
               et une liste C de N entiers représentant la séquence.
    """
    N = int(input())
    C = [int(input()) for _ in range(N)]
    return N, C

def initialize_dp_arrays(N, max_C):
    """
    Initialise les tableaux nécessaires pour le calcul dynamique.

    Args:
        N (int): Taille de la séquence.
        max_C (int): Valeur maximale parmi les éléments de la séquence C.

    Returns:
        tuple: 
            dp (list): Tableau pour stocker le nombre de façons d'atteindre chaque position.
            r (list): Tableau pour stocker le prochain indice valide pour chaque position.
            prev (list): Tableau pour stocker le dernier indice où chaque valeur C[i] est apparue.
    """
    dp = [0 for _ in range(N)]   # Nombre de façons d'arriver à chaque index
    dp[0] = 1                   # Il y a une seule façon d'être au début
    r = [-1 for _ in range(N)]   # Pour chaque position, stocke le prochain indice valide (initialisé à -1)
    prev = [-1 for _ in range(max_C + 1)] # Dernière occurrence de chaque valeur de C
    return dp, r, prev

def build_next_indices(N, C, r, prev):
    """
    Remplit le tableau r où, pour chaque position, on stocke l'indice du prochain
    même nombre (C[i]) qui n'est pas consécutif.

    Args:
        N (int): Taille de la séquence.
        C (list): Séquence des valeurs.
        r (list): Tableau à remplir avec les indices suivants valides.
        prev (list): Tableau maintenant la dernière position connue pour chaque valeur.
    """
    for i in range(N):
        # Si la valeur C[i] est déjà apparue et pas à la position précédente,
        # alors on met à jour r à la dernière position où elle est apparue.
        if prev[C[i]] != -1 and prev[C[i]] + 1 != i:
            r[prev[C[i]]] = i
        # On met à jour la dernière occurrence de C[i]
        prev[C[i]] = i

def compute_dp(N, r, dp, MOD):
    """
    Calcule dynamiquement, pour chaque position, le nombre de façons d'y arriver, 
    avec la contrainte que deux mêmes couleurs non consécutives autorisent une transition directe.

    Args:
        N (int): Taille de la séquence.
        r (list): Tableau des indices suivants valides.
        dp (list): Tableau des nombres de façons (modifié sur place).
        MOD (int): Modulo pour éviter les débordements.

    Returns:
        list: Tableau dp mis à jour.
    """
    for i in range(N - 1):
        # Si un saut non consécutif est possible vers r[i], on additionne le nombre de façons
        if r[i] != -1:
            dp[r[i]] += dp[i]
            dp[r[i]] %= MOD
        # Ajoute le nombre de façons d'arriver à i pour arriver à i + 1 (prochain élément consécutif)
        dp[i + 1] += dp[i]
        dp[i + 1] %= MOD
    return dp

def main():
    """
    Fonction principale pour résoudre le problème :
    Compte le nombre de façons d'atteindre la fin de la séquence en autorisant à chaque étape :
    - de continuer à l'élément suivant;
    - de "sauter" à un élément de même valeur non consécutif.
    Toutes les réponses sont calculées modulo 10**9 + 7.
    """
    MOD = 10**9 + 7

    # Lecture de l'entrée utilisateur
    N, C = read_input()

    # Initialisation des tableaux
    dp, r, prev = initialize_dp_arrays(N, max(C))

    # Construction du tableau d'indices de saut possible
    build_next_indices(N, C, r, prev)

    # Calcul dynamique des manières d'atteindre chaque position
    dp = compute_dp(N, r, dp, MOD)

    # Affichage du résultat final modulo MOD
    print(dp[N-1] % MOD)

if __name__ == '__main__':
    main()