def main():
    """
    Programme principal qui lit un entier suivi d'une liste d'entiers, puis affiche
    le minimum, le maximum et la somme des éléments de la liste.
    """
    # Lire le nombre d'éléments dans la liste depuis l'entrée standard
    n = int(input())
    
    # Lire les entiers entrés par l'utilisateur et les convertir en liste d'entiers
    a = list(map(int, input().split()))
    
    # Calculer le minimum, le maximum et la somme de la liste
    min_val, max_val, total_sum = compute_min_max_sum(a)
    
    # Afficher le résultat : minimum, maximum et somme séparés par des espaces
    print(min_val, max_val, total_sum)

def compute_min_max_sum(values):
    """
    Calcule le minimum, le maximum et la somme d'une liste d'entiers.

    Args:
        values (list of int): Liste des valeurs entières à traiter.

    Returns:
        tuple: (min, max, sum) des éléments de la liste.
    """
    # Trier la liste pour obtenir aisément le minimum et le maximum
    sorted_values = sorted(values)
    
    # Le plus petit élément est le premier de la liste triée
    min_value = sorted_values[0]
    # Le plus grand élément est le dernier de la liste triée
    max_value = sorted_values[-1]
    # Calculer la somme de tous les éléments
    total = sum(values)
    
    return min_value, max_value, total

# Exécution du programme principal si ce fichier est exécuté directement
if __name__ == "__main__":
    main()