def is_valid_password(password):
    """
    Vérifie si le mot de passe respecte les critères suivants :
    - Minimum 6 caractères
    - Ne doit pas être uniquement composé de lettres (toutes majuscules ou toutes minuscules)
    - Ne doit pas être uniquement composé de chiffres
    - Ne doit pas être composé uniquement de lettres sans majuscules/minuscules/ chiffres mélangés

    Args:
        password (str): Le mot de passe à vérifier.

    Returns:
        bool: True si le mot de passe est valide, False sinon.
    """
    # Vérifie si la longueur du mot de passe est inférieure à 6
    if len(password) < 6:
        return False
    # Vérifie si le mot de passe contient uniquement des lettres
    if password.isalpha():
        return False
    # Vérifie si le mot de passe est entièrement en minuscules
    if password.islower():
        return False
    # Vérifie si le mot de passe est entièrement en majuscules
    if password.isupper():
        return False
    # Vérifie si le mot de passe contient uniquement des chiffres
    if password.isdigit():
        return False
    # Si aucune des conditions ci-dessus n'est vraie, le mot de passe est valide
    return True

def main():
    """
    Point d'entrée du programme.
    Demande à l'utilisateur un mot de passe à valider et affiche s'il est valide ou non.
    """
    # Demande à l'utilisateur de saisir un mot de passe
    x = input()
    # Vérifie la validité du mot de passe à l'aide de la fonction is_valid_password
    if is_valid_password(x):
        print("VALID")
    else:
        print("INVALID")

# Exécute la fonction principale si le script est exécuté directement
if __name__ == "__main__":
    main()