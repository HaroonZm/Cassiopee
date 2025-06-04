def get_sum_of_inputs(count):
    """
    Lit `count` entiers depuis l'entrée standard, calcule et retourne leur somme.

    Args:
        count (int): Le nombre de valeurs à lire.

    Returns:
        int: La somme des valeurs lues.
    """
    # Créer une liste vide pour stocker les valeurs lues
    numbers = []
    # Boucler 'count' fois pour lire les entiers
    for i in range(count):
        # Lecture d'un entier depuis l'entrée utilisateur
        value = int(raw_input())
        # Ajouter la valeur à la liste
        numbers.append(value)
    # Calculer la somme des nombres lus
    total = sum(numbers)
    return total

def main():
    """
    Fonction principale du programme.
    Lit un entier N depuis l'entrée, puis lit N entiers supplémentaires,
    calcule leur moyenne, et affiche le résultat.
    """
    # Lecture du nombre d'éléments à lire
    N = input()
    # Calcul de la somme des N éléments lus
    total_sum = get_sum_of_inputs(N)
    # Calcul de la moyenne (division entière en Python 2)
    average = total_sum / N
    # Affichage de la moyenne calculée
    print average

# Appel de la fonction principale pour exécuter le script
main()