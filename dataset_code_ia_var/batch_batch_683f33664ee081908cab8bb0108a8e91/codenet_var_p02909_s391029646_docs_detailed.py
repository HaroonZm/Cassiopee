def get_next_weather(current_weather):
    """
    Prend la condition météorologique actuelle en entrée et retourne la condition suivante selon l'ordre :
    'Sunny' -> 'Cloudy' -> 'Rainy' -> 'Sunny' (cycle).

    Paramètres:
        current_weather (str): La condition météorologique actuelle, doit être l'une de ['Sunny', 'Cloudy', 'Rainy'].

    Retourne:
        str: La prochaine condition météorologique dans l'ordre cyclique.

    Exemple:
        >>> get_next_weather('Sunny')
        'Cloudy'
    """
    # Définir la liste ordonnée des conditions météorologiques
    Ts = ['Sunny', 'Cloudy', 'Rainy']
    # Parcourir chaque indice dans la liste des conditions
    for i in range(3):
        # Si la condition actuelle correspond à celle de l'indice i
        if Ts[i] == current_weather:
            # Retourner la condition suivante, en utilisant le modulo 3 pour revenir au début si nécessaire
            return Ts[(i+1)%3]
    # Si la condition n'a pas été trouvée, retourner None ou éventuellement lancer une exception
    return None

def main():
    """
    Fonction principale qui lit l'entrée de l'utilisateur, détermine et affiche la prochaine condition météorologique.
    """
    # Lire l'entrée utilisateur et retirer les espaces ou les sauts de ligne en fin
    Ss = input().rstrip()
    # Utiliser la fonction get_next_weather pour déterminer la prochaine condition
    next_weather = get_next_weather(Ss)
    # Afficher la condition suivante si elle existe
    if next_weather:
        print(next_weather)
    else:
        print("Condition météorologique non reconnue.")

if __name__ == "__main__":
    main()