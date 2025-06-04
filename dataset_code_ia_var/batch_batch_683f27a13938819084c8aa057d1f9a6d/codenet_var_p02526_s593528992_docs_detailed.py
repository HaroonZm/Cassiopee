def main():
    """
    Exécute le programme principal :
    - Lit deux ensembles de chaînes de caractères entrés par l'utilisateur.
    - Calcule et affiche le cardinal de leur intersection.
    """
    # Il est préférable d'utiliser input() dans Python 3 pour lire les entrées utilisateur,
    # mais raw_input() est utilisé dans Python 2. Ici, nous utilisons input() selon la consigne moderne.
    
    # Lecture du nombre d'éléments du premier ensemble (la valeur n'est pas utilisée directement)
    input()
    # Lecture des éléments du premier ensemble depuis une ligne d'entrée utilisateur,
    # puis conversion en ensemble de chaînes de caractères
    S = set(input().split())
    
    # Lecture du nombre d'éléments du second ensemble (la valeur n'est pas utilisée directement)
    input()
    # Lecture des éléments du second ensemble depuis une ligne d'entrée utilisateur,
    # puis conversion en ensemble de chaînes de caractères
    T = set(input().split())
    
    # Calcul de l'intersection des deux ensembles S et T à l'aide de l'opérateur &
    intersection = S & T
    
    # Affichage du cardinal (nombre d'éléments) de l'intersection
    print(len(intersection))

if __name__ == "__main__":
    main()