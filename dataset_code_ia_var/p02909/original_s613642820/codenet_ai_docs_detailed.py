def weather_forecast():
    """
    Lit une chaîne de caractères représentant la météo actuelle depuis l'entrée standard
    et affiche la météo prévue en fonction de l'état donné.
    
    Logique :
      - Si la météo est 'Sunny', prédire 'Cloudy'.
      - Si la météo est 'Cloudy', prédire 'Rainy'.
      - Pour toute autre valeur (en pratique, ici 'Rainy'), prédire 'Sunny'.
    """
    # Demande à l'utilisateur de saisir l'état actuel de la météo
    s = input()

    # Vérifie si la météo est "Sunny"
    if s == 'Sunny':
        # Affiche la prévision correspondante
        print("Cloudy")
    # Vérifie si la météo est "Cloudy"
    elif s == 'Cloudy':
        # Affiche la prévision correspondante
        print("Rainy")
    else:
        # Pour toute autre entrée (notamment 'Rainy'), afficher 'Sunny'
        print("Sunny")

# Appelle la fonction principale pour démarrer le programme
weather_forecast()