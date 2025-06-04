def process_input():
    """
    Exécute une boucle interactive qui traite différents cas d'utilisation.
    À chaque itération :
    - Lit une valeur entière 'v' (la valeur cible ou seuil). Si 'v' vaut 0, le programme se termine.
    - Pour le cas courant, lit douze paires de valeurs entières 'm' (mesures) et 'n' (normes) :
        * À chaque mois, met à jour un cumul 'c' en ajoutant (m - n).
        * Dès que 'c' atteint ou dépasse 'v' pour la première fois, le numéro du mois est enregistré dans 'f'.
    - À la fin des 12 mois, affiche le premier mois où le seuil est atteint/surpassé ('f'), sinon affiche "NA".
    """
    while True:
        # Lecture de l'entrée pour la valeur cible 'v'
        v = int(input())
        if v == 0:
            # Arrêt du programme si la saisie est 0
            break

        c = 0  # Cumul des différences sur 12 mois
        f = 0  # Mois où le cumul atteint au moins 'v' pour la première fois
        for i in range(1, 13):
            # Lecture de la paire [m, n] séparée par un espace
            m, n = [int(x) for x in input().split()]
            c += m - n  # Mise à jour du cumul du mois courant

            if f == 0 and c >= v:
                # Si c atteint ou dépasse 'v' pour la première fois, on retient le mois courant
                f = i

        if f > 0:
            print(f)
        else:
            print("NA")

if __name__ == "__main__":
    process_input()