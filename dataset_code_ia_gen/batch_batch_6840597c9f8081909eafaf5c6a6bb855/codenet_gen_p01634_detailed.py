# Solution complète en Python pour le problème "Register Phase"

# L'approche utilisée est simple : on vérifie chaque condition 
# imposée par l'énoncé à l'aide de méthodes et de boucles.

# Etapes :
# 1. Lire la chaîne de caractères représentant le mot de passe.
# 2. Vérifier la longueur (>=6).
# 3. Vérifier la présence d'au moins un chiffre.
# 4. Vérifier la présence d'au moins une lettre majuscule.
# 5. Vérifier la présence d'au moins une lettre minuscule.
# 6. Afficher "VALID" si toutes les conditions sont remplies, sinon "INVALID".

def main():
    password = input().strip()

    # Condition 1: longueur >= 6
    if len(password) < 6:
        print("INVALID")
        return

    has_digit = False
    has_upper = False
    has_lower = False

    # Parcourir chaque caractère du mot de passe pour vérifier les autres conditions
    for ch in password:
        if ch.isdigit():
            has_digit = True
        elif ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True

    # Vérification finale des conditions
    if has_digit and has_upper and has_lower:
        print("VALID")
    else:
        print("INVALID")

if __name__ == "__main__":
    main()