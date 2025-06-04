def read_set(prompt):
    """
    Lit une ligne de l'entrée utilisateur, la divise en éléments et retourne un ensemble (set).
    
    Args:
        prompt (str): Message affiché pour demander l'entrée utilisateur.
        
    Returns:
        set: Un ensemble des éléments entrés par l'utilisateur sous forme de chaînes de caractères.
    """
    input_line = raw_input(prompt)
    # Utilise split() pour diviser la ligne en éléments séparés
    return set(input_line.split())

def intersect_sets(set1, set2):
    """
    Calcule et retourne l'intersection de deux ensembles.
    
    Args:
        set1 (set): Premier ensemble.
        set2 (set): Deuxième ensemble.
        
    Returns:
        set: Un ensemble résultant de l'intersection de set1 et set2.
    """
    return set1 & set2

def main():
    """
    Fonction principale qui :
      1. Lit deux ensembles de l'utilisateur
      2. Calcule leur intersection
      3. Affiche la taille (cardinalité) de l'intersection
    """
    # Récupère le nombre d'éléments dans le premier ensemble (n), sans utilisation ultérieure
    n = int(raw_input())
    
    # Lis le premier ensemble S depuis l'entrée utilisateur
    S = read_set("")  # Pas de prompt pour respecter l'entrée sans modification

    # Récupère le nombre d'éléments dans le second ensemble (q), sans utilisation ultérieure
    q = int(raw_input())
    
    # Lis le second ensemble T depuis l'entrée utilisateur
    T = read_set("")
    
    # Calcule l'intersection des deux ensembles S et T
    intersection = intersect_sets(S, T)
    
    # Affiche le nombre d'éléments communs aux deux ensembles
    print len(intersection)

# Appel du point d'entrée principal du script
if __name__ == "__main__":
    main()