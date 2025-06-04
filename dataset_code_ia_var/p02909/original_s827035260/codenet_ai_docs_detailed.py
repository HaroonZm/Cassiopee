def weather_transition():
    """
    Lit une condition météorologique depuis l'entrée standard et affiche l'état météorologique suivant selon la règle suivante :
    - 'Sunny' devient 'Cloudy'
    - 'Cloudy' devient 'Rainy'
    - 'Rainy' devient 'Sunny'

    Si l'entrée n'est pas précisément l'une des options attendues, elle sera considérée comme 'Cloudy' et produira 'Rainy'.
    """
    # Demander à l'utilisateur d'entrer la condition météorologique actuelle
    s = input()
    
    # Sélectionner et afficher la prochaine météo selon la règle définie
    if s == 'Sunny':
        # Si c'est ensoleillé, il fera nuageux ensuite
        print('Cloudy')
    elif s == 'Rainy':
        # Si c'est pluvieux, il fera ensuite ensoleillé
        print('Sunny')
    else:
        # Sinon (typiquement si c'est 'Cloudy'), il fera pluvieux ensuite
        print('Rainy')

# Appeler la fonction principale pour exécuter le code
weather_transition()