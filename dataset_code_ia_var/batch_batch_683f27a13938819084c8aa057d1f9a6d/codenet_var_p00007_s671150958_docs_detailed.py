import math

def calculate_future_value(years, initial_value=100000, rate=0.05, rounding=1000):
    """
    Calcule la valeur future d'un investissement avec intérêts composés,
    en arrondissant chaque année le résultat à l'entier supérieur du palier de 'rounding'.

    Args:
        years (int): Nombre d'années d'investissement.
        initial_value (float or int, optional): Valeur de départ de l'investissement. Par défaut à 100000.
        rate (float, optional): Taux d'intérêt composé annuel. Par défaut à 0.05 (5%).
        rounding (int, optional): Palier utilisé pour l'arrondi supérieur. Par défaut à 1000.

    Returns:
        int: Valeur finale arrondie à l'entier supérieur du palier de 'rounding' après la période.
    """
    # Initialisation de la valeur de départ
    future_value = initial_value
    
    # Pour chaque année d'investissement
    for _ in range(years):
        # On applique le taux d'intérêt annuel
        future_value *= (1 + rate)
        # On arrondit au palier supérieur le plus proche de 'rounding'
        future_value = int(math.ceil(future_value / rounding) * rounding)
    
    # On retourne la valeur finale arrondie
    return future_value

if __name__ == '__main__':
    # Lecture du nombre d'années depuis l'entrée utilisateur
    number_of_years = int(input())
    # Calcul de la valeur future avec les paramètres par défaut
    result = calculate_future_value(number_of_years)
    # Affichage de la valeur calculée
    print(result)