def get_suffix(N):
    """
    Détermine et affiche le suffixe correspondant à un chiffre donné
    selon des règles spécifiques :
      - Si le dernier chiffre est 2, 4, 5, 7 ou 9, affiche 'hon'
      - Si le dernier chiffre est 0, 1, 6 ou 8, affiche 'pon'
      - Si le dernier chiffre est 3, affiche 'bon'

    Paramètres
    ----------
    N : str
        Chaîne de caractères représentant un nombre.

    Retour
    ------
    None
    """
    # Récupération du dernier caractère (chiffre) de la chaîne N
    last_digit = int(N[-1])

    # Vérifie si le dernier chiffre correspond à l'un des suffixes selon la règle
    if last_digit in [2, 4, 5, 7, 9]:
        # Affiche 'hon' si la règle est respectée
        print('hon')
    if last_digit in [0, 1, 6, 8]:
        # Affiche 'pon' si la règle est respectée
        print('pon')
    if last_digit == 3:
        # Affiche 'bon' si la règle est respectée
        print('bon')

def main():
    """
    Fonction principale qui demande à l'utilisateur un nombre au format chaîne,
    puis affiche le suffixe approprié selon la valeur du dernier chiffre.
    """
    # Demande à l'utilisateur une saisie sous forme de chaîne de caractères
    N = input()
    # Appelle la fonction get_suffix avec N comme argument
    get_suffix(N)

# Appelle la fonction principale pour démarrer le programme
if __name__ == '__main__':
    main()