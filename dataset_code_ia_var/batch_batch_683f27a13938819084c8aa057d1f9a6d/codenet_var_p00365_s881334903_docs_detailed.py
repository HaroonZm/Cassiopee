def read_date():
    """
    Lit une date saisie par l'utilisateur au format 'année mois jour' (ex: '2020 5 15').

    Returns:
        tuple: Un triplet d'entiers correspondant à (année, mois, jour).
    """
    return tuple(map(int, input().split()))

def swap_dates_if_needed(y1, m1, d1, y2, m2, d2):
    """
    Permute deux dates si la première est postérieure à la seconde.

    Args:
        y1, m1, d1: Entiers représentant la première date (année, mois, jour).
        y2, m2, d2: Entiers représentant la seconde date (année, mois, jour).

    Returns:
        tuple: Les dates dans l'ordre croissant (y1, m1, d1, y2, m2, d2).
    """
    # Si la première date est après la seconde, on intervertit les deux dates
    if (y1 > y2) or (y1 == y2 and (m1 > m2 or (m1 == m2 and d1 > d2))):
        return y2, m2, d2, y1, m1, d1
    else:
        return y1, m1, d1, y2, m2, d2

def calculate_years(y1, m1, d1, y2, m2, d2):
    """
    Calcule la différence d'années pleine ou écoulée selon la position des dates.

    Si la date de fin (y2, m2, d2) est postérieure (dans l'année) à la date de début (même mois/jour
    ou après), on ajoute 1 à la différence d'années.
    Sinon, on prend seulement la différence sans ajouter 1.

    Args:
        y1, m1, d1: Entiers représentant la date de début (année, mois, jour).
        y2, m2, d2: Entiers représentant la date de fin (année, mois, jour).

    Returns:
        int: Le nombre d'années écoulées entre les deux dates selon la règle précisée.
    """
    # Si la date de fin est plus avancée dans l'année (mois ou même mois mais jour plus tard)
    if m1 < m2 or (m1 == m2 and d1 <= d2):
        return y2 - y1 + 1
    else:
        return y2 - y1

def main():
    """
    Point d'entrée du programme. Lis deux dates, les ordonne puis calcule et affiche
    le nombre d'années écoulées selon la logique décrite.
    """
    # Lecture de la première date de l'utilisateur
    y1, m1, d1 = read_date()
    # Lecture de la deuxième date de l'utilisateur
    y2, m2, d2 = read_date()
    # S'assurer que la première date est antérieure ou égale à la seconde
    y1, m1, d1, y2, m2, d2 = swap_dates_if_needed(y1, m1, d1, y2, m2, d2)
    # Calcul du nombre d'années écoulées et affichage
    print(calculate_years(y1, m1, d1, y2, m2, d2))

if __name__ == "__main__":
    main()