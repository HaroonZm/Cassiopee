def read_numbers():
    """
    Lit le nombre d'éléments à saisir, puis lit la liste des entiers de l'utilisateur.

    Retourne :
        tuple : un tuple contenant un entier (le nombre d'éléments) et une liste d'entiers saisie par l'utilisateur.
    """
    # Lecture du nombre d'éléments attendus (non utilisé dans la suite mais gardé pour cohérence)
    num = int(input("Entrez le nombre d'éléments : "))
    # Lecture de la liste d'entiers séparés par des espaces, convertis en liste d'entiers
    numbers = [int(i) for i in input("Entrez les entiers séparés par des espaces : ").split()]
    return num, numbers

def get_min_max_sum(numbers):
    """
    Calcule la valeur minimale, la valeur maximale et la somme d'une liste d'entiers.

    Args:
        numbers (list): Liste des entiers à analyser.

    Retourne :
        tuple : Un tuple contenant la valeur minimale, la valeur maximale et la somme des entiers.
    """
    # Calcul du minimum de la liste
    min_num = min(numbers)
    # Calcul du maximum de la liste
    max_num = max(numbers)
    # Calcul de la somme de la liste
    sum_num = sum(numbers)
    return min_num, max_num, sum_num

def main():
    """
    Fonction principale du programme.
    Lit les saisies utilisateur, calcule les statistiques et affiche les résultats.
    """
    # Appel de la fonction pour lire l'entrée utilisateur
    num, numbers = read_numbers()
    # Calcul des valeurs min, max et somme
    min_num, max_num, sum_num = get_min_max_sum(numbers)
    # Affichage des résultats séparés par des espaces
    print(min_num, max_num, sum_num)

# Exécution du programme principal
if __name__ == "__main__":
    main()