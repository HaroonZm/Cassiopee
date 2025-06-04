def classify_japanese_suffix(number_str):
    """
    Détermine le suffixe japonais à utiliser pour un nombre donné en fonction de son dernier chiffre.

    Args:
        number_str (str): Le nombre saisi par l'utilisateur sous forme de chaîne de caractères.

    Returns:
        str: Le suffixe approprié pour le nombre ('hon', 'pon', ou 'bon').
    """
    # Extraire le dernier caractère de la chaîne (le dernier chiffre)
    last_digit = number_str[-1]

    # Vérifier quel suffixe correspond au dernier chiffre selon les règles japonaises de comptage des objets longs et fins
    if last_digit in ('2', '4', '5', '7', '9'):
        return 'hon'
    elif last_digit in ('0', '1', '6', '8'):
        return 'pon'
    else:
        return 'bon'

if __name__ == "__main__":
    # Lire l'entrée utilisateur depuis la console
    user_input = input()
    # Appeler la fonction pour déterminer le suffixe correct et afficher le résultat
    print(classify_japanese_suffix(user_input))