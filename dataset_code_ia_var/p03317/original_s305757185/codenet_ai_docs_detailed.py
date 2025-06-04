import math

def calculate_minimum_trips(N, K, A):
    """
    Calcule le nombre minimal de voyages nécessaires pour traiter tous les éléments d'une liste A,
    sachant que chaque voyage peut traiter jusqu'à K éléments, et que le premier élément est traité au premier voyage,
    puis chaque voyage suivant traite jusqu'à K-1 nouveaux éléments non encore traités.

    Args:
        N (int): Le nombre total d'éléments à traiter.
        K (int): Le nombre maximal d'éléments pouvant être traités lors du premier voyage,
                 puis chaque voyage suivant peut ajouter jusqu'à K-1 nouveaux éléments.
        A (List[int]): La liste des éléments à traiter.

    Returns:
        int: Le nombre minimum de voyages nécessaires pour traiter tous les éléments.
    """
    # On calcule le nombre d'éléments restant à traiter après le premier voyage (N-1)
    # Chaque voyage additionnel permet de traiter jusqu'à (K-1) nouveaux éléments non encore traités
    # On utilise math.ceil pour s'assurer d'arrondir vers le haut si la division n'est pas entière
    trips = math.ceil((N - 1) / (K - 1))
    return trips

if __name__ == "__main__":
    # Lecture des entrées utilisateur
    # N: le nombre total d'éléments, K: la capacité du premier voyage
    N, K = map(int, input().split())
    # Lecture de la liste des éléments à traiter
    A = list(map(int, input().split()))
    # Appel de la fonction et affichage du résultat
    print(calculate_minimum_trips(N, K, A))