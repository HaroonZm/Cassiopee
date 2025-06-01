def calculate_min_cost(num_cases):
    """
    Calcule et affiche le coût minimum pour chaque cas parmi plusieurs cas donnés.

    Pour chaque cas, la fonction lit quatre entiers : x, y, b, p.
    Elle calcule deux coûts différents :
    - cost1 : coût direct sans réduction.
    - cost2 : coût avec des prix minimums et une réduction de 20%.

    La fonction imprime le coût minimum entre cost1 et cost2 pour chaque cas.

    Args:
        num_cases (int): Le nombre de cas à traiter.
    """
    for _ in range(num_cases):
        # Lecture des valeurs x, y, b, p séparées par un espace et conversion en entiers
        x, y, b, p = map(int, raw_input().split())

        # Calcul du coût simple sans réduction : prix b multiplié par x + prix p multiplié par y
        cost1 = x * b + y * p

        # Calcul du coût avec prix minimum et remise de 20%
        # Les prix sont au moins 5 pour b et 2 pour p, puis réduction de 20% appliquée
        cost2 = (x * max(b, 5) + y * max(p, 2)) * 0.8

        # Affichage du coût minimum entre cost1 et cost2, formaté en entier
        print "%d" % min(cost1, cost2)


if __name__ == "__main__":
    # Lecture du nombre de cas à traiter
    num_cases = int(raw_input())
    # Exécution de la fonction principale de calcul des coûts
    calculate_min_cost(num_cases)