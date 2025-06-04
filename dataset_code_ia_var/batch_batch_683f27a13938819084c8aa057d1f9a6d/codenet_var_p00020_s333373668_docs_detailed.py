def main():
    """
    Fonction principale qui lit une chaîne de caractères depuis l'entrée utilisateur,
    convertit cette chaîne en majuscules puis l'affiche.
    """
    # Demande à l'utilisateur de saisir une chaîne de caractères
    x = input("Veuillez entrer une chaîne de caractères : ")

    # Convertit la chaîne saisie en majuscules
    x_upper = convert_to_uppercase(x)

    # Affiche la chaîne convertie
    print(x_upper)

def convert_to_uppercase(text):
    """
    Prend une chaîne de caractères en entrée et retourne une nouvelle chaîne
    où tous les caractères sont en majuscule.

    Args:
        text (str): La chaîne de caractères à convertir.

    Returns:
        str: La chaîne de caractères convertie en majuscules.
    """
    # Utilise la méthode upper() de la classe str pour tout mettre en majuscules
    return text.upper()

if __name__ == "__main__":
    main()