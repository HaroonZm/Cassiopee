def get_weekday(x):
    """
    Calcule et retourne le jour de la semaine correspondant à un nombre donné.
    La semaine commence par 'mon' (lundi) en position 0.
    Le décalage de 3 correspond à un ajustement pour aligner l'entrée utilisateur 
    avec le bon jour de la semaine, puis applique un modulo 7 pour garantir que 
    l'index reste dans le tableau des jours.

    Args:
        x (int): Un entier représentant un numéro de jour.

    Returns:
        str: L'abréviation anglaise à trois lettres du jour correspondant.
    """
    # Liste des jours de la semaine commençant par lundi
    days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
    # Calcule l'index du jour selon la formule donnée et utilise le modulo pour rester dans les bornes du tableau
    day_index = (x + 3) % 7
    return days[day_index]


def main():
    """
    Fonction principale qui lit un entier depuis l'entrée standard,
    puis affiche l'abbréviation du jour de la semaine correspondante.
    """
    # Demande à l'utilisateur de saisir un nombre entier
    x = int(input("Entrez un entier : "))
    # Obtient et affiche le jour de la semaine correspondant
    print(get_weekday(x))


if __name__ == "__main__":
    main()