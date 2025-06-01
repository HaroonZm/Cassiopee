def josephus_winner(n, m):
    """
    Calcule le gagnant du jeu 'ヨセフのおイモ' (problème de Josephus).

    Args:
        n (int): Nombre total de participants.
        m (int): Intervalle du participant qui est exclu à chaque tour.

    Retour:
        int: Le numéro du participant gagnant (1-indexé).
    """
    # La position gagnante dans une configuration de 1 seule personne est 0 (indexé à 0)
    winner = 0
    # On calcule itérativement la position gagnante pour chaque nombre croissant de participants
    for i in range(2, n + 1):
        winner = (winner + m) % i
    # La numérotation dans l'énoncé commence à 1, on ajoute donc 1
    return winner + 1


def main():
    import sys

    for line in sys.stdin:
        # Traiter chaque ligne non vide
        if line.strip():
            n, m = map(int, line.split())
            # Condition de fin d'entrée
            if n == 0 and m == 0:
                break
            # Afficher le gagnant pour chaque cas
            print(josephus_winner(n, m))


if __name__ == "__main__":
    main()