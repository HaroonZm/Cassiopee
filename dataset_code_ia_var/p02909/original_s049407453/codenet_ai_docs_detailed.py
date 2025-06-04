def get_next_weather(current_weather):
    """
    Prend une condition météorologique en tant que chaîne de caractères et renvoie la prochaine condition logique.
    
    Paramètres:
        current_weather (str): La condition météorologique actuelle ("Sunny", "Cloudy" ou autre).
        
    Retourne:
        str: La prochaine condition météorologique ("Cloudy" si actuelle est "Sunny", "Rainy" si actuelle est "Cloudy", ou "Sunny" sinon).
    """
    # Initialisation de la variable avec la valeur par défaut "Sunny"
    next_weather = 'Sunny'
    
    # Si la condition actuelle est "Sunny", la prochaine est "Cloudy"
    if current_weather == 'Sunny':
        next_weather = 'Cloudy'
    # Si la condition actuelle est "Cloudy", la prochaine est "Rainy"
    elif current_weather == 'Cloudy':
        next_weather = 'Rainy'
    # Pour toute autre condition, next_weather reste à la valeur par défaut "Sunny"
    
    return next_weather

def main():
    """
    Fonction principale qui demande à l'utilisateur de saisir la condition météorologique
    puis affiche la prochaine condition.
    """
    # Lecture de l'entrée utilisateur (par exemple : "Sunny", "Cloudy", "Rainy")
    user_input = input()
    
    # Appel de la fonction pour obtenir la prochaine condition selon l'entrée utilisateur
    result = get_next_weather(user_input)
    
    # Affichage de la prochaine condition météorologique
    print(result)

# Appel du point d'entrée du programme
if __name__ == "__main__":
    main()