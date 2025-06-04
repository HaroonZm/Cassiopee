import sys

def find_A_to_Z_length(s):
    """
    Calcule la longueur de la sous-chaîne la plus courte qui commence par le premier 'A'
    et se termine au dernier 'Z' dans la chaîne donnée.

    Args:
        s (str): La chaîne de caractères à analyser.

    Returns:
        int: La longueur entre le premier 'A' et le dernier 'Z' (inclus).
             Retourne -1 si l'un des caractères n'est pas trouvé.
    """

    # Recherche l'index du premier 'A' dans la chaîne
    a_index = s.find("A")
    # Recherche l'index du dernier 'Z' dans la chaîne
    z_index = s.rfind("Z")

    # Si ni 'A' ni 'Z' ne sont trouvés, retourne -1 comme valeur d'erreur
    if a_index == -1 or z_index == -1 or z_index < a_index:
        return -1

    # Calcule la longueur de la sous-chaîne allant du premier 'A' au dernier 'Z'
    length = z_index - a_index + 1
    return length

def main():
    """
    Point d'entrée du script.
    Lit une entrée standard, traite la chaîne, et affiche la longueur trouvée.
    """
    # Demande à l'utilisateur de saisir une chaîne de caractères
    s = input()

    # Calcule la longueur cherchée via find_A_to_Z_length
    result = find_A_to_Z_length(s)

    # Affiche le résultat au format requis
    print("{}".format(result))

if __name__ == "__main__":
    main()