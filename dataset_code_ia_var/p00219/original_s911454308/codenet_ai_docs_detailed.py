def get_integer_input():
    """
    Demande à l'utilisateur de saisir un nombre entier.
    
    Returns:
        int: Le nombre saisi par l'utilisateur.
    """
    return int(input())

def count_input_occurrences(n):
    """
    Compte le nombre d'occurrences de chaque chiffre entre 0 et 9 dans les entrées utilisateur.
    
    Args:
        n (int): Nombre d'entrées à lire.
    
    Returns:
        list: Une liste de 10 entiers représentant la fréquence des chiffres 0 à 9.
    """
    # Initialisation de la liste des comptes pour chaque chiffre (indices 0 à 9)
    data = [0 for _ in range(10)]
    for _ in range(n):
        value = get_integer_input()
        if 0 <= value <= 9:
            # Incrémente le compteur de la valeur lue
            data[value] += 1
    return data

def print_histogram(data):
    """
    Affiche un histogramme basé sur la liste de fréquences passée en argument.
    Affiche '-' pour les chiffres n'ayant aucune occurrence, et une ligne de '*' pour les autres.
    
    Args:
        data (list): Liste des fréquences pour les chiffres 0 à 9.
    """
    for count in data:
        if count == 0:
            print("-")
        else:
            print("*" * count)

def main():
    """
    Programme principal.
    À chaque itération, lit un nombre n.
    Si n vaut 0, arrête le programme.
    Sinon, lit n fois un chiffre (0 à 9) et affiche l'histogramme des fréquences.
    """
    while True:
        n = get_integer_input()
        # Condition d'arrêt si l'utilisateur entre 0
        if n == 0:
            break
        # Compter les occurrences pour n valeurs entrées
        data = count_input_occurrences(n)
        # Afficher l'histogramme correspondant
        print_histogram(data)

# Lancer le programme principal
main()