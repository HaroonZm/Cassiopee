def get_weekday_from_offset(offset):
    """
    Calcule le jour de la semaine correspondant à un décalage fourni.

    Paramètres :
    offset (int): Entier représentant le nombre de jours de décalage.

    Retourne :
    str: Nom abrégé du jour de la semaine correspondant ('mon', 'tue', etc.).
    """
    # Liste des jours de la semaine commençant par lundi
    table = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    # Ajoute un décalage de 3, puis utilise modulo 7 pour rester dans la plage valide
    index = (offset + 3) % 7
    # Retourne le jour correspondant après application du décalage
    return table[index]

if __name__ == "__main__":
    # Demande à l'utilisateur de saisir un entier représentant le décalage de jours
    X = int(input())
    # Calcule et affiche le jour de la semaine correspondant
    print(get_weekday_from_offset(X))