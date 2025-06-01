List = [0] * 101  # Initialisation d'une liste de 101 éléments remplis de 0 (indices de 0 à 100)

def read_scores():
    """
    Lit des paires de valeurs entières (p, s) séparées par une virgule depuis l'entrée standard.
    Chaque paire représente un index p dans la liste et une valeur s à assigner.
    L'entrée se termine lorsque la paire (0, 0) est rencontrée.
    
    Modifie la liste globale 'List' en assignant List[p] = s.
    """
    while True:
        # Lecture d'une paire p, s depuis l'entrée standard, séparée par une virgule
        p, s = map(int, input().split(","))
        # Condition d'arrêt de la lecture : la paire (0, 0)
        if p == 0 and s == 0:
            break
        # Affectation de la valeur s à l'index p dans la liste List
        List[p] = s

def create_sorted_unique_list():
    """
    Crée une nouvelle liste triée des valeurs uniques de 'List' en ordre décroissant.
    
    Returns:
        list: Une liste sorted en ordre décroissant des valeurs distinctes dans 'List'.
    """
    # Conversion en set pour obtenir les valeurs uniques, puis tri décroissant
    return sorted(set(List), reverse=True)

def process_queries(Sorted_List):
    """
    Lit des entrées entières q (indices) depuis l'entrée standard jusqu'à la fin de fichier (EOF),
    puis affiche pour chaque q la position (1-based) de List[q] dans Sorted_List.
    
    Args:
        Sorted_List (list): Liste triée des valeurs uniques pour déterminer le rang.
    """
    while True:
        try:
            # Lecture d'un entier q
            q = int(input())
        except EOFError:
            # Fin des données d'entrée, on sort de la boucle
            break
        # Calcul de l'indice (1-based) de la valeur List[q] dans Sorted_List et affichage
        rank = Sorted_List.index(List[q]) + 1
        print(rank)

# Lecture et affectation des scores dans la liste List
read_scores()

# Création de la liste triée des scores uniques
Sorted_List = create_sorted_unique_list()

# Traitement des requêtes de rang et affichage des résultats
process_queries(Sorted_List)