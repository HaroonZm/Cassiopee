def get_input_value():
    """
    Demande à l'utilisateur de saisir une valeur entière et la retourne.

    Returns:
        int: La valeur entière saisie par l'utilisateur.
    """
    return int(input())

def get_data_string():
    """
    Demande à l'utilisateur de saisir une chaîne de caractères et la retourne.

    Returns:
        str: La chaîne saisie par l'utilisateur.
    """
    return raw_input()

def find_xx_substring(dato):
    """
    Cherche l'occurrence de la sous-chaîne 'xx' dans la chaîne donnée.

    Args:
        dato (str): La chaîne dans laquelle rechercher.

    Returns:
        int: L'indice de la première occurrence de 'xx', ou -1 si non trouvée.
    """
    return dato.find("xx")

def main():
    """
    Fonction principale qui coordonne la saisie et l'affichage du résultat.

    - Demande à l'utilisateur un entier p.
    - Si p est strictement positif :
        - Demande une chaîne de caractères.
        - Recherche la position de la sous-chaîne 'xx'.
        - Si 'xx' n'est pas trouvée, affiche simplement p.
        - Sinon, affiche la position (1-based) de la première occurrence de 'xx'.
    """
    p = get_input_value()  # Saisie de l'entier par l'utilisateur

    # On traite seulement si p est strictement positif
    if p > 0:
        dato = get_data_string()  # Saisie de la chaîne de caractères
        i = find_xx_substring(dato)  # Recherche de 'xx'
        if i < 0:
            # Affiche p si 'xx' n'est pas trouvée
            print(p)
        else:
            # Affiche la position (en partant de 1) de la première occurrence de 'xx'
            print(i + 1)

if __name__ == "__main__":
    main()