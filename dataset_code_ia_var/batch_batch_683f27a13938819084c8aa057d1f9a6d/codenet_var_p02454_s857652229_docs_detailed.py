from bisect import bisect

def read_input_list():
    """
    Lit une ligne de l'entrée standard et la convertit en une liste d'entiers.

    Returns:
        list: Une liste d'entiers issus de l'entrée utilisateur.
    """
    return list(map(int, input().split()))

def process_queries(a, num_query):
    """
    Traite une série de requêtes de recherche à l'aide du module bisect.

    Pour chaque requête contenant un entier k, affiche deux valeurs :
    - L'indice d'insertion de k - 1 dans la liste triée a (nombre d'éléments < k)
    - L'indice d'insertion de k dans la liste triée a (nombre d'éléments <= k)

    Args:
        a (list): Une liste d'entiers triés en ordre croissant.
        num_query (int): Le nombre total de requêtes à traiter.

    Returns:
        None
    """
    for _ in range(num_query):
        k = int(input())
        left_index = bisect(a, k - 1)  # Éléments strictement inférieurs à k
        right_index = bisect(a, k)     # Éléments inférieurs ou égaux à k
        print(f"{left_index} {right_index}")

if __name__ == "__main__":
    # Lecture du nombre d'éléments dans la liste
    n = int(input())

    # Lecture de la liste de n entiers, supposée triée
    a = read_input_list()

    # Lecture du nombre de requêtes à traiter
    num_query = int(input())

    # Traitement des requêtes et affichage des résultats
    process_queries(a, num_query)