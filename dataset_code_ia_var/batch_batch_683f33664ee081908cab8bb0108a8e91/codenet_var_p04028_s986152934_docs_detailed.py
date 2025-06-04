def compute_dp_table(N, S):
    """
    Calcule le nombre de façons d'obtenir une certaine configuration
    basée sur la chaîne S, en utilisant une programmation dynamique.

    Args:
        N (int): Taille du tableau ou nombre d'opérations à considérer.
        S (str): Chaîne représentant l'état initial ou le motif cible.

    Returns:
        int: Nombre de façons d'obtenir la configuration après N étapes,
            modulo 10**9 + 7.
    """
    mod = 10 ** 9 + 7  # Modulo pour éviter les débordements d'entiers
    M = len(S)         # Longueur de la chaîne S

    # Initialisation de la table DP :
    # DP[i][j] représente le nombre de façons d'obtenir un état où
    # j est la taille courante (ou un certain compteur) après i étapes.
    DP = [[0] * (N + 1) for _ in range(N + 1)]

    # Il y a exactement une façon d'avoir une taille 0 après 0 étapes.
    DP[0][0] = 1

    # Remplissage de la table DP
    for i in range(1, N + 1):
        for j in range(N + 1):
            if 0 < j < N:
                # Cas général : l'état j peut provenir de j-1 (par ajout)
                # ou de j+1 (par suppression, avec un facteur 2)
                DP[i][j] = DP[i - 1][j - 1] + 2 * DP[i - 1][j + 1]
            elif j == 0:
                # Cas particulier : bas de la bande, pas de j-1 possible
                DP[i][j] = DP[i - 1][j] + 2 * DP[i - 1][j + 1]
            else:
                # j == N : bord supérieur, ne peut venir que de j-1
                DP[i][j] = DP[i - 1][j - 1]
            # Prend le modulo pour chaque mise à jour
            DP[i][j] %= mod

    # Le résultat est le nombre de façons d’obtenir l’état de taille M après N étapes
    return DP[N][M]


def main():
    """
    Fonction principale pour lire les entrées,
    appeler le calcul, et afficher le résultat.
    """
    N = int(input())  # Lecture de l'entier N
    S = input()       # Lecture du motif ou état sous forme de chaîne

    # Calcul du résultat
    result = compute_dp_table(N, S)
    print(result)

if __name__ == "__main__":
    main()