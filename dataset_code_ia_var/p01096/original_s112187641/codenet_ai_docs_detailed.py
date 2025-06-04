def solve(n, w):
    """
    Résout le problème de partitionnement optimal sur une liste de poids w de longueur n.
    Elle calcule la longueur maximale de séquences supprimables selon une règle définie : 
    un segment [l, r) peut être supprimé si sa longueur est pair et
    - soit il correspond à deux points extrêmes effaçables (différence <= 1)
      et le segment interne l+1 à r-1 est totalement supprimable,
    - soit le segment se subdivise en deux segments supprimables.

    Args:
        n (int): Longueur de la liste des poids.
        w (List[int]): Liste des poids.

    Returns:
        int: La taille maximale du segment supprimable.
    """
    # dp[l][r] stocke la taille maximale de sous-séquences supprimables dans [l, r)
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    # kukan est la longueur du segment
    for kukan in range(2, n + 1):
        # l est la borne gauche du segment
        for l in range(0, n + 1 - kukan):
            r = l + kukan  # r est la borne droite (exclue) du segment
            # On vérifie si le segment [l, r) a une longueur paire 
            if (kukan - 2) % 2 == 0:
                # Vérifie la règle de suppression : 
                # - extrémités rapprochées (différence <= 1)
                # - le sous-segment interne peut être entièrement supprimé
                if abs(w[l] - w[r - 1]) <= 1 and dp[l + 1][r - 1] == r - l - 2:
                    dp[l][r] = dp[l + 1][r - 1] + 2
                    continue  # On a trouvé un segment total supprimable

            # Sinon, on essaie toutes les partitions possibles dans [l, r)
            for i in range(l + 1, r):
                if dp[l][r] < (dp[l][i] + dp[i][r]):
                    dp[l][r] = dp[l][i] + dp[i][r]

    return dp[0][n]

def main():
    """
    Fonction principale :
    - Lit un entier n depuis l'entrée standard, puis des séquences de n entiers,
    - Applique la fonction solve pour chaque séquence, affiche le résultat.
    - S'arrête lorsque n == 0.
    """
    n = int(input())
    while n != 0:
        w = list(map(int, input().split()))
        print(solve(n, w))
        n = int(input())

# Appeler la fonction principale si ce script est exécuté directement
if __name__ == "__main__":
    main()