def validate_password():
    """
    Lit un mot de passe de l'utilisateur, vérifie sa validité selon les critères suivants :
    - Au moins 6 caractères de long
    - Doit contenir à la fois minuscules, majuscules, chiffres et/ou symboles
    - Ne peut pas être uniquement en minuscules, ou uniquement en majuscules, ou uniquement alphabétique, ou uniquement numérique

    Affiche 'VALID' si le mot de passe est valide, sinon 'INVALID'.
    """
    # Lecture de la saisie utilisateur sous forme de chaîne de caractères
    p = raw_input()

    # Déterminer la validité du mot de passe suivant les règles spécifiées :
    # - Longueur inférieure à 6 => invalide
    condition_length = len(p) < 6
    # - Tout en minuscules => invalide
    condition_islower = p.islower()
    # - Tout en majuscules => invalide
    condition_isupper = p.isupper()
    # - Composé uniquement de lettres => invalide
    condition_isalpha = p.isalpha()
    # - Composé uniquement de chiffres => invalide
    condition_isdigit = p.isdigit()

    # Si une des conditions d'invalidité est vraie, alors le mot de passe est invalide
    if condition_length or condition_islower or condition_isupper or condition_isalpha or condition_isdigit:
        print "INVALID"
    else:
        # Sinon, le mot de passe est valide
        print "VALID"

# Appel de la fonction principale
validate_password()