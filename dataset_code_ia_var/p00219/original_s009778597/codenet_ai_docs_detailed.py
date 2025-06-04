def read_numbers():
    """
    Lit un nombre entier n depuis l'entrée standard, puis lit n entiers supplémentaires pour constituer une liste.

    Returns:
        list: La liste des entiers lus depuis l'entrée.
        Si n vaut 0, retourne None pour signaler la fin des lectures.
    """
    n = int(input())  # Lire le nombre d'éléments à saisir
    if n == 0:
        return None
    numbers = []
    for _ in range(n):
        value = int(input())  # Lire chaque entier individuellement
        numbers.append(value)
    return numbers

def count_digits(numbers):
    """
    Compte le nombre d'occurrences de chaque chiffre de 0 à 9 dans la liste fournie.

    Args:
        numbers (list): Liste des entiers (supposés entre 0 et 9).

    Returns:
        list: Une liste de taille 10 contenant le nombre d'apparitions de chaque chiffre (index = chiffre).
    """
    digit_counts = [0 for _ in range(10)]  # Initialiser un compteur pour chaque chiffre de 0 à 9
    for number in numbers:
        digit = int(number)  # S'assurer que c'est bien un chiffre (0..9)
        digit_counts[digit] += 1  # Incrémenter le compteur du chiffre correspondant
    return digit_counts

def print_histogram(digit_counts):
    """
    Affiche un histogramme horizontal pour chaque chiffre de 0 à 9 selon leur fréquence.

    Args:
        digit_counts (list): Liste de fréquences où l'index correspond au chiffre.
    """
    for count in digit_counts:
        if count == 0:
            print('-')       # Affiche '-' si le chiffre n'est pas présent
        else:
            print('*' * count)  # Affiche autant d'étoiles que d'occurrences du chiffre

def main():
    """
    Boucle principale qui lit plusieurs séquences de chiffres et affiche à chaque fois leur histogramme.
    Arrête la lecture lorsqu'un 0 est entré à la place de la taille de séquence.
    """
    while True:
        numbers = read_numbers()  # Lire la prochaine séquence de chiffres
        if numbers is None:       # Si on reçoit None, sortir de la boucle principale
            break
        digit_counts = count_digits(numbers)  # Compter les occurrences des chiffres
        print_histogram(digit_counts)         # Afficher l'histogramme correspondant

# Démarrage du programme principal
main()