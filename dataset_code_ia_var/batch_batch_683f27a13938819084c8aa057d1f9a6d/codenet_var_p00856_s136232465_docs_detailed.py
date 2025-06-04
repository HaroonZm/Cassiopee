def parse_input():
    """
    Lit une ligne d'entrée, la découpe en quatre entiers, puis retourne ces entiers.

    Returns:
        tuple: Un tuple (N, T, L, B) où
               N : la position cible sur le plateau (int),
               T : le nombre maximal de tours (int),
               L : le nombre de cases 'Lose' (int),
               B : le nombre de cases 'Back' (int).
    """
    return map(int, raw_input().split(" "))


def collect_positions(count):
    """
    Lit 'count' lignes d'entrées et retourne un set des positions correspondantes.

    Args:
        count (int): Nombre de positions à lire.

    Returns:
        set: Ensemble des entiers représentant les positions saisies.
    """
    return set([int(raw_input()) for _ in range(count)])


def initialize_dp_table(turns, length):
    """
    Crée un tableau dynamique initialisé à zéro.
    Dimensions: (turns+1) x (length+1)

    Args:
        turns (int): Nombre maximal de tours (pour la première dimension).
        length (int): Position cible sur le plateau (pour la deuxième dimension).

    Returns:
        list: Tableau dynamique dp[turn][position] initialisé à 0.
    """
    return [[0 for _ in range(length + 1)] for _ in range(turns + 1)]


def compute_probability(N, T, Lose, Back):
    """
    Calcule la probabilité de terminer le jeu en moins ou égal à T tours,
    compte tenu des cases de perte ('Lose') et de retour ('Back').

    Args:
        N (int): Position d'arrivée sur le plateau.
        T (int): Nombre maximal de tours disponibles.
        Lose (set): Ensemble des positions qui déclenchent une perte de tour.
        Back (set): Ensemble des positions qui renvoient à la case départ.

    Returns:
        float: Probabilité totale d'atteindre la case N en [1, T] tours.
    """
    # Initialisation du tableau dynamique pour stocker les probabilités.
    dp = initialize_dp_table(T, N)
    dp[0][0] = 1  # On commence en case 0, avec proba 1 à tour 0.

    # Simulation pour chaque tour et chaque position possible
    for i in range(T):
        for j in range(N):
            # Calcul du tour à utiliser si on arrive d'une case 'Lose'
            rank = i - 1 if j in Lose else i
            # Parcours des résultats possibles d'un lancer de dé (1 à 6)
            for d in range(1, 7):
                next_pos = j + d
                # Gestion du dépassement du plateau (rebond)
                if next_pos > N:
                    next_pos = N - (next_pos - N)
                # Case spéciale 'Back': retour à zéro
                if next_pos in Back:
                    dp[i + 1][0] += dp[rank][j] / 6.0
                else:
                    dp[i + 1][next_pos] += dp[rank][j] / 6.0
    # Somme des probabilités d'atteindre N en au moins un tour (de 1 à T)
    return sum(dp[i][N] for i in range(1, T + 1))


def main():
    """
    Point d'entrée principal du programme. Lit les différentes configurations de jeu,
    appelle le calculateur de probabilité, puis affiche le résultat formaté.
    Arrête le traitement lors de la ligne de terminaison "0 0 0 0".
    """
    while True:
        N, T, L, B = parse_input()
        if N == T == L == B == 0:
            break
        Lose = collect_positions(L)
        Back = collect_positions(B)
        probability = compute_probability(N, T, Lose, Back)
        print "%6f" % probability


# Exécution du programme principal
main()