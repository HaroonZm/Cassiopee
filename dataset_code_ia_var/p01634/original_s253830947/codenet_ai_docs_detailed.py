def is_valid_password(s):
    """
    Vérifie si le mot de passe fourni respecte les critères suivants :
    - Au moins 6 caractères de long.
    - Contient au moins une lettre majuscule (A-Z).
    - Contient au moins une lettre minuscule (a-z).
    - Contient au moins un chiffre (0-9).
    
    Args:
        s (str): Le mot de passe à vérifier.
        
    Returns:
        bool: True si le mot de passe est valide, False sinon.
    """
    # Vérifier que la longueur du mot de passe est d'au moins 6 caractères
    if len(s) < 6:
        return False

    # Initialiser les compteurs pour les chiffres, lettres minuscules et lettres majuscules
    num = 0   # Compte le nombre de chiffres
    lower = 0 # Compte le nombre de lettres minuscules
    upper = 0 # Compte le nombre de lettres majuscules

    # Parcourir chaque caractère du mot de passe
    for i in range(len(s)):
        # Vérifier si le caractère est un chiffre (code ASCII de 0 à 9 : 48 à 57)
        if ord(s[i]) >= 48 and ord(s[i]) <= 57:
            num += 1
        # Vérifier si le caractère est une lettre minuscule (a-z : 97 à 122)
        if ord(s[i]) >= 97 and ord(s[i]) <= 122:
            lower += 1
        # Vérifier si le caractère est une lettre majuscule (A-Z : 65 à 90)
        if ord(s[i]) >= 65 and ord(s[i]) <= 90:
            upper += 1

    # Le mot de passe doit contenir au moins un chiffre, une minuscule et une majuscule
    if num == 0 or lower == 0 or upper == 0:
        return False
    else:
        return True

def main():
    """
    Fonction principale qui lit une chaîne depuis l'entrée utilisateur
    et affiche "VALID" si la chaîne respecte les critères de mot de passe,
    "INVALID" sinon.
    """
    # Lire la chaîne entrée par l'utilisateur
    s = str(input())
    
    # Vérifier la validité du mot de passe et afficher le résultat approprié
    if is_valid_password(s):
        print("VALID")
    else:
        print("INVALID")

# Exécution du script
if __name__ == "__main__":
    main()