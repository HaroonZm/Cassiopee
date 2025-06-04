from collections import deque

def initialize_stacks(n):
    """
    Initialise une liste de piles (utilisant des deques) vides.

    Args:
        n (int): Le nombre de piles à initialiser.

    Returns:
        list: Une liste contenant n objets de type deque, représentant les piles.
    """
    stacks = []
    for _ in range(n):
        stacks.append(deque())
    return stacks

def process_queries(stacks, queries):
    """
    Traite une liste de requêtes sur les piles.

    Chaque requête peut être de trois types :
        - 0 t x : Empile la valeur x sur la pile d'indice t.
        - 1 t   : Affiche la valeur au sommet de la pile d'indice t si elle n'est pas vide.
        - 2 t   : Dépile l'élément au sommet de la pile d'indice t si elle n'est pas vide.

    Args:
        stacks (list of deque): Liste des piles à manipuler.
        queries (int): Le nombre de requêtes à traiter.

    Returns:
        None
    """
    for _ in range(queries):
        # Lecture d'une requête et traitement selon le type
        query = list(map(int, input().split()))
        q_type = query[0]     # Type de la requête (0, 1 ou 2)
        t = query[1]          # Indice de la pile concernée

        if q_type == 0:
            # Opération d'empilement : ajoute x sur la pile t
            x = query[2]
            stacks[t].append(x)

        elif q_type == 1:
            # Opération d'affichage : affiche le sommet de la pile t si non vide
            if stacks[t]:
                print(stacks[t][-1])

        elif q_type == 2:
            # Opération de dépilement : enlève le sommet de la pile t si non vide
            if stacks[t]:
                stacks[t].pop()

def main():
    """
    Point d'entrée principal du programme.

    Lit le nombre de piles et de requêtes, initialise les piles et traite les requêtes.
    """
    # Lecture du nombre de piles et du nombre de requêtes
    n, queries = map(int, input().split())

    # Initialisation des piles
    stacks = initialize_stacks(n)

    # Traitement des requêtes
    process_queries(stacks, queries)

if __name__ == '__main__':
    main()