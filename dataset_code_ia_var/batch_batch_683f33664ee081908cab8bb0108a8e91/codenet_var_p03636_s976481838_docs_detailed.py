def compress_string(s):
    """
    Compresse une chaîne en suivant le format : première lettre + nombre de caractères du milieu + dernière lettre.

    Exemple :
        "internationalization" -> "i18n"

    Args:
        s (str): La chaîne à compresser.

    Returns:
        str: La chaîne compressée.
    """
    # Si la chaîne a moins de 2 caractères, la compression n’a pas de sens.
    if len(s) <= 2:
        return s

    # Obtenir le premier caractère
    first_char = s[0]

    # Compter le nombre de caractères entre le premier et le dernier caractère
    middle_length = len(s[1:-1])

    # Obtenir le dernier caractère
    last_char = s[-1]

    # Construire et retourner la chaîne compressée
    return first_char + str(middle_length) + last_char

def main():
    """
    Lit une chaîne depuis l'entrée standard, la compresse et l'affiche.
    """
    # Lecture de l'entrée utilisateur
    s = input()
    # Compression de la chaîne et affichage du résultat
    print(compress_string(s))

if __name__ == "__main__":
    main()