def read_number_of_entries():
    """
    Demande à l'utilisateur de saisir un nombre entier.
    Renvoie :
        int : le nombre entier entré par l'utilisateur.
    """
    return int(input())

def count_digit_frequencies(n):
    """
    Compte la fréquence d'apparition des chiffres entre 0 et 9 pour n valeurs saisies par l'utilisateur.
    
    Paramètres :
        n (int) : nombre de valeurs à lire depuis l'utilisateur.
    
    Renvoie :
        list : une liste de 10 entiers, où chaque indice correspond au chiffre et la valeur à sa fréquence.
    """
    frequencies = [0] * 10  # Initialiser la fréquence de chaque chiffre à zéro
    for _ in range(n):
        digit = int(input())  # Lire un chiffre de l'utilisateur
        frequencies[digit] += 1  # Incrémenter la fréquence du chiffre approprié
    return frequencies

def display_frequencies(frequencies):
    """
    Affiche les fréquences des chiffres. Si un chiffre n'est pas présent, affiche '-'.
    Sinon, affiche autant d'étoiles '*' que la fréquence du chiffre.
    
    Paramètres :
        frequencies (list): la liste des fréquences à afficher.
    """
    for freq in frequencies:
        if freq == 0:
            print('-')  # Aucun chiffre trouvé à cette position
        else:
            print('*' * freq)  # Affiche autant d'étoiles que la fréquence

def main():
    """
    Fonction principale. Demande des séries de chiffres à l'utilisateur
    et affiche leur fréquence tant que l'utilisateur n'entre pas 0 pour terminer.
    """
    while True:
        n = read_number_of_entries()  # Lire le nombre d'occurences à traiter
        if n == 0:
            break  # Arrêter si la saisie est 0
        frequencies = count_digit_frequencies(n)  # Compter la fréquence des chiffres pour cette série
        display_frequencies(frequencies)  # Afficher le résultat

if __name__ == "__main__":
    main()