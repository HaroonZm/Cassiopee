def has_minimum_length(password, length=6):
    """
    Vérifie si le mot de passe a une longueur minimale spécifiée.

    Args:
        password (str): Le mot de passe à vérifier.
        length (int): La longueur minimale requise (par défaut 6).

    Returns:
        bool: True si le mot de passe a une longueur >= length, sinon False.
    """
    return len(password) >= length

def contains_digit(password):
    """
    Vérifie si le mot de passe contient au moins un chiffre.

    Args:
        password (str): Le mot de passe à vérifier.

    Returns:
        bool: True si au moins un chiffre est présent, sinon False.
    """
    for char in password:
        if char.isdigit():
            return True
    return False

def contains_lowercase(password):
    """
    Vérifie si le mot de passe contient au moins une lettre minuscule.

    Args:
        password (str): Le mot de passe à vérifier.

    Returns:
        bool: True si au moins une minuscule est présente, sinon False.
    """
    for char in password:
        if char.islower():
            return True
    return False

def contains_uppercase(password):
    """
    Vérifie si le mot de passe contient au moins une lettre majuscule.

    Args:
        password (str): Le mot de passe à vérifier.

    Returns:
        bool: True si au moins une majuscule est présente, sinon False.
    """
    for char in password:
        if char.isupper():
            return True
    return False

def is_password_valid(password):
    """
    Vérifie si le mot de passe fourni respecte toutes les règles suivantes :
    - Au moins 6 caractères de long.
    - Contient au moins un chiffre.
    - Contient au moins une lettre minuscule.
    - Contient au moins une lettre majuscule.

    Args:
        password (str): Le mot de passe à vérifier.

    Returns:
        bool: True si le mot de passe est valide, sinon False.
    """
    # Compteur de conditions remplies
    criteria_met = 0

    # Vérification de la longueur minimale
    if has_minimum_length(password):
        criteria_met += 1

    # Vérification de la présence d'au moins un chiffre
    if contains_digit(password):
        criteria_met += 1

    # Vérification de la présence d'au moins une lettre minuscule
    if contains_lowercase(password):
        criteria_met += 1

    # Vérification de la présence d'au moins une lettre majuscule
    if contains_uppercase(password):
        criteria_met += 1

    # Le mot de passe est valide seulement si toutes les conditions sont remplies
    return criteria_met == 4

def main():
    """
    Point d'entrée du programme. Demande à l'utilisateur de saisir un mot de passe,
    vérifie sa validité et affiche 'VALID' ou 'INVALID' selon le résultat.
    """
    # Demande de saisie du mot de passe
    password = input()

    # Vérification de la validité du mot de passe
    if is_password_valid(password):
        print('VALID')
    else:
        print('INVALID')

if __name__ == "__main__":
    main()