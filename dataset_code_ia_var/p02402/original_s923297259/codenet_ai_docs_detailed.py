def get_min_max_sum(numbers):
    """
    Calcule et renvoie la valeur minimale, maximale et la somme d'une liste de nombres.

    Args:
        numbers (list of int): Liste des nombres à analyser.

    Returns:
        tuple: Un triplet contenant la valeur minimale, la valeur maximale et la somme.
    """
    min_value = min(numbers)  # Trouve la plus petite valeur de la liste
    max_value = max(numbers)  # Trouve la plus grande valeur de la liste
    total = sum(numbers)      # Calcule la somme de la liste
    return min_value, max_value, total

def main():
    """
    Fonction principale du programme.
    Lit les entrées utilisateur, traite les données et affiche le résultat.
    """
    # Lire le nombre d'éléments dans la liste
    n = int(input())
    
    # Lire les éléments de la liste sous forme de chaîne, puis les convertir en entiers
    A = list(map(int, input().split()))
    
    # Appeler la fonction pour obtenir min, max, et somme
    minimum, maximum, total_sum = get_min_max_sum(A)
    
    # Afficher les résultats sous le format demandé
    print(minimum, maximum, total_sum)

# Appeler la fonction principale lorsque l'exécution commence ici
if __name__ == "__main__":
    main()