def calculate_time_sum(a: int, b: int) -> int:
    """
    Calcule la somme de deux entiers représentant des heures de l'horloge (format 24 heures)
    et ajuste le résultat si la somme atteint ou dépasse 24, pour simuler une addition d'heure
    sur une horloge (modulo 24).

    Args:
        a (int): Première valeur horaire (entre 0 et 23).
        b (int): Deuxième valeur horaire (entre 0 et 23).

    Returns:
        int: Résultat de l'addition sur l'horloge, après ajustement modulo 24.
    """
    ans = a + b  # Calcule la somme des deux heures
    if ans < 24:
        # Si la somme est inférieure à 24, le résultat est simplement la somme
        return ans
    else:
        # Si la somme est 24 ou plus, on soustrait 24 pour "revenir à zéro" sur l'horloge
        return ans - 24

def main():
    """
    Fonction principale du script.
    Demande à l'utilisateur de saisir deux entiers séparés par un espace,
    représentant des heures, puis affiche le résultat de leur addition modulo 24.
    """
    # Lecture de deux entiers depuis l'entrée standard, séparés par un espace
    a, b = map(int, input().split())
    # Calcul et affichage du résultat en utilisant la fonction calculate_time_sum
    print(calculate_time_sum(a, b))

# Appel de la fonction principale si le script est exécuté directement
if __name__ == '__main__':
    main()