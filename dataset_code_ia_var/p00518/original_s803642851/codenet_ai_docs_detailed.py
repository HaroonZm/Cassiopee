def initialize_dp_table(N):
    """
    Initialise le tableau dp utilisé pour la programmation dynamique.

    Args:
        N (int): La longueur de la chaîne d'entrée.

    Returns:
        list: Un tableau 2D de dimensions (N+1) x 8 initialisé à 0.
    """
    return [[0 for _ in range(8)] for _ in range(N + 1)]

def update_dp_j(dp, i):
    """
    Met à jour le tableau dp à l'étape i+1 quand la lettre 'J' est rencontrée.

    Args:
        dp (list): Le tableau de programmation dynamique.
        i (int): L'indice actuel de la chaîne.
    """
    dp[i + 1][1] = dp[i][1] + dp[i][2] + dp[i][3] + dp[i][4]
    dp[i + 1][2] = dp[i][1] + dp[i][2] + dp[i][3] + dp[i][4] + dp[i][5] + dp[i][6]
    dp[i + 1][3] = dp[i][1] + dp[i][2] + dp[i][3] + dp[i][4] + dp[i][6] + dp[i][7]
    dp[i + 1][4] = dp[i][1] + dp[i][2] + dp[i][3] + dp[i][4] + dp[i][5] + dp[i][6] + dp[i][7]
    dp[i + 1][5] = 0
    dp[i + 1][6] = 0
    dp[i + 1][7] = 0

def update_dp_o(dp, i):
    """
    Met à jour le tableau dp à l'étape i+1 quand la lettre 'O' est rencontrée.

    Args:
        dp (list): Le tableau de programmation dynamique.
        i (int): L'indice actuel de la chaîne.
    """
    dp[i + 1][1] = 0
    dp[i + 1][2] = dp[i][1] + dp[i][2] + dp[i][3] + dp[i][4] + dp[i][5] + dp[i][6]
    dp[i + 1][3] = 0
    dp[i + 1][4] = dp[i][1] + dp[i][2] + dp[i][3] + dp[i][4] + dp[i][5] + dp[i][6] + dp[i][7]
    dp[i + 1][5] = dp[i][2] + dp[i][4] + dp[i][5] + dp[i][6]
    dp[i + 1][6] = dp[i][2] + dp[i][3] + dp[i][4] + dp[i][5] + dp[i][6] + dp[i][7]
    dp[i + 1][7] = 0

def update_dp_i(dp, i):
    """
    Met à jour le tableau dp à l'étape i+1 quand la lettre 'I' est rencontrée.

    Args:
        dp (list): Le tableau de programmation dynamique.
        i (int): L'indice actuel de la chaîne.
    """
    dp[i + 1][1] = 0
    dp[i + 1][2] = 0
    dp[i + 1][3] = dp[i][1] + dp[i][2] + dp[i][3] + dp[i][4] + dp[i][6] + dp[i][7]
    dp[i + 1][4] = dp[i][1] + dp[i][2] + dp[i][3] + dp[i][4] + dp[i][5] + dp[i][6] + dp[i][7]
    dp[i + 1][5] = 0
    dp[i + 1][6] = dp[i][2] + dp[i][3] + dp[i][4] + dp[i][5] + dp[i][6] + dp[i][7]
    dp[i + 1][7] = dp[i][3] + dp[i][4] + dp[i][6] + dp[i][7]

def main():
    """
    Fonction principale du programme.
    Lit l'entrée, initialise le tableau dp et applique la dynamique
    pour obtenir le résultat final.
    """
    # Lecture de la longueur de la chaîne d'entrée
    N = int(input())

    # Lecture de la chaîne de caractères (composée de 'J', 'O', ou 'I')
    C = input()

    # Initialisation de la table de DP.
    dp = initialize_dp_table(N)

    # Condition initiale : avant tout caractère, seul dp[0][1] vaut 1 (au début d'un état)
    dp[0][1] = 1

    # Parcours de chaque caractère de la chaîne d'entrée
    for i in range(N):
        if C[i] == "J":
            update_dp_j(dp, i)
        if C[i] == 'O':
            update_dp_o(dp, i)
        if C[i] == 'I':
            update_dp_i(dp, i)

    # Calcul du résultat final : somme des états possibles modulo 10007
    result = sum(dp[N][j] for j in range(1, 8)) % 10007
    print(result)

if __name__ == "__main__":
    main()