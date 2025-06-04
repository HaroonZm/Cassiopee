def next_weather_state(current_state):
    """
    Détermine l'état météorologique suivant selon l'état actuel.
    
    Args:
        current_state (str): L'état actuel du temps, accepté : 'Sunny', 'Cloudy', ou 'Rainy'.
    
    Returns:
        str: L'état météorologique suivant dans la séquence.
            - 'Sunny' devient 'Cloudy'
            - 'Cloudy' devient 'Rainy'
            - Tout autre état (y compris 'Rainy') devient 'Sunny'
    """
    # Vérifie l'état actuel et retourne l'état suivant approprié
    if current_state == 'Sunny':
        return 'Cloudy'
    elif current_state == 'Cloudy':
        return 'Rainy'
    else:
        return 'Sunny'

def main():
    """
    Fonction principale qui lit une entrée utilisateur,
    détermine l'état météorologique suivant et l'affiche.
    """
    # Demande à l'utilisateur de saisir l'état du temps actuel
    s = input()
    # Détermine et affiche le prochain état du temps
    print(next_weather_state(s))

# Exécute la fonction principale si ce script est exécuté directement
if __name__ == "__main__":
    main()