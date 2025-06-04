def read_int() -> int:
    """
    Lit une ligne d'entrée et la convertit en un entier.
    
    Returns:
        int: La valeur entière lue depuis l'entrée standard.
    """
    return int(input())

def read_int_set() -> set:
    """
    Lit une ligne d'entrée composée d'entiers séparés par des espaces et la convertit en un ensemble d'entiers.
    
    Returns:
        set: Ensemble d'entiers extraits de la ligne d'entrée.
    """
    return set(map(int, input().split()))

def is_superset() -> int:
    """
    Détermine si le premier ensemble d'entiers est un surensemble du second ensemble.
    
    Lit les ensembles et leur taille depuis l'entrée standard selon le format suivant:
        - Un entier n (taille du premier ensemble, mais ici inutilisé directement)
        - n entiers (éléments du premier ensemble)
        - Un entier m (taille du second ensemble, mais ici inutilisé directement)
        - m entiers (éléments du second ensemble)
        
    Returns:
        int: 1 si le premier ensemble est un surensemble du deuxième, 0 sinon.
    """
    n = read_int()                # Lecture de la taille du premier ensemble (inutile car set() gère la taille)
    a = read_int_set()            # Lecture des éléments du premier ensemble
    m = read_int()                # Lecture de la taille du second ensemble (inutile car set() gère la taille)
    b = read_int_set()            # Lecture des éléments du second ensemble

    # Vérifie si 'a' est un surensemble de 'b'. Convertit le booléen en entier:
    return int(a.issuperset(b))

if __name__ == "__main__":
    # Appelle la fonction principale et affiche le résultat
    print(is_superset())