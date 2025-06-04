def process_ball_moves(n, m, moves):
    """
    Simule le déplacement des balles entre des boîtes selon des règles spécifiques.

    Args:
        n (int): Nombre de boîtes.
        m (int): Nombre de déplacements.
        moves (list of tuple): Liste contenant les mouvements. Chaque mouvement est
            un tuple (x, y) indiquant le déplacement d'une balle de la boîte x à la boîte y (indices 0-based).

    Returns:
        int: Nombre de boîtes contenant au moins une balle rouge à la fin des déplacements.
    """
    # Initialise la liste pour savoir si une boîte contient une balle rouge (1 si oui, 0 sinon)
    redball = [0] * n
    redball[0] = 1  # Seule la première boîte contient initialement une balle rouge

    # Initialise la liste pour compter le nombre de balles dans chaque boîte (initialement 1 par boîte)
    ball_cnt = [1] * n

    # Parcourt chaque mouvement de balle
    for x, y in moves:
        # Si la boîte source x n’a qu'une seule balle ET qu’elle est rouge
        if ball_cnt[x] == 1 and redball[x] == 1:
            redball[x] = 0       # La boîte x perd la balle rouge
            redball[y] = 1       # La boîte y reçoit une balle rouge

        # Si la boîte x a plusieurs balles et contient une balle rouge
        elif ball_cnt[x] > 1 and redball[x] == 1:
            redball[y] = 1       # La boîte y reçoit aussi une balle rouge

        # Met à jour les compteurs de balles après le déplacement
        ball_cnt[x] -= 1
        ball_cnt[y] += 1

    # Compte et retourne le nombre de boîtes contenant au moins une balle rouge
    return redball.count(1)


def main():
    """
    Fonction principale.
    Lit l'entrée utilisateur, exécute la simulation, puis affiche le résultat.
    """
    # Lecture du nombre de boîtes et du nombre de déplacements
    n, m = list(map(int, input().split()))

    # Lecture de la liste des mouvements
    moves = []
    for _ in range(m):
        x, y = list(map(int, input().split()))
        # Convertit en indices 0-based et ajoute à la liste
        moves.append((x-1, y-1))

    # Exécute la simulation et affiche le résultat
    result = process_ball_moves(n, m, moves)
    print(result)


if __name__ == '__main__':
    main()